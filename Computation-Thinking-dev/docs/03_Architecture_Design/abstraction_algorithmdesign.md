# ARCHITECTURE DESIGN: ABSTRACTION & ALGORITHM DESIGN
**Course:** CSC10014 / Computational Thinking / 2026  
**Group ID:** Group 02  
**Domain:** Travel Planner Assistant  
**Author:** Từ Nguyễn Thuận Thiên & Nguyễn Bình An  

---

## 1. ABSTRACTION

Extract essential entities and parameters from user inputs and map them to structured computational models:

### A. User Profile & Query Abstraction
1. **Destination** (`string`): Target city or region (e.g., "Da Lat") or `NULL` if unspecified.
2. **Budget** (`double`): Maximum spending threshold for the trip ($B_{max}$).
3. **Duration** (`int`): Total number of travel days ($D$).
4. **Vibe Preferences** (`list of strings`): Desired travel atmosphere and themes (e.g., `['Cool', 'Natural', 'Trending', 'Adventure']`).
5. **Party Composition** (`string`): Traveling group type (e.g., `Solo`, `Couple`, `Friends`, `Family`).
6. **Accommodation Preference** (`string`): Preferred lodging style (e.g., `Homestay`, `Hotel`, `Resort`).

### B. Point of Interest (POI) & Destination Abstraction
1. **POI Name** (`string`): Official name of the destination or attraction (e.g., "Langbiang Mountain").
2. **Category & Vibe Tags** (`list of strings`): Descriptive features used for preference alignment.
3. **Average Cost** (`double`): Estimated expenditure per person (entry tickets, dining, or accommodation rates).
4. **Geographical Location** (`coordinates` / `string`): Latitude, longitude, or address for distance calculation.
5. **Operating Hours** (`time range`): Opening and closing windows for scheduling feasibility.
6. **Average Visit Duration** (`double`): Estimated time required to visit (e.g., 1.5 to 2.0 hours).

---

## 2. ALGORITHM DESIGN

### Scenario 1: Destination-Specified Planning Workflow
* **Step 1 (Input Acquisition):** Collect user query parameters, including destination, total budget, duration, party composition, and accommodation preferences.
* **Step 2 (Input Validation & Feasibility Check):** Validate parameters for anomalies or unrealistic constraints (e.g., detecting unrealistic budgets such as 100,000 VND for a 7-day trip) and prompt user for revisions if needed.
* **Step 3 (Constraint Filtering & Scoring):** Filter candidate POIs within the target destination against mandatory constraints (budget ceiling, party fit) and score remaining candidates by preference alignment.
* **Step 4 (Spatial Clustering & Daily Scheduling):** Cluster POIs geographically by district/area, sequence visits using shortest-path heuristics (TSPTW), and verify time-window feasibility.
* **Step 5 (Supplemental Recommendations):** Suggest nearby culinary spots and backup indoor attractions during evening hours or travel downtime.

### Scenario 2: Vibe-Based Discovery Workflow (Unspecified Destination)
* **Step 1 (Preference Elicitation):** Prompt user for desired trip vibes (e.g., chill, nature-oriented, vibrant, wellness).
* **Step 2 (Tag Similarity Matching):** Compute set similarity scores between user vibe tags and candidate destination characteristic profiles.
* **Step 3 (Candidate Presentation):** Present the top 5 recommended destinations with estimated budget ranges and summary highlights.
* **Step 4 (Workflow Transition):** Once the user selects a preferred destination, seamlessly transition to **Scenario 1** to synthesize the complete itinerary.
