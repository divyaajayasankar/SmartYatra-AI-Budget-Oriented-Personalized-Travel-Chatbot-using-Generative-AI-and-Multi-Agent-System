from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import os
import re

router = APIRouter()

# =====================================================
# LOAD DATASET
# =====================================================

DATASET_PATH = "data/india_tourist_places.csv"

if os.path.exists(DATASET_PATH):
    df = pd.read_csv(DATASET_PATH)
else:
    df = pd.DataFrame()

# =====================================================
# REQUEST MODEL
# =====================================================

class ChatRequest(BaseModel):
    query: str
    persons: int = 1

# =====================================================
# EXTRACT DAYS
# =====================================================

def extract_days(query):

    match = re.search(r'(\d+)\s*day', query.lower())

    if match:
        return int(match.group(1))

    return 3

# =====================================================
# EXTRACT BUDGET
# =====================================================

def extract_budget(query):

    query = query.lower()

    lakh_match = re.search(r'(\d+)\s*l', query)

    if lakh_match:
        return int(lakh_match.group(1)) * 100000

    k_match = re.search(r'(\d+)\s*k', query)

    if k_match:
        return int(k_match.group(1)) * 1000

    amount_match = re.search(r'(\d+)', query)

    if amount_match:
        return int(amount_match.group(1))

    return 20000

# =====================================================
# WOMEN SAFETY
# =====================================================

def get_women_safety(score):

    if score >= 8:
        return "High"

    elif score >= 6:
        return "Moderate"

    return "Low"

# =====================================================
# CHAT API
# =====================================================

@router.post("/chat")
def chat(request: ChatRequest):

    query = request.query.lower()

    persons = request.persons

    days = extract_days(query)

    total_budget = extract_budget(query)

    destination = None

    # =================================================
    # DETECT DESTINATION
    # =================================================

    if not df.empty and "city" in df.columns:

        cities = df["city"].dropna().unique()

        for city in cities:

            if str(city).lower() in query:

                destination = city
                break

    # =================================================
    # FILTER DESTINATION
    # =================================================

    if destination:

        filtered_df = df[
            df["city"].astype(str).str.lower()
            == destination.lower()
        ]

    else:

        return {
            "ai_response": "Destination not found in dataset",
            "budget": {},
            "recommendations": [],
            "destination_map": {},
            "safety": {},
            "itinerary": []
        }

    # =================================================
    # NO DATA
    # =================================================

    if filtered_df.empty:

        return {
            "ai_response": "No places found",
            "budget": {},
            "recommendations": [],
            "destination_map": {},
            "safety": {},
            "itinerary": []
        }

    # =================================================
    # BUDGET CALCULATION
    # =================================================

    hotel_budget = int(total_budget * 0.45)

    food_budget = int(total_budget * 0.25)

    transport_budget = int(total_budget * 0.20)

    misc_budget = int(total_budget * 0.10)

    # =================================================
    # TAKE ONLY 2 PLACES
    # =================================================

    sample_places = filtered_df.sample(
        min(2, len(filtered_df))
    )

    recommendations = []

    for _, row in sample_places.iterrows():

        safety_score = float(
            row.get("safety_score", 7)
        )

        women_safety = get_women_safety(
            safety_score
        )

        recommendations.append({

            "name": row.get(
                "place",
                "Tourist Place"
            ),

            "city": row.get(
                "city",
                destination
            ),

            "state": row.get(
                "state",
                "India"
            ),

            "type": row.get(
                "type",
                "Tourism"
            ),

            "hotel_name": row.get(
                "hotel_name",
                "Tourist Residency"
            ),

            "budget": int(
                total_budget / 2
            ),

            "women_safety": women_safety,

            "safety_score": safety_score,

            "crowd_level": "Medium",

            "best_time": "Morning",

            "good_places": [

                row.get(
                    "good_place_1",
                    "Tourist Market"
                ),

                row.get(
                    "good_place_2",
                    "Food Street"
                )
            ],

            "bad_places": [

                row.get(
                    "bad_place_1",
                    "Avoid isolated roads"
                ),

                row.get(
                    "bad_place_2",
                    "Avoid dark streets"
                )
            ],

            "railway_distance": 5,

            "bus_distance": 3,

            "airport_distance": 15,

            "lat": float(
                row.get("lat", 28.6139)
            ),

            "lng": float(
                row.get("lng", 77.2090)
            )
        })

    # =================================================
    # ITINERARY
    # =================================================

    itinerary = []

    for day in range(1, days + 1):

        if day == 1:

            itinerary.append(
                f"Day {day} - Arrival and sightseeing"
            )

        elif day == days:

            itinerary.append(
                f"Day {day} - Shopping and return journey"
            )

        else:

            itinerary.append(
                f"Day {day} - Explore tourist attractions and food streets"
            )

    # =================================================
    # MAP LOCATION
    # =================================================

    map_location = recommendations[0]

    # =================================================
    # FINAL RESPONSE
    # =================================================

    return {

        "ai_response":
        f"Budget trip planned for {persons} persons to {destination}",

        "budget": {

            "hotel": hotel_budget,

            "food": food_budget,

            "transport": transport_budget,

            "misc": misc_budget,

            "total": total_budget
        },

        "recommendations": recommendations,

        "destination_map": {

            "name": map_location["name"],

            "lat": map_location["lat"],

            "lng": map_location["lng"]
        },

        "safety": {

            "women_safety":
            recommendations[0]["women_safety"],

            "child_friendly": "Yes",

            "night_risk": "Low"
        },

        "itinerary": itinerary
    }