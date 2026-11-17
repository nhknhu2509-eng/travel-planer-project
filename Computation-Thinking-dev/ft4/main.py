import os
import json
import csv
from datetime import datetime
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Travel Planner Survey API")

# Cấu hình CORS để Frontend gọi được API từ trình duyệt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = "data"
QUESTIONS_FILE = "questions.json"
SURVEY_JSON_FILE = os.path.join(DATA_DIR, "survey_responses.json")
SURVEY_CSV_FILE = os.path.join(DATA_DIR, "survey_responses.csv")

os.makedirs(DATA_DIR, exist_ok=True)

# Schema dữ liệu nhận từ Client
class SurveySubmitPayload(BaseModel):
    user_id: Optional[str] = "ANONYMOUS"
    answers: Dict[str, int]  # Ví dụ: {"Q1": 4, "Q2": 5, ...}
    comment: Optional[str] = ""

def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        raise HTTPException(status_code=500, detail="Không tìm thấy file questions.json!")
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/api/questions")
def get_questions():
    """Lấy danh sách câu hỏi khảo sát"""
    return load_questions()

@app.post("/api/survey/submit")
def submit_survey(payload: SurveySubmitPayload):
    """Nhận kết quả khảo sát và ghi vào file JSON & CSV"""
    questions = load_questions()
    q_map = {q["id"]: q for q in questions}

    if len(payload.answers) < len(questions):
        raise HTTPException(status_code=400, detail="Vui lòng trả lời đầy đủ tất cả câu hỏi!")

    survey_id = f"SRV_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    timestamp = datetime.now().isoformat()
    
    formatted_responses = []
    total_score = 0

    for q_id, score in payload.answers.items():
        if score < 1 or score > 5:
            raise HTTPException(status_code=400, detail=f"Điểm số của {q_id} phải từ 1 đến 5")
        
        q_info = q_map.get(q_id, {})
        formatted_responses.append({
            "question_id": q_id,
            "tag": q_info.get("tag", "UNKNOWN"),
            "group": q_info.get("group", ""),
            "score": score
        })
        total_score += score

    avg_score = round(total_score / len(formatted_responses), 2)

    survey_entry = {
        "survey_id": survey_id,
        "user_id": payload.user_id,
        "timestamp": timestamp,
        "average_score": avg_score,
        "comment": payload.comment,
        "responses": formatted_responses
    }

    # 1. Ghi vào file JSON (Append mode)
    json_data = []
    if os.path.exists(SURVEY_JSON_FILE):
        try:
            with open(SURVEY_JSON_FILE, "r", encoding="utf-8") as f:
                json_data = json.load(f)
        except Exception:
            json_data = []
    
    json_data.append(survey_entry)
    with open(SURVEY_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    # 2. Ghi vào file CSV (Append mode)
    file_exists = os.path.exists(SURVEY_CSV_FILE)
    with open(SURVEY_CSV_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if not file_exists:
            # Ghi Header
            header = ["Survey_ID", "User_ID", "Timestamp", "Average_Score", "Comment"]
            for q in questions:
                header.append(f"{q['id']}_{q['tag']}")
            writer.writerow(header)

        # Ghi Dữ liệu dòng mới
        row = [survey_id, payload.user_id, timestamp, avg_score, payload.comment]
        for q in questions:
            row.append(payload.answers.get(q["id"], ""))
        writer.writerow(row)

    return {
        "status": "success",
        "message": "Đã lưu kết quả khảo sát thành công!",
        "survey_id": survey_id,
        "average_score": avg_score
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)