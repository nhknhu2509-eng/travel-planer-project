## REPORT PART 3: PREPARE ABOUT DATASET

### 1. Inputs

Applying the 4 pillars of Computational Thinking to our project—specifically in the Decomposition stage—we divide the overall planning problem into two main layers: Direct User Inputs and System Processing. Inside System Processing, the architecture further branches into External Data Collection and Algorithm Optimization.

Because algorithms rely entirely on accurate data representation, the inputs to our function consist of data collected directly from user preferences as well as structured dataset fields retrieved from external/system sources.
#### a) Directed input from user:
The direct input is captured from the user interface as a structured payload (represented as a UserRequest object). It includes basic travel constraints, budget limits, duration, and categorical preference filters.

Destination (string or NULL): Target city for the trip (e.g., "Đà Lạt" or "Nha Trang"). If set to NULL, the recommendation engine triggers vibe-based city discovery.

Total Budget (double): Total budget limit allocated for the entire trip in VND (e.g., 6000000 VND).

Duration (int): Total duration of the trip in days (e.g., 3 days).

Party Size (int): Total number of travelers participating in the trip (e.g., 2 people).

Vibe & Type Selection Mode (string): Defines whether preference tags are applied globally across the entire itinerary ("global") or tailored day-by-day ("daily").

Preferred Place Types (list<string>): Selected categories of places to include in the itinerary. Options include:

Accommodation, Restaurant, Attraction, Café

Travel Vibes (list<string>): Categorical tags defining the user's preferred travel atmosphere. Available vibes include:

Nature, Chill, Adventure, Romantic, Cultural, View_Hunting, Culinary, Local_Food, Relaxation, Luxury, Budget_Friendly, Photography, Trending, Sightseeing

### Concrete example
Based on the system's user interface, a typical input submitted by a user planning a couple's trip to Đà Lạt is structured as follows:
```{
  "destination": "Đà Lạt",
  "total_budget": 6000000,
  "duration": 3,
  "party_size": 2,
  "selection_mode": "global",
  "preferred_types": [
    "Attraction",
    "Restaurant",
    "Café",
    "Accommodation"
  ],
  "travel_vibes": [
    "Culinary",
    "Local_Food",
    "Sightseeing"
  ]
}
```
### b) External & System Processing Dataset

To match user requests with suitable destinations, optimize cost constraints ($0/1\text{ Knapsack}$), and sequence daily visits ($TSPTW$), the system utilizes a structured POI (Point of Interest) dataset stored as standard JSON records (e.g., places_dalat.json and places_nhatrang.json).

Each POI record contains spatial coordinates, pricing bounds, operating time windows, ratings, and tag classifications:

Basic Info: stt (ID), name (Name of POI), type (Category: Accommodation/Restaurant/Attraction/Café).

Spatial Data: lat & lng (Geographical coordinates used for distance matrix computation & K-Means clustering), new_address & old_address.

Cost & Time Constraints: avg_price (Numerical price in VND used for budget enforcement), open_time & close_time (Operating hours used for TSPTW time windows).

Categorical Matching Data: vibes (List of vibe strings used for Set Intersection / Similarity matching with user inputs).

Metadata & Routing: rating (Score out of 5.0), link (Google Maps URL).

### Concrete example

Below are representative data entries extracted from our active dataset:
```[
  {
    "stt": 2,
    "name": "Tiệm Cà Phê Túi Mơ To",
    "new_address": "Hẻm 31 Sào Nam, Phường 11, Đà Lạt, Lâm Đồng",
    "type": "Café",
    "vibes": ["Chill", "View_Hunting", "Trending", "Photography"],
    "avg_price": 70000,
    "open_time": "07:00",
    "close_time": "21:30",
    "rating": 4.6,
    "lat": 11.9472,
    "lng": 108.4795,
    "link": "https://maps.google.com/?q=Túi+Mơ+To+Đà+Lạt"
  },
  {
    "stt": 1,
    "name": "Tháp Bà Ponagar",
    "new_address": "2 Đường 2 Tháng 4, Vĩnh Phước, Nha Trang, Khánh Hòa",
    "type": "Attraction",
    "vibes": ["Cultural", "Sightseeing"],
    "avg_price": 30000,
    "open_time": "06:00",
    "close_time": "17:30",
    "rating": 4.5,
    "lat": 12.2654,
    "lng": 109.1961,
    "link": "https://maps.google.com/?q=Tháp+Bà+Ponagar+Nha+Trang"
  }
]
```
### 2. Outputs
Based on the input data structures (UserRequest) and the place dataset (POI Dataset), the function processes and returns an output data structure (ItineraryResponse), which includes a detailed itinerary for the entire trip:

Trip Overview (object): Summary information of the trip, including destination city, total duration, total party size, and total estimated cost after optimization.

Daily Itinerary Schedule (list<DayPlan>): A detailed list of schedules divided by day (Day 1, Day 2, Day 3...). Each day includes:

Geographical Cluster ID: The geographical zone/cluster for the day (result from the clustering algorithm).

Ordered List of Activities (list<POI>): A list of tourist spots, dining places, cafes, and accommodations ordered to minimize travel time (respecting operating hours and time windows - TSPTW).

Daily Cost Breakdown: Estimated total cost for that day (tickets, dining, transportation) to enforce budget constraints ($0/1\text{ Knapsack}$).

### Sample output payload
```
{
  "destination": "Đà Lạt",
  "total_duration": 3,
  "estimated_total_cost": 5400000,
  "itinerary_by_days": [
    {
      "day_index": 1,
      "cluster_zone": "Central & East Zone",
      "activities": [
        {
          "time_slot": "08:30 - 11:00",
          "name": "Thung Lũng Tình Yêu Tourist Area",
          "type": "Attraction",
          "estimated_cost": 250000
        },
        {
          "time_slot": "11:30 - 13:00",
          "name": "Bánh Mì Xíu Mại Ri 79",
          "type": "Restaurant",
          "estimated_cost": 35000
        },
        {
          "time_slot": "14:00 - 17:00",
          "name": "Tiệm Cà Phê Túi Mơ To",
          "type": "Café",
          "estimated_cost": 70000
        }
      ]
    }
  ]
}
```
### 3. How it works

This section explains the coordination mechanism between inputs and algorithms to generate results (linking directly to the Decomposition and Pattern Recognition sections):

Step 1: Input Parsing & Validation

The system receives the UserRequest payload from the user interface.

Checks destination constraints: If Destination == NULL, the system uses the Vibes field to recommend a suitable city. If a specific city is provided (e.g., Đà Lạt), it proceeds to data filtering.

Step 2: Preference & Vibe Matching

Based on the user's travel_vibes and preferred_types, the system scans the dataset (places_dalat.json / places_nhatrang.json) to find places with the highest overlapping tag sets (Set Intersection / Similarity Measures).

Step 3: Budget OptimizationApplying the 0/1 Knapsack Problem model, the system selects attractions, dining options, and accommodations to maximize experiential value while keeping cumulative costs within the total budget limit (total_budget $\le B_{max}$).

Step 4: Geographical Clustering & Sequencing

K-Means Clustering / Spatial Locality: Groups selected locations into nearby geographical areas to avoid unnecessary zigzag travel.

TSPTW (Traveling Salesperson Problem with Time Windows): Sequences visits for each day, ensuring arrival times fall within operating windows (open_time - close_time) and minimizing travel time.

Step 5: Output Generation

Compiles all computed data into an ItineraryResponse structure and renders the complete travel schedule visually on the user interface.