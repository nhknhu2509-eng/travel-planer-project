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

- Problem Statement: After clearly defining the core objective—to make an optimal travel plan—we decompose the problem into two main components: ***Direct User Data*** and ***System Processing***.

- ***System Processing*** Breakdown: Inside System Processing, we further divide the logic into two sub-layers:

+ ***Collect External Data***: We gather data from external platforms (e.g., weather forecasts, place characteristics) to support intelligent decision-making.

+ ***Algorithm Optimization***: We apply classic Mathematical Models (0/1 Knapsack, TSPTW, and K-Means Clustering) to process, filter, and sequence the itinerary efficiently.

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

**Example output:**

Based on the user's requirements, the virtual travel assistant recommends the following destinations and activities in Da Lat for a group of four people on a 3-day, 2-night trip.

| **Recommended option** | **Why it is suitable** | **Evaluation criteria** |
|---|---|---|
| A. Nature exploration at Tuyen Lam Lake | Offers opportunities to enjoy natural scenery and spend time outdoors in a relatively peaceful environment. | Natural scenery, outdoor activities, and suitability for relaxation. |
| B. Cloud hunting at Cau Dat | Provides an opportunity to experience Da Lat's highland scenery and enjoy an early-morning outdoor activity. However, cloud visibility depends on actual weather conditions. | Experience value, nature-related preferences, and weather feasibility. |
| C. Exploring local farms and gardens | Allows the group to explore local agricultural activities and enjoy a more experiential trip rather than visiting only popular tourist attractions. | Local experiences, activity diversity, and group suitability. |

**Reasons for selection:**

The system evaluates each option based on the user's stated preferences, including nature, experiential activities, and avoiding overcrowded places. It also considers the 3-day, 2-night duration and the needs of a group of four people.

Destinations and activities that match these preferences receive higher suitability scores. The system should also consider travel distance, estimated costs, opening hours where applicable, and weather conditions before finalizing the itinerary.

These recommendations are preliminary options rather than guaranteed choices. Before generating the final itinerary, the system should verify relevant travel information and compare the alternatives. If an option is expected to be crowded or unsuitable under the forecast conditions, it should suggest a more suitable alternative.

---

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

**Example input:**

The user plans a 3-day, 2-night trip to Da Lat with a group of 4 people. They want to experience cloud hunting but prefer affordable accommodation over luxury hotels. Their total budget is VND 8,000,000 for the entire group.

**Example output:**

Based on the user's budget and preferences, the virtual travel assistant proposes the following estimated budget allocation for the group of four.

| **Expense category** | **Estimated cost (VND)** | **Reason for allocation** |
|---|---:|---|
| Transportation | 1,600,000 | Allocate funds for round-trip transportation between Ho Chi Minh City and Da Lat. |
| Accommodation | 1,600,000 | Choose affordable accommodation for 2 nights instead of luxury hotels. |
| Food and drinks | 2,000,000 | Reserve a reasonable amount for meals and local food experiences. |
| Activities and sightseeing | 1,600,000 | Prioritize cloud hunting and other nature-related activities. |
| Contingency expenses | 800,000 | Reserve funds for unexpected costs during the trip. |
| **Total estimated budget** | **7,600,000** | **Within the maximum budget of VND 8,000,000.** |

**Reasons for selection:**

The system allocates the budget based on three main factors:

- **Total budget constraint:** The estimated total cost must not exceed VND 8,000,000.
- **User preferences:** Cloud hunting is a priority, so the system preserves funds for this experience while reducing accommodation costs.
- **Expense balance:** The system distributes the remaining budget across transportation, meals, activities, and contingency expenses to avoid overspending in one category.

The estimated cost is VND 7,600,000, leaving VND 400,000 below the user's maximum budget. The system should verify actual transportation, accommodation, and activity prices before finalizing the plan.

If the verified costs exceed the budget, the system should suggest adjustments, such as choosing cheaper accommodation or reducing less important expenses, while attempting to preserve the cloud-hunting experience. It should not exceed the user's maximum budget without their agreement.

These figures are illustrative estimates rather than verified current prices.

---

#### Problem 3: Poorly Connected Itineraries That Waste Time and Money

