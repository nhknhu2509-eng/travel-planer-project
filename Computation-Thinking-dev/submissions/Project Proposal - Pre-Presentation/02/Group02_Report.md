# PROJECT PROPOSAL: ENGINEERING A SMART VIRTUAL ASSISTANT
**Course:** CSC10014 / Computational Thinking / 2026  
**Group ID:** Group 02  
**Domain:** Travel Planner Assistant

## TEAM MEMBERS
| No. | Full Name | Student ID | Role in Project |
| :---: | :--- | :---: | :--- |
| 1 | Từ Nguyễn Thuận Thiên | 25127146 | Developer & Data/API Handler |
| 2 | Nguyễn Huỳnh Khánh Như | 25127222 | Team leader & Presenter |
| 3 | Nguyễn Thị Hoàng Châu | 25127022 | Front-end |
| 4 | Nguyễn Bạch Thành Nhân | 25127111 | QA/Tester & Documentation |
| 5 | Nguyễn Bình An | 23127149 | Developer & Logic Implementer |

---

## TABLE OF CONTENTS
* [1. THE ILL-DEFINED PROBLEM](#1-the-ill-defined-problem)
* [2. THE WELL-DEFINED PROBLEM](#2-the-well-defined-problem)
* [3. AN INITIAL VERSION OF THE FOUR PILLARS](#3-an-initial-version-of-the-four-pillars)
  * [3.1. Decomposition](#31-decomposition)
  * [3.2. Pattern Recognition](#32-pattern-recognition)
  * [3.3. Abstraction](#33-abstraction)
  * [3.4. Algorithm Design](#34-algorithm-design)
* [4. SEVERAL SOLUTIONS AND DIRECTIONS EXPLORED](#4-several-solutions-and-directions-explored)
  * [4.1. Exploration of Approaches for Sub-Problems](#41-exploration-of-approaches-for-sub-problems)
  * [4.2. Selected Overall Solution](#42-selected-overall-solution)
  * [4.3. Implementation Roadmap: Dataset and Algorithm Directions](#43-implementation-roadmap-dataset-and-algorithm-directions)

---

## 1. THE ILL-DEFINED PROBLEM

Nowadays, when planning a trip, users often have to search for and compile information from multiple sources, such as Google Maps, transportation booking websites, hotel booking platforms, destination reviews, and weather forecasts. This process leads to several problems: 

**Problem 1: Difficulty Finding Destinations That Match Personal Preferences** 

Users may find numerous tourist destinations but struggle to determine which ones best suit their preferences, group size, travel duration, and trip objectives. For example, people who enjoy adventure and exploration have different travel needs from those who prefer relaxation or family-friendly activities. 

**Problem 2: Difficulty Managing the Travel Budget** 

Transportation, accommodation, food, and sightseeing expenses are often researched separately. Users may find individual services at reasonable prices, but the total cost of the trip can still exceed their budget. 

**Problem 3: Poorly Connected Itineraries That Waste Time and Money** 

Tourist attractions, restaurants, and accommodations may be located far from one another. Without proper planning, users may have to travel back and forth frequently, resulting in additional expenses and insufficient time to fully enjoy their experiences. 

**Problem 4: Insufficient Preparation for Actual Conditions at the Destination** 

Users may not be familiar with the weather, terrain, or specific characteristics of their intended destinations. For instance, watching clouds form in the early morning requires appropriate clothing for low temperatures, while hiking in forests requires consideration of insects, terrain conditions, and essential equipment. 

**Problem 5: Difficulty Evaluating and Choosing Between Different Travel Options** 

Users often have to compare multiple routes, transportation methods, hotels, and activities on their own. A cheaper option may require more travel time, while an itinerary covering many destinations may not be suitable for those who prefer a relaxing trip. 

**Problem 6: Lack of Transparency and Personalization in Travel Recommendations** 

Existing lists of destinations and pre-designed itineraries often fail to explain why they are suitable for particular users. As a result, users may find it difficult to determine whether a recommendation genuinely meets their requirements or simply features popular tourist destinations. 


---

## 2. THE WELL-DEFINED PROBLEM
               
Based on these problems, our team proposes developing a personalized virtual travel assistant website to support users in planning their trips. Users can provide information about their desired destination, departure location, travel dates, group size, budget, preferences, and other specific requirements. 

The system will analyze the input data and retrieve relevant travel information from multiple sources. It will then generate several itinerary options, compare their advantages and disadvantages, and explain how well each option satisfies the user's requirements. This approach aims to help users make informed travel decisions and create itineraries that are personalized, practical, and aligned with their budgets and preferences. 


---

## 3. AN INITIAL VERSION OF THE FOUR PILLARS

### 3.1. Decomposition
To build an effective personalized travel planning assistant, our team decomposes the complex travel planning system into five interconnected, manageable sub-problems (modules):

1. **User Profile & Input Parsing Module:**
   * Extracts essential input parameters from user queries: destination, departure location, duration, party size, total budget, companion type, accommodation type, and vibe preferences.
   * Validates input feasibility (e.g., detecting unrealistic budgets like 100,000 VND for 7 days) and prompts for corrections if necessary.

2. **Destination & POI Recommendation Module:**
   * **Vibe-based Recommendation:** When the destination is not specified, matches user vibe preferences against destination profiles to recommend top candidate cities.
   * **POI Filtering & Ranking:** When the destination is established, filters candidate Points of Interest (POIs) based on party composition (solo, couple, friends, family) and ranks them using preference suitability scores.

3. **Budget Allocation & Expense Control Module:**
   * Categorizes the total budget into dedicated allowances: transportation, accommodation, food & dining, sightseeing tickets, and contingency funds.
   * Tracks accumulated expenses during itinerary generation to ensure total projected costs remain strictly within the user's budget ceiling.

4. **Geographical Clustering & Itinerary Scheduling Module:**
   * Groups POIs by geographical area to minimize transit time and avoid back-and-forth travel.
   * Sequences daily activities considering opening/closing hours, expected visit durations, and reasonable resting/dining windows.

5. **Contextual Advisory & Risk Warning Module:**
   * Assesses weather forecasts and terrain characteristics for the destination.
   * Generates tailored packing checklists (e.g., warm clothes for morning cloud-hunting) and suggests dynamic backup alternatives when unfavorable weather occurs.

---

### 3.2. Pattern Recognition
During the analysis of the travel planning domain, our team identified several recurring patterns that map directly to standard computational problem models:

1. **Preference & Vibe Alignment Pattern (Tag Matching / Set Intersection):**
   * *Observation:* Both users and travel destinations can be described using descriptive categorical tags (e.g., `['Cool', 'Natural', 'Trending', 'Adventure']`).
   * *Computational Pattern:* Finding matching destinations or POIs follows the pattern of computing set intersections or similarity coefficients between the user's vibe vector and the destination's tag vector.

2. **Budget Optimization Pattern (Knapsack Problem):**
   * *Observation:* Users want to maximize experience value across attractions, accommodations, and activities while remaining under a fixed financial threshold ($B_{max}$).
   * *Computational Pattern:* This mirrors the classic **0/1 Knapsack Problem**, where each POI/service has an associated cost (weight) and preference score (value), and the algorithm aims to maximize total satisfaction without exceeding total budget capacity.

3. **Route Sequencing Pattern (Traveling Salesperson Problem with Time Windows - TSPTW):**
   * *Observation:* Visiting multiple attractions in a day requires finding an efficient route that minimizes travel distance while ensuring arrival occurs within each venue's operating hours.
   * *Computational Pattern:* This corresponds to the **Traveling Salesperson Problem with Time Windows (TSPTW)**, solvable using nearest-neighbor heuristics combined with time-slot feasibility checks.

4. **Spatial Locality Pattern (Geographic Clustering):**
   * *Observation:* Tourist spots in a region naturally form spatial clusters (e.g., Da Lat city center vs. Tuyen Lam lake area vs. Cau Dat tea hill).
   * *Computational Pattern:* Grouping destinations by geographic proximity before daily assignment maps to spatial clustering patterns (similar to K-Means or grid-based partitioning), preventing redundant cross-city transit.

5. **Adaptive Contingency Pattern (Rule-Based Fallback):**
   * *Observation:* External disruptions (e.g., sudden heavy rain during cloud-hunting or an attraction closure) require real-time plan adjustments.
   * *Computational Pattern:* This follows a deterministic condition-action rule pattern: `IF condition (e.g., weather == "heavy_rain") THEN trigger alternative_action (replace outdoor POI with indoor café/museum)`.

### 3.3. Abstraction
Extract essential entities and parameters from user inputs and map them to structured computational models:

**A. User Profile & Query Abstraction**
1. **Destination** (`string`): Target city or region (e.g., "Da Lat") or `NULL` if unspecified.
2. **Budget** (`double`): Maximum spending threshold for the trip ($B_{max}$).
3. **Duration** (`int`): Total number of travel days ($D$).
4. **Vibe Preferences** (`list of strings`): Desired travel atmosphere and themes (e.g., `['Cool', 'Natural', 'Trending', 'Adventure']`).
5. **Party Composition** (`string`): Traveling group type (e.g., `Solo`, `Couple`, `Friends`, `Family`).
6. **Accommodation Preference** (`string`): Preferred lodging style (e.g., `Homestay`, `Hotel`, `Resort`).

**B. Point of Interest (POI) & Destination Abstraction**
1. **POI Name** (`string`): Official name of the destination or attraction (e.g., "Langbiang Mountain").
2. **Category & Vibe Tags** (`list of strings`): Descriptive features used for preference alignment.
3. **Average Cost** (`double`): Estimated expenditure per person (entry tickets, dining, or accommodation rates).
4. **Geographical Location** (`coordinates` / `string`): Latitude, longitude, or address for distance calculation.
5. **Operating Hours** (`time range`): Opening and closing windows for scheduling feasibility.
6. **Average Visit Duration** (`double`): Estimated time required to visit (e.g., 1.5 to 2.0 hours).

### 3.4. Algorithm Design

**Scenario 1: Destination-Specified Planning Workflow**
* **Step 1 (Input Acquisition):** Collect user query parameters, including destination, total budget, duration, party composition, and accommodation preferences.
* **Step 2 (Input Validation & Feasibility Check):** Validate parameters for anomalies or unrealistic constraints (e.g., detecting unrealistic budgets such as 100,000 VND for a 7-day trip) and prompt user for revisions if needed.
* **Step 3 (Constraint Filtering & Scoring):** Filter candidate POIs within the target destination against mandatory constraints (budget ceiling, party fit) and score remaining candidates by preference alignment.
* **Step 4 (Spatial Clustering & Daily Scheduling):** Cluster POIs geographically by district/area, sequence visits using shortest-path heuristics (TSPTW), and verify time-window feasibility.
* **Step 5 (Supplemental Recommendations):** Suggest nearby culinary spots and backup indoor attractions during evening hours or travel downtime.

**Scenario 2: Vibe-Based Discovery Workflow (Unspecified Destination)**
* **Step 1 (Preference Elicitation):** Prompt user for desired trip vibes (e.g., chill, nature-oriented, vibrant, wellness).
* **Step 2 (Tag Similarity Matching):** Compute set similarity scores between user vibe tags and candidate destination characteristic profiles.
* **Step 3 (Candidate Presentation):** Present the top 5 recommended destinations with estimated budget ranges and summary highlights.
* **Step 4 (Workflow Transition):** Once the user selects a preferred destination, seamlessly transition to **Scenario 1** to synthesize the complete itinerary.


---

## 4. SEVERAL SOLUTIONS AND DIRECTIONS EXPLORED

The key point is that each problem does not necessarily have only one solution. The virtual assistant should consider different approaches depending on the situation and then select the most suitable solution based on the user's needs. 

### 4.1. Exploration of Approaches for Sub-Problems

#### Problem 1: Difficulty Finding Destinations That Match Personal Preferences

**Example input:** The user wants to visit Da Lat for 3 days and 2 nights with a group of 4 people. They enjoy nature and experiential activities but prefer to avoid overcrowded places. 

|**Solution**|**Approach**|**Suitability**|
|---|---|---|
|A. Filter by mandatory<br>constraints|Eliminate destinations that do not meet<br>requirements regarding time, distance, or<br>accessibility.|When the user has specific<br>requirements that cannot<br>be violated.|
|B. Score destinations<br>based on preferences|Assign scores to destinations according to<br>their suitability for nature, experiential<br>activities, crowd levels, and other<br>preferences.|When multiple destinations<br>satisfy the mandatory<br>constraints.|
|C. Recommend a<br>combination of<br>activity types|Combine cloud hunting, nature sightseeing,<br>local experiences, and relaxation.|When the user wants a<br>diverse travel experience.|
|D. Suggest alternative<br>destinations|If the preferred destination is unsuitable due<br>to weather conditions or excessive travel<br>distance, find similar alternatives.|When the initial option is<br>not feasible.|



**Optimal solution:** Combine A + B + D. First, eliminate destinations that do not meet mandatory requirements. Then, rank the remaining destinations based on the user's preferences and prepare alternative options when necessary. 

#### Problem 2: Difficulty Managing the Total Travel Budget

|**Solution**|**Approach**|**Trade-offs**|
|---|---|---|
|A. Choose the<br>cheapest options|Prioritize low-cost transportation,<br>accommodation, and activities.|Saves money but may reduce comfort.|
|B. Allocate the budget<br>by category|Divide the budget among transportation,<br>accommodation, food, sightseeing, and<br>contingency expenses.|Maintains an overall balance<br>and prevents overspending in<br>one category.|
|C. Optimize spending<br>based on experience<br>value|Preserve activities the user enjoys while<br>reducing costs in less important categories.|Provides a more suitable<br>experience but requires clear<br>priorities.|
|D. Create multiple<br>budget scenarios|Offer budget-friendly, balanced, and<br>comfort-oriented itineraries for<br>comparison.|Provides more choices but<br>requires calculations for<br>multiple alternatives.|



**Optimal solution:** Combine B + C, while using D when the user has not clearly defined their priorities. The system must treat the maximum budget as a constraint when evaluating options rather than simply selecting individual services with low prices. 

For example, if the user particularly enjoys cloud hunting but does not consider luxury accommodation essential, the system should prioritize keeping the cloud-hunting experience while finding affordable accommodation. 

If no option satisfies all requirements within the budget, the system must clearly inform the user and suggest possible adjustments for them to choose from, rather than exceeding the budget without permission. 

#### Problem 3: Poorly Connected Itineraries That Waste Time and Money

**Example:** The user wants to visit six destinations, eat at local restaurants, and have sufficient time to rest over two days. 

|**Solution**|**Approach**|**Suitability**|
|---|---|---|
|A. Arrange destinations by proximity|Prioritize the next destination that is closest to the current location.|When minimizing travel distance is important.|
|B. Group destinations by area|Divide attractions into geographical<br>clusters and assign them to different<br>days.|When destinations are spread across several areas.|
|C. Arrange activities according to operating<br>hours|Consider opening hours, visit durations, and suitable time slots.|When certain destinations are only available during specific<br>hours.|
|D. Balance activities and<br>relaxation|Limit the number of activities per day<br>and allocate sufficient time for meals<br>and rest.|When the user does not want<br>an overly packed itinerary.|



**Optimal solution:** Combine B + C + D, then use A to determine an efficient travel order within each area. The system should not simply select the nearest destination, as this could result in conflicts with opening hours or repeated trips to the same area. Effective optimization must consider location, time, and user preferences simultaneously. 

#### Problem 4: Insufficient Preparation for Actual Conditions at the Destination

**Example:** The user plans to go cloud hunting early in the morning or visit a forested area. 

|**Solution**|**Approach**|**Suitability**|
|---|---|---|
|A. Provide recommendations<br>based on destination<br>characteristics|Use information about terrain, activities,<br>and typical conditions to suggest<br>necessary items.|When basic<br>preparation is needed.|
|B. Provide recommendations<br>based on weather forecasts|Adjust clothing recommendations,<br>itineraries, and activities according to the<br>forecast for the travel dates.|When the trip depends<br>heavily on weather<br>conditions.|
|C. Provide risk-based warnings|Warn users about heavy rain, slippery<br>roads, difficult terrain, or potentially<br>unsafe activities.|When unfavorable<br>conditions may occur.|
|D. Suggest alternative<br>activities|Replace outdoor activities with indoor<br>alternatives when the weather is<br>unsuitable.|When the original plan<br>may not be feasible.|



**Optimal solution:** Combine A + B + C + D. The system should not only provide a packing checklist but also adjust the plan when actual conditions change. 

For example, if rain is forecast during the planned cloud-hunting period, the system should explain the potential impact, recommend checking the forecast closer to the departure date, and suggest alternative activities. It should not guarantee that users will see clouds simply because a destination is well known for this activity. 

#### Problem 5: Difficulty Comparing Different Transportation, Accommodation, and Dining Options

**Example:** The user is traveling from Ho Chi Minh City to Da Lat and is deciding between taking a coach and using a private vehicle. 

|**Solution**|**Approach**|**Priority**|
|---|---|---|
|A. Optimize for cost|Compare the total cost for the entire group.|Users with limited budgets.|
|B. Optimize for time|Compare travel time and waiting time.|Users with limited vacation time.|
|C. Optimize for comfort|Consider rest requirements, group size, luggage, and driving ability.|Families or groups seeking convenient transportation.|
|D. Optimize for flexibility|Consider the ability to change destinations, departure times, and routes independently.|Users who enjoy exploring multiple places.|

**Optimal solution:** The system should not apply a single criterion to every user. Instead, it should assign scores based on the priority weights provided by the user. 

For example, if the user prioritizes saving money, cost should receive a higher weight. If the user is traveling with elderly people, comfort and sufficient rest time may be more important. 

For the same destination, the system can provide two or three alternative options, clearly presenting estimated costs, travel times, and trade-offs so that users can make informed decisions. 

#### Problem 6: Lack of Transparency and Personalization in Recommendations

**Example:** The system recommends a restaurant and a tourist attraction. 

|**Solution**|**Approach**|**Priority**|
|---|---|---|
|A. Explain recommendations based on individual requirements|Clarify how each destination matches the user's preferences,<br> budget, or location requirements.|Helps users understand why<br>a recommendation was made.|
|B. Provide information<br>sources|Attach sources for prices, maps,<br>weather forecasts, and destination<br>information.|Allows users to verify the<br>accuracy of the information.|
|C. Identify unmet<br>requirements|Clearly explain which requirements a<br>destination satisfies and where it<br>has limitations.|Prevents exaggerated claims<br>and unrealistic expectations.|
|D. Allow feedback and<br>adjustments|Let users request cheaper options,<br>less walking, or alternative restaurants.|Makes the itinerary<br>increasingly suitable for the user's needs.|

**Optimal solution:** Combine all four approaches. Each recommendation should identify the relevant user requirements, explain the reasons for the selection, provide supporting information sources, and disclose any limitations. When the user changes their requirements, the system should recalculate the affected parts of the itinerary. 

### 4.2. Selected Overall Solution

Based on the analysis above, our team selects an integrated solution that combines constraint filtering, suitability scoring, itinerary optimization, budget management, and explainable recommendations. 

**Proposed workflow:** 

1. **Collect user information:** Destination, travel dates, group size, budget, preferences, and special requirements. 

2. **Analyze and classify requirements:** Distinguish mandatory constraints from preference-based criteria. 

3. **Collect and evaluate data:** Gather information about destinations, service prices, maps, weather forecasts, and operating hours. 

4. **Generate and compare alternatives:** Create budget-friendly, balanced, and experience-oriented itineraries. 

5. **Check feasibility:** Evaluate the budget, routes, available time, and actual conditions. 

6. **Present results and explanations:** Provide the itinerary, estimated costs, reasons for recommendations, reference sources, and important notes. 

The virtual assistant should be capable of answering the following questions: 

- Which destinations best match the group's needs? 

- What transportation options provide the best balance between cost and time? 

- How should the itinerary be arranged to minimize unnecessary travel? 

- What should be changed if the budget is exceeded or the weather is unfavorable? 

- Why does the system select one option over the alternatives? 

---

### 4.3. Implementation Roadmap: Dataset and Algorithm Directions

#### 4.3.1. System Objective
The primary objective of this phase is to establish the technical foundation for the virtual assistant by formalizing data collection standards (Tourism Dataset) and designing the computational pipeline (Algorithms) required to transform raw user queries into feasible, optimized itineraries.

#### 4.3.2. Dataset Direction
The system avoids storing unstructured descriptive text, focusing strictly on structured numerical and categorical parameters essential for algorithmic computation.

**A. Proposed Data Sources**
- **Geographical & Spatial Data:** Google Maps Platform API and OpenStreetMap (OSM) for geocoordinates, road network distances, and transit times.
- **Pricing & Feedback Data:** Targeted data extraction from travel platforms (e.g., TripAdvisor, Traveloka) for admission fees, average meal costs, and rating scores.

**B. Standardized POI Data Schema**

Each destination in the database is standardized into 6 core technical attributes:
1. **POI Name & Identifier:** Unique identifier and official destination name.
2. **Coordinates (`latitude`, `longitude`):** Precise spatial coordinates for Euclidean and distance-matrix calculations.
3. **Estimated Cost:** Average expenditure per visitor, used as a constraint in budget optimization.
4. **Category & Vibe Tags:** Standardized classification tags (e.g., `Nature`, `Cultural`, `Adventure`, `Relaxing`) used for preference similarity matching.
5. **Operating Hours:** Opening and closing time windows to guarantee schedule feasibility.
6. **Average Visit Duration:** Recommended time allotment (e.g., 1.5 to 2.0 hours) for itinerary scheduling.

#### 4.3.3. Algorithms Direction
The processing workflow from input ingestion to final itinerary synthesis is organized into a two-stage computational pipeline:

**Stage 1: Multi-Criteria Filtering & Scoring Algorithm**
- **Hard Constraint Filtering:** Instantly prunes destinations that fall outside the target geographic boundary or exceed the maximum single-activity budget threshold.
- **Preference Scoring:** Evaluates set similarity (e.g., Jaccard index / tag matching) between user vibe vectors and POI tag vectors to rank candidate attractions by relevance.

**Stage 2: Spatial Clustering & Route Scheduling Algorithm**
- **Spatial Partitioning:** Groups candidate POIs into regional daily clusters to eliminate redundant cross-city transit.
- **Routing Optimization:** Solves a localized Traveling Salesperson Problem with Time Windows (TSPTW) using greedy nearest-neighbor heuristics, ensuring timely arrival within operating hours and reasonable rest intervals.

#### 4.3.4. Next Steps (Phase 2)
1. **Mock Dataset Construction:** Curate and validate a localized test dataset of 30–50 destinations for a representative pilot city (e.g., Da Lat).
2. **Algorithmic Flowcharts & Pseudocode:** Formulate detailed architectural flowcharts and formal pseudocode for the multi-stage filtering and route-scheduling pipeline.
3. **Feasibility Testing:** Run simulation scenarios to evaluate budget adherence, transit efficiency, and schedule practicality.
