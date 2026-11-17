import os
import json
import math
import asyncio
from contextlib import asynccontextmanager
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

DATA_DIR = "data"
CITY_FILES = {
    "Đà Lạt": os.path.join(DATA_DIR, "places_dalat.json"),
    "Nha Trang": os.path.join(DATA_DIR, "places_nhatrang.json")
}

# Nếu file dữ liệu ở thư mục gốc thì sử dụng file gốc
for city, path in CITY_FILES.items():
    if not os.path.exists(path):
        filename = os.path.basename(path)
        if os.path.exists(filename):
            CITY_FILES[city] = filename

PRESET_TYPES = ["Attraction", "Restaurant", "Café", "Accommodation"]

PRESET_VIBES = [
    "Nature", "Chill", "Adventure", "Romantic", "Cultural",
    "View_Hunting", "Culinary", "Local_Food", "Relaxation",
    "Luxury", "Budget_Friendly", "Photography", "Trending", "Sightseeing"
]

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")

def sync_place_with_google_api(place: dict) -> dict:
    if not GOOGLE_MAPS_API_KEY:
        return place
    try:
        url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place['name']}&inputtype=textquery&fields=rating,formatted_address,place_id,opening_hours&key={GOOGLE_MAPS_API_KEY}"
        res = requests.get(url, timeout=5).json()
        if res.get("status") == "OK" and res.get("candidates"):
            candidate = res["candidates"][0]
            if "rating" in candidate:
                place["rating"] = candidate["rating"]
            if "formatted_address" in candidate:
                place["new_address"] = candidate["formatted_address"]
    except Exception as e:
        print(f"Sync error for {place['name']}: {e}")
    return place

async def periodic_data_sync():
    while True:
        await asyncio.sleep(43200) # 12 tiếng
        for city, filepath in CITY_FILES.items():
            if os.path.exists(filepath):
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        places = json.load(f)
                    updated_places = [sync_place_with_google_api(p) for p in places]
                    with open(filepath, "w", encoding="utf-8") as f:
                        json.dump(updated_places, f, ensure_ascii=False, indent=2)
                except Exception as e:
                    print(f"Sync failed for {city}: {e}")

# SỬA CẢNH BÁO DEPRECATION: Sử dụng lifespan thay cho @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    sync_task = asyncio.create_task(periodic_data_sync())
    yield
    sync_task.cancel()

app = FastAPI(title="Smart Travel Planner Engine v2", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def calculate_haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

def compute_jaccard_similarity(user_vibes: List[str], place_vibes: List[str]) -> float:
    set_user = set(user_vibes)
    set_place = set(place_vibes)
    if not set_user or not set_place:
        return 0.0
    intersection = set_user.intersection(set_place)
    union = set_user.union(set_place)
    return len(intersection) / len(union)

class DailyPreference(BaseModel):
    day_number: int
    selected_types: List[str]
    selected_vibes: List[str]

class TripPlannerInput(BaseModel):
    destination: str          
    budget_k_vnd: float       
    days: int                 
    party_size: int           
    preference_mode: str      
    global_types: Optional[List[str]] = []
    global_vibes: Optional[List[str]] = []
    daily_preferences: Optional[List[DailyPreference]] = []

@app.get("/api/config-data")
def get_config_data():
    return {
        "cities": list(CITY_FILES.keys()),
        "preset_types": PRESET_TYPES,
        "preset_vibes": PRESET_VIBES
    }

@app.get("/api/places/{city}")
def get_city_places(city: str):
    filepath = CITY_FILES.get(city)
    if not filepath or not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail=f"Không tìm thấy dữ liệu địa điểm cho {city}!")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