**Example:** The user wants to visit six destinations, eat at local restaurants, and have sufficient time to rest over two days. 

|**Solution**|**Approach**|**Suitability**|
|---|---|---|
|A. Arrange destinations by proximity|Prioritize the next destination that is closest to the current location.|When minimizing travel distance is important.|
|B. Group destinations by area|Divide attractions into geographical<br>clusters and assign them to different<br>days.|When destinations are spread across several areas.|
|C. Arrange activities according to operating<br>hours|Consider opening hours, visit durations, and suitable time slots.|When certain destinations are only available during specific<br>hours.|
|D. Balance activities and<br>relaxation|Limit the number of activities per day<br>and allocate sufficient time for meals<br>and rest.|When the user does not want<br>an overly packed itinerary.|



**Optimal solution:** Combine B + C + D, then use A to determine an efficient travel order within each area. The system should not simply select the nearest destination, as this could result in conflicts with opening hours or repeated trips to the same area. Effective optimization must consider location, time, and user preferences simultaneously. 

**Example output:**

Based on the user's requirements, the virtual travel assistant generates the following two-day itinerary for six destinations. The destinations are grouped by geographical area, their operating hours are considered, and sufficient time is allocated for meals and rest.

| **Day** | **Time** | **Activity** | **Reason for arrangement** |
|---|---|---|---|
| Day 1 | 8:00–9:00 | Have breakfast at a local restaurant. | Start the day comfortably and include a local dining experience. |
| Day 1 | 9:00–11:00 | Visit Destinations A and B in the same area. | Group nearby destinations to reduce travel time and unnecessary transportation costs. |
| Day 1 | 11:00–13:00 | Have lunch and take a break. | Allow sufficient time for meals and rest. |
| Day 1 | 13:00–15:00 | Visit Destination C in the same area. | Continue exploring the area without returning to a previously visited location. |
| Day 1 | 15:00–17:00 | Return to the accommodation and rest. | Prevent the itinerary from becoming too demanding. |
| Day 1 | 18:00–19:30 | Have dinner at a local restaurant. | Include another local food experience while keeping the evening relaxed. |
| Day 2 | 8:00–9:00 | Have breakfast at a local restaurant. | Prepare for the second day of activities. |
| Day 2 | 9:00–11:00 | Visit Destinations D and E in another area. | Group destinations by location to minimize backtracking. |
| Day 2 | 11:00–13:00 | Have lunch and take a break. | Maintain a balance between sightseeing and relaxation. |
| Day 2 | 13:00–15:00 | Visit Destination F. | Complete the remaining destination without overcrowding the schedule. |
| Day 2 | 15:00 onward | Return to the accommodation or prepare for departure. | Keep the remaining time flexible for rest and travel arrangements. |

**Reasons for selection:**

The itinerary is generated based on four main factors:

- **Geographical grouping:** Destinations A, B, and C are scheduled on Day 1, while Destinations D, E, and F are scheduled on Day 2, assuming each group is located in the same area. This reduces unnecessary travel between distant areas.
- **Operating hours:** The system checks the opening hours of each destination and adjusts the visiting order to ensure that the planned activities are feasible.
- **Travel time and distance:** Within each geographical area, the system prioritizes an efficient visiting order to minimize travel time and avoid repeatedly visiting the same area.
- **Activity and rest balance:** Meals and rest periods are included to prevent an overly packed schedule and provide a more comfortable travel experience.

This approach combines geographical grouping, operating-hour constraints, and activity balancing. The nearest destination is not always selected first because its opening hours or position in the overall route may make another visiting order more efficient.

The itinerary is an illustrative example. Actual destination locations, operating hours, and travel times must be verified before the final schedule is generated.

---

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

**Example output:**

Based on the user's plan to go cloud hunting early in the morning or visit a forested area, the virtual travel assistant provides the following preparation recommendations.

**A. Preparation based on destination characteristics**

- **Cloud hunting:** Bring a warm jacket, comfortable shoes, and suitable clothing for early-morning outdoor conditions.
- **Forest exploration:** Wear appropriate walking shoes, bring drinking water, insect repellent, and a small first-aid kit.

**B. Recommendations based on weather forecasts**

If rain is forecast during the planned cloud-hunting period, the system recommends checking the updated forecast closer to the departure date and preparing suitable rainwear. Cloud visibility may be reduced under unfavorable weather conditions.

**C. Risk-based warnings**

If heavy rain or slippery paths are expected, the system warns the user about potentially unsafe outdoor conditions. It recommends checking local weather updates and trail conditions before proceeding. If conditions are considered unsafe, the outdoor activity should be postponed or avoided.

**D. Alternative activities**

If the weather is unsuitable for cloud hunting or forest exploration, the system suggests alternative activities, such as visiting a local museum, exploring indoor attractions, or enjoying local cafés.

**Reasons for selection:**

The system generates these recommendations based on four factors:

- **Destination characteristics:** The terrain and planned activities determine the essential items the user should prepare.
- **Weather conditions:** The forecast helps the system adjust clothing recommendations and determine whether outdoor activities remain feasible.
- **Potential risks:** Heavy rain, slippery paths, and difficult terrain may affect user safety and require changes to the original plan.
- **Activity feasibility:** Alternative indoor activities help maintain a useful travel itinerary when outdoor plans cannot be carried out safely.

The system should distinguish between general preparation advice and recommendations based on the latest available weather information. Since weather forecasts can change, users should check updated conditions closer to their departure date. The system should not guarantee that cloud hunting will be successful, as cloud visibility depends on actual weather and environmental conditions.

---

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

**Example output:**

Based on the user's trip from Ho Chi Minh City to Da Lat, the virtual travel assistant compares two transportation options. The final recommendation depends on the user's priorities regarding cost, travel time, comfort, and flexibility.

| **Evaluation criterion** | **Option A: Coach** | **Option B: Private vehicle** |
|---|---|---|
| Estimated total cost | Depends on the number of passengers and ticket prices. | Depends on fuel, tolls, parking, and vehicle-related expenses. |
| Travel time | Depends on the coach schedule, traffic, and waiting time. | Depends on traffic, route choice, and rest stops. |
| Comfort | Passengers do not need to drive and can rest during the journey. | Offers more privacy but requires someone to drive. |
| Flexibility | Departure times and routes depend on the coach operator. | Allows more control over departure times, routes, and stops. |
| Most suitable for | Travelers who prioritize convenience and do not want to drive. | Groups who value flexibility and want to visit multiple places along the way. |

**Reasons for selection:**

The system evaluates the options based on the user's priorities rather than applying the same criteria to every traveler.

- **If cost is the highest priority:** The system compares the total cost for the entire group, including all relevant transportation expenses, and recommends the more economical feasible option.
- **If travel time is the highest priority:** The system compares estimated journey durations, waiting time, and the time needed for rest stops.
- **If comfort is the highest priority:** The system considers the group's size, luggage, need for rest, and whether a suitable driver is available.
- **If flexibility is the highest priority:** The system favors the option that provides greater control over departure times, routes, and stops.

For example, if the user prioritizes saving money and does not need to stop at multiple locations along the way, the coach may be more suitable if its total cost is lower. However, if the group wants to explore several places along the route and has a suitable driver, a private vehicle may be more appropriate.

The system should assign weights to the user's priorities, compare the available options, and explain the trade-offs of each choice. It can then recommend the most suitable option or present both alternatives if neither clearly outperforms the other.

The comparison is illustrative. Actual prices and travel times should be checked for the user's travel dates before a final recommendation is made.

---

#### Problem 6: Lack of Transparency and Personalization in Recommendations

**Example:** The system recommends a restaurant and a tourist attraction. 

|**Solution**|**Approach**|**Priority**|
|---|---|---|
|A. Explain recommendations based on individual requirements|Clarify how each destination matches the user's preferences,<br> budget, or location requirements.|Helps users understand why<br>a recommendation was made.|
|B. Provide information<br>sources|Attach sources for prices, maps,<br>weather forecasts, and destination<br>information.|Allows users to verify the<br>accuracy of the information.|
|C. Identify unmet<br>requirements|Clearly explain which requirements a<br>destination satisfies and where it<br>has limitations.|Prevents exaggerated claims<br>and unrealistic expectations.|
|D. Allow feedback and<br>adjustments|Let users request cheaper options,<br>less walking, or alternative restaurants.|Makes the itinerary<br>increasingly suitable for the user's needs.|

**Optimal solution:** Combine all four approaches. Each recommendation should identify the relevant user requirements, explain the reasons for the selection, provide supporting information sources, and disclose any limitations. When the user changes their requirements, the system should recalculate the affected parts of the itinerary. 

**Example output:**

Based on the user's preferences, budget, and location requirements, the virtual travel assistant recommends a local restaurant and a tourist attraction. Each recommendation includes an explanation, supporting information sources, and potential limitations.

**Recommendation 1: Local Restaurant**

- **Reason for recommendation:** The restaurant matches the user's preference for local food and is located near the planned sightseeing area, helping reduce unnecessary travel.
- **Supporting information:** The system provides the restaurant's location on a map, available menu and price information, customer reviews, and a source link where available.
- **Limitations:** Prices, opening hours, and crowd levels may change. The system should identify any information that has not been verified rather than presenting it as confirmed.
- **Possible adjustment:** If the user considers the restaurant too expensive, the system can search for a more affordable alternative nearby.

**Recommendation 2: Tourist Attraction**

- **Reason for recommendation:** The attraction matches the user's interest in nature and outdoor experiences and can be incorporated into the planned itinerary.
- **Supporting information:** The system provides the attraction's location, relevant visitor information, operating hours where available, and weather information when the activity depends on outdoor conditions.
- **Limitations:** The attraction may involve considerable walking or may be unsuitable under unfavorable weather conditions. The system should disclose these limitations before the user makes a decision.
- **Possible adjustment:** If the user prefers less walking, the system can suggest an alternative with easier access or a shorter walking distance.

**Reasons for selection:**

The system evaluates each recommendation using four principles:

- **Personalized explanations:** Explain how the restaurant or attraction matches the user's stated preferences, budget, and location requirements.
- **Transparent information sources:** Provide links or references so users can verify relevant details, such as prices, locations, operating hours, and weather conditions.
- **Disclosure of limitations:** Identify potential drawbacks and distinguish verified information from estimates or information that may change.
- **User feedback and adjustment:** Allow users to request cheaper options, reduce walking distance, change restaurants, or modify other preferences.

When the user changes a requirement, the system should reassess the affected recommendations and itinerary components while preserving the remaining requirements where possible.

This approach helps users understand not only what the system recommends, but also why it makes each recommendation, what information supports it, and what limitations they should consider.

**User Feedback and Experience Sharing**

After using the travel assistant, users can submit feedback about the recommended destinations, restaurants, accommodations, and itineraries. They can share their experiences, rate how well the recommendations matched their expectations, and report any differences between the information provided by the system and their actual experiences.

This feedback helps future users make more informed decisions by providing real-world perspectives in addition to the system's explanations and information sources. For transparency, the app should distinguish user reviews from verified facts, display feedback fairly, and avoid presenting individual opinions as guaranteed outcomes.

If users report outdated information or unsatisfactory recommendations, the system can use this feedback to review relevant information and improve future recommendations.

**Reason for Selection:** User feedback adds transparency by showing how recommendations have worked for other travelers. Combined with the system's explanations, information sources, and stated limitations, it gives users a clearer basis for deciding whether a recommendation suits their needs.

---

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

### 4.3.2. Dataset Direction: Building the Tourism Database

#### A. Data Sources and Collection

The proposed travel planning assistant requires tourism data collected from multiple sources to support destination recommendation, budget management, and itinerary generation. Following our presentation, the team plans to build the tourism database using two primary sources: Google Maps Platform API and web scraping.

**1. Google Maps Platform API**

The Google Maps Platform API will be considered a primary source for geographic and place-related information. Depending on the selected API and the fields available through it, the system may obtain information such as place names, coordinates, addresses, and place categories.

This information supports the identification of tourist attractions and provides geographic data for itinerary planning. If the scheduling algorithm uses travel time rather than straight-line distance, an appropriate routing service or another documented estimation method will also be required.

**2. Web Scraping**

Web scraping will be explored to collect additional tourism information that may not be available through the selected mapping API. Potential information includes estimated entrance fees, attraction descriptions, category information, and recommended visit durations.

The team will prioritize official attraction websites and reliable tourism sources. Data will only be extracted when permitted by the relevant website terms and access restrictions. If automated extraction is unavailable or inappropriate, the team may collect the information manually from permitted sources.

Because information from different websites may use inconsistent formats or may not be up to date, collected data will be checked before being added to the database. The system will retain source references for important information so that values can be reviewed when necessary.

#### B. AI-Based Data Processing

Raw information collected from APIs and web pages may contain unstructured descriptions, inconsistent formats, and different representations of the same information. As described in our presentation, an AI model is proposed to process this raw information and transform it into structured fields that can be used by the recommendation and itinerary-generation algorithms.

The initial dataset will focus on four core attributes:

1. **Coordinates (latitude and longitude):** Used to identify the geographic location of each attraction and support location-based calculations.
2. **Estimated Cost:** Used to estimate attraction expenses and support budget control.
3. **Category Tags:** Used to classify attractions and match them with users’ preferred travel styles or activities.
4. **Average Visit Duration:** Used to estimate the time needed for each attraction and construct daily schedules.

These four attributes represent the main data fields highlighted in the presentation. The implementation-ready dataset may include additional fields, such as place names, operating hours, and source references, to support data identification and schedule validation.

The AI model will assist with extracting, classifying, and normalizing information from the collected sources. However, AI-generated values will not automatically be treated as verified facts. Important information, particularly costs, coordinates, and operating hours, must be checked against available sources. Missing or uncertain values will be marked for further verification rather than filled with unsupported estimates.

#### C. Dataset Structure

For the initial prototype, each point of interest (POI) will be stored as a structured record. The proposed schema is designed to support the requirements of the project’s recommendation, budget-control, and scheduling algorithms.

| Attribute | Description | Purpose |
|---|---|---|
| POI ID | Unique identifier for each attraction | Identifies each record |
| POI Name | Name of the attraction | Displays and identifies the destination |
| Coordinates | Latitude and longitude | Supports geographic calculations |
| Estimated Cost | Estimated entrance fee or activity cost | Supports budget estimation |
| Cost Basis | Cost per person, ticket, group, or other unit, when known | Prevents inconsistent cost calculations |
| Category Tags | Categories and vibe-related labels | Supports preference matching |
| Operating Hours | Opening and closing times, when available | Supports schedule feasibility |
| Average Visit Duration | Estimated visit time in minutes | Supports daily itinerary generation |
| Source Reference | URL or identifier of the information source | Supports traceability |
| Last Verified | Date when the information was last checked | Supports data freshness monitoring |

The four core attributes from the presentation form the foundation of the dataset, while the additional fields provide the information needed to use and maintain the records more reliably.

#### D. Data Cleaning and Quality Control

Before the dataset is used by the algorithms, the team will apply basic data-quality checks.

- **Completeness:** Identify missing values in fields required for a particular algorithm.
- **Validity:** Check whether coordinates, costs, and visit durations use acceptable formats and values.
- **Consistency:** Standardize cost units, category tags, and time representations.
- **Deduplication:** Identify repeated records referring to the same attraction.
- **Source verification:** Review important information against its recorded source when possible.
- **Freshness:** Record when information was last checked, especially for costs and operating hours that may change over time.

If a value cannot be verified, it will be marked as unknown or estimated, depending on the available evidence. The system should not present uncertain information as confirmed. Records missing essential information may be excluded from specific calculations until the required fields are available.

#### E. Initial Dataset Construction

The team plans to construct an initial dataset of approximately 30–50 points of interest in Da Lat as a manageable test case for the prototype.

The dataset will be stored in a structured format, such as JSON or CSV, so that the recommendation and itinerary-generation modules can process it consistently. The initial records will be used to test preference matching, estimated attraction costs, geographic planning, and daily scheduling.

The team will evaluate whether the collected data are sufficiently complete and consistent for these tasks. The results will help identify missing fields, unreliable values, and areas requiring improvement before expanding the database to additional destinations.

This staged approach allows the team to develop and test the core functionality with a limited dataset before considering larger-scale data collection.
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