@app.post("/api/generate-itinerary")
def generate_itinerary(payload: TripPlannerInput):
    filepath = CITY_FILES.get(payload.destination)
    if not filepath or not os.path.exists(filepath):
        raise HTTPException(status_code=400, detail="Thành phố không hợp lệ hoặc chưa có dữ liệu!")

    with open(filepath, "r", encoding="utf-8") as f:
        all_places = json.load(f)

    total_budget_vnd = payload.budget_k_vnd * 1000

    accommodations = [p for p in all_places if p.get("type") == "Accommodation"]
    restaurants = [p for p in all_places if p.get("type") == "Restaurant"]
    attractions = [p for p in all_places if p.get("type") == "Attraction"]
    cafes = [p for p in all_places if p.get("type") == "Café"]

    # Kiểm tra tính khả thi ngân sách
    min_acc_price = min([p.get("avg_price", 0) for p in accommodations]) if accommodations else 200000
    rooms_needed = math.ceil(payload.party_size / 2)
    min_hotel_cost = min_acc_price * max(1, payload.days - 1) * rooms_needed

    min_food_cost = 150000 * payload.party_size * payload.days
    min_required_budget = min_hotel_cost + min_food_cost

    if total_budget_vnd < min_required_budget:
        return {
            "status": "warning",
            "message": f"Ngân sách {payload.budget_k_vnd:,.0f}k VNĐ ({total_budget_vnd:,.0f} VNĐ) quá thấp! Với đoàn {payload.party_size} người đi {payload.days} ngày tại {payload.destination}, chi phí tối thiểu cho lưu trú ({min_hotel_cost:,.0f}đ) và ăn uống ({min_food_cost:,.0f}đ) là khoảng {min_required_budget/1000:,.0f}k VNĐ. Vui lòng tăng ngân sách."
        }

    # Chọn khách sạn tối ưu
    selected_hotel = accommodations[0]
    hotel_budget_allowance = (total_budget_vnd * 0.35) / max(1, (payload.days - 1) * rooms_needed)
    suitable_hotels = [h for h in accommodations if h.get("avg_price", 0) <= hotel_budget_allowance]
    if suitable_hotels:
        suitable_hotels.sort(key=lambda x: x.get("rating", 0), reverse=True)
        selected_hotel = suitable_hotels[0]
    else:
        accommodations.sort(key=lambda x: x.get("avg_price", 0))
        selected_hotel = accommodations[0]

    actual_hotel_cost = selected_hotel.get("avg_price", 0) * max(1, payload.days - 1) * rooms_needed

    used_attraction_ids = set()
    used_restaurant_ids = set()

    daily_itinerary = []
    total_estimated_cost = actual_hotel_cost
    total_distance_km = 0.0

    for day in range(1, payload.days + 1):
        if payload.preference_mode == "per_day" and payload.daily_preferences:
            day_pref = next((dp for dp in payload.daily_preferences if dp.day_number == day), None)
            target_types = day_pref.selected_types if day_pref and day_pref.selected_types else PRESET_TYPES
            target_vibes = day_pref.selected_vibes if day_pref and day_pref.selected_vibes else PRESET_VIBES
        else:
            target_types = payload.global_types if payload.global_types else PRESET_TYPES
            target_vibes = payload.global_vibes if payload.global_vibes else PRESET_VIBES

        def get_best_candidates(pool: List[dict], used_set: set, count: int, category_type: str) -> List[dict]:
            filtered_pool = [p for p in pool if p.get("type") == category_type or category_type == "Any"]
            if not filtered_pool:
                filtered_pool = pool

            scored_list = []
            for p in filtered_pool:
                score = compute_jaccard_similarity(target_vibes, p.get("vibes", []))
                scored_list.append({"place": p, "score": score, "used": p["stt"] in used_set})

            scored_list.sort(key=lambda x: (not x["used"], x["score"], x["place"].get("rating", 0)), reverse=True)

            selected = []
            for item in scored_list:
                if len(selected) < count:
                    p = item["place"]
                    selected.append(p)
                    used_set.add(p["stt"])

            while len(selected) < count and pool:
                selected.append(pool[len(selected) % len(pool)])

            return selected

        breakfast = get_best_candidates(restaurants, used_restaurant_ids, 1, "Restaurant")[0]
        morning_attraction = get_best_candidates(attractions + cafes, used_attraction_ids, 1, "Any")[0]
        lunch = get_best_candidates(restaurants, used_restaurant_ids, 1, "Restaurant")[0]
        afternoon_attraction = get_best_candidates(attractions + cafes, used_attraction_ids, 1, "Any")[0]
        dinner = get_best_candidates(restaurants, used_restaurant_ids, 1, "Restaurant")[0]

        day_schedule = []
        prev_loc = (selected_hotel["lat"], selected_hotel["lng"])

        # 1. Bữa sáng
        d = calculate_haversine(prev_loc[0], prev_loc[1], breakfast["lat"], breakfast["lng"])
        total_distance_km += d
        cost = breakfast.get("avg_price", 0) * payload.party_size
        total_estimated_cost += cost
        day_schedule.append({
            "time": "07:30 - 08:30",
            "category": "🍳 Bữa Sáng Địa Phương",
            "place": breakfast,
            "cost_vnd": cost,
            "distance_km": d,
            "note": "Bắt đầu ngày mới với món ăn đặc sản."
        })
        prev_loc = (breakfast["lat"], breakfast["lng"])

        # 2. Tham quan sáng
        d = calculate_haversine(prev_loc[0], prev_loc[1], morning_attraction["lat"], morning_attraction["lng"])
        total_distance_km += d
        cost = morning_attraction.get("avg_price", 0) * payload.party_size
        total_estimated_cost += cost
        day_schedule.append({
            "time": "09:00 - 11:30",
            "category": "🏞️ Tham Quan / Săn Ảnh Sáng",
            "place": morning_attraction,
            "cost_vnd": cost,
            "distance_km": d,
            "note": "Thời điểm chụp ảnh đẹp và không khí mát mẻ."
        })
        prev_loc = (morning_attraction["lat"], morning_attraction["lng"])

        # 3. Ăn trưa & Nghỉ trưa
        d = calculate_haversine(prev_loc[0], prev_loc[1], lunch["lat"], lunch["lng"])
        total_distance_km += d
        cost = lunch.get("avg_price", 0) * payload.party_size
        total_estimated_cost += cost
        day_schedule.append({
            "time": "11:30 - 13:30",
            "category": "🍲 Bữa Trưa & Thư Giãn",
            "place": lunch,
            "cost_vnd": cost,
            "distance_km": d,
            "note": "Dùng bữa trưa và nghỉ ngơi khôi phục năng lượng."
        })
        prev_loc = (lunch["lat"], lunch["lng"])

        # 4. Tham quan / Cà phê chiều
        d = calculate_haversine(prev_loc[0], prev_loc[1], afternoon_attraction["lat"], afternoon_attraction["lng"])
        total_distance_km += d
        cost = afternoon_attraction.get("avg_price", 0) * payload.party_size
        total_estimated_cost += cost
        day_schedule.append({
            "time": "14:00 - 16:30",
            "category": "☕ Trải Nghiệm Chiều / Vui Chơi",
            "place": afternoon_attraction,
            "cost_vnd": cost,
            "distance_km": d,
            "note": "Thưởng thức cà phê view đẹp hoặc check-in điểm đến nổi tiếng."
        })
        prev_loc = (afternoon_attraction["lat"], afternoon_attraction["lng"])

        # 5. Khung thời gian nghỉ ngơi chiều
        d_hotel = calculate_haversine(prev_loc[0], prev_loc[1], selected_hotel["lat"], selected_hotel["lng"])
        total_distance_km += d_hotel
        day_schedule.append({
            "time": "16:30 - 18:00",
            "category": "🛌 Khung Nghỉ Ngơi Chiều",
            "place": selected_hotel,
            "cost_vnd": 0,
            "distance_km": d_hotel,
            "note": "Trở về chỗ nghỉ ngơi, tắm rửa chuẩn bị cho buổi tối."
        })
        prev_loc = (selected_hotel["lat"], selected_hotel["lng"])

        # 6. Bữa tối & Dạo đêm
        d = calculate_haversine(prev_loc[0], prev_loc[1], dinner["lat"], dinner["lng"])
        total_distance_km += d
        cost = dinner.get("avg_price", 0) * payload.party_size
        total_estimated_cost += cost
        day_schedule.append({
            "time": "18:30 - 21:00",
            "category": "🌙 Bữa Tối & Phố Đêm",
            "place": dinner,
            "cost_vnd": cost,
            "distance_km": d,
            "note": "Thưởng thức bữa tối và trải nghiệm không khí phố đêm."
        })

        daily_itinerary.append({
            "day_title": f"Ngày {day}",
            "target_vibes": target_vibes,
            "activities": day_schedule
        })

    all_places_sorted = sorted(all_places, key=lambda x: x.get("rating", 0), reverse=True)

    return {
        "status": "success",
        "summary": {
            "destination": payload.destination,
            "party_size": payload.party_size,
            "days": payload.days,
            "user_budget_k_vnd": payload.budget_k_vnd,
            "user_budget_vnd": total_budget_vnd,
            "total_estimated_cost_vnd": total_estimated_cost,
            "total_estimated_cost_k_vnd": round(total_estimated_cost / 1000, 1),
            "budget_remaining_vnd": total_budget_vnd - total_estimated_cost,
            "total_distance_km": round(total_distance_km, 1),
            "accommodation": selected_hotel,
            "hotel_cost_vnd": actual_hotel_cost
        },
        "recommended_candidates": all_places_sorted[:15],
        "daily_itinerary": daily_itinerary
    }

# ĐỔI SANG PORT 8001 ĐỂ TRÁNH TRÙNG CỔNG 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)