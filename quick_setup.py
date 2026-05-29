import os
import sys

# Create the models directory
models_dir = r"d:\travel_chatbot_project\backend\models"
os.makedirs(models_dir, exist_ok=True)

requests_py = r"""from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, validator


class TravelMode(str, Enum):
    FLIGHT = "flight"
    TRAIN = "train"
    BUS = "bus"
    CAR = "car"
    SHIP = "ship"


class DepartureType(str, Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    FLEXIBLE = "flexible"


class FoodPreference(str, Enum):
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    HALAL = "halal"
    KOSHER = "kosher"
    GLUTEN_FREE = "gluten_free"
    NO_PREFERENCE = "no_preference"


class TransportClass(str, Enum):
    ECONOMY = "economy"
    PREMIUM_ECONOMY = "premium_economy"
    BUSINESS = "business"
    FIRST_CLASS = "first_class"


class TransportationCost(BaseModel):
    mode: TravelMode = Field(..., description="Mode of transportation")
    cost_per_person: float = Field(..., gt=0, description="Cost per person in USD")
    total_cost: float = Field(..., gt=0, description="Total transportation cost in USD")
    duration_hours: Optional[float] = Field(None, description="Duration of travel in hours")
    carbon_footprint_kg: Optional[float] = Field(None, description="Carbon footprint in kilograms")

    @validator("total_cost")
    def validate_total_cost(cls, v, values):
        if v < 0:
            raise ValueError("Total cost must be positive")
        return v

    class Config:
        description = "Transportation cost breakdown"


class BudgetBreakdown(BaseModel):
    transportation: float = Field(..., gt=0, description="Transportation costs in USD")
    accommodation: float = Field(..., gt=0, description="Accommodation costs in USD")
    food: float = Field(..., gt=0, description="Food/dining costs in USD")
    activities: float = Field(..., gt=0, description="Activities and attractions costs in USD")
    miscellaneous: float = Field(default=0, ge=0, description="Miscellaneous costs in USD")
    total_budget: float = Field(..., gt=0, description="Total budget in USD")

    @validator("total_budget")
    def validate_total_budget(cls, v, values):
        if "transportation" in values and "accommodation" in values and \
           "food" in values and "activities" in values and "miscellaneous" in values:
            expected_total = (
                values["transportation"] + values["accommodation"] + 
                values["food"] + values["activities"] + values["miscellaneous"]
            )
            if abs(v - expected_total) > 0.01:
                raise ValueError(
                    f"Total budget ({v}) must equal sum of categories ({expected_total})"
                )
        return v

    class Config:
        description = "Budget breakdown for travel"


class Accommodation(BaseModel):
    name: str = Field(..., min_length=1, description="Name of accommodation")
    location: str = Field(..., min_length=1, description="Location/city of accommodation")
    type: str = Field(..., description="Type of accommodation (hotel, hostel, airbnb, etc.)")
    price_per_night_usd: float = Field(..., gt=0, description="Price per night in USD")
    nights: int = Field(..., gt=0, description="Number of nights")
    total_cost_usd: float = Field(..., gt=0, description="Total accommodation cost in USD")
    rating: Optional[float] = Field(None, ge=0, le=5, description="Rating from 0 to 5")
    amenities: List[str] = Field(default_factory=list, description="List of amenities")

    @validator("total_cost_usd")
    def validate_total_cost(cls, v, values):
        if "price_per_night_usd" in values and "nights" in values:
            expected_total = values["price_per_night_usd"] * values["nights"]
            if abs(v - expected_total) > 0.01:
                raise ValueError(
                    f"Total cost must equal price per night * nights ({expected_total})"
                )
        return v

    class Config:
        description = "Accommodation recommendation with pricing"


class SafetyInfo(BaseModel):
    destination: str = Field(..., description="Destination city/country")
    safety_rating: int = Field(..., ge=1, le=10, description="Safety rating from 1 (unsafe) to 10 (very safe)")
    crime_rate: str = Field(..., description="Crime rate level (low, moderate, high)")
    health_recommendations: List[str] = Field(default_factory=list, description="Health/vaccination recommendations")
    emergency_contacts: Dict[str, str] = Field(default_factory=dict, description="Emergency contact numbers")
    travel_advisories: Optional[List[str]] = Field(None, description="Travel advisories and warnings")
    best_practices: List[str] = Field(default_factory=list, description="Safety best practices for travelers")

    @validator("safety_rating")
    def validate_safety_rating(cls, v):
        if not (1 <= v <= 10):
            raise ValueError("Safety rating must be between 1 and 10")
        return v

    class Config:
        description = "Safety information for travel destination"


class TravelRequest(BaseModel):
    origin_city: str = Field(..., min_length=1, description="City of departure")
    destination_city: str = Field(..., min_length=1, description="City of destination")
    departure_date: str = Field(..., description="Departure date (YYYY-MM-DD format)")
    return_date: Optional[str] = Field(None, description="Return date (YYYY-MM-DD format) for round trips")
    number_of_travelers: int = Field(..., gt=0, description="Number of travelers")
    budget_usd: float = Field(..., gt=0, description="Total budget in USD")
    travel_modes: List[TravelMode] = Field(default_factory=lambda: [TravelMode.FLIGHT], description="Preferred travel modes")
    departure_preference: DepartureType = Field(default=DepartureType.FLEXIBLE, description="Preferred departure time")
    food_preferences: List[FoodPreference] = Field(default_factory=list, description="Food preferences")
    transport_class: TransportClass = Field(default=TransportClass.ECONOMY, description="Preferred transport class")
    special_requirements: Optional[str] = Field(None, description="Special requirements or notes")

    @validator("number_of_travelers")
    def validate_travelers(cls, v):
        if v > 100:
            raise ValueError("Number of travelers cannot exceed 100")
        return v

    @validator("budget_usd")
    def validate_budget(cls, v):
        if v < 100:
            raise ValueError("Budget must be at least $100")
        return v

    class Config:
        description = "Travel request with all preferences"


class TravelResponse(BaseModel):
    request_id: str = Field(..., description="Unique request identifier")
    origin_city: str = Field(..., description="Origin city")
    destination_city: str = Field(..., description="Destination city")
    transportation_options: List[TransportationCost] = Field(default_factory=list, description="Available transportation options")
    accommodations: List[Accommodation] = Field(default_factory=list, description="Accommodation recommendations")
    budget_breakdown: Optional[BudgetBreakdown] = Field(None, description="Detailed budget breakdown")
    safety_information: Optional[SafetyInfo] = Field(None, description="Safety information for destination")
    estimated_total_cost: float = Field(..., gt=0, description="Estimated total cost in USD")
    trip_duration_days: int = Field(..., gt=0, description="Total trip duration in days")
    itinerary: Optional[List[str]] = Field(None, description="Suggested daily itinerary")
    tips_and_recommendations: Optional[List[str]] = Field(None, description="Travel tips and recommendations")
    created_at: Optional[str] = Field(None, description="Response creation timestamp (ISO format)")

    @validator("estimated_total_cost")
    def validate_estimated_cost(cls, v):
        if v < 100:
            raise ValueError("Estimated total cost must be at least $100")
        return v

    class Config:
        description = "Complete travel recommendation response"
"""

init_py = r"""from .requests import (
    TravelMode,
    DepartureType,
    FoodPreference,
    TransportClass,
    TravelRequest,
    TransportationCost,
    BudgetBreakdown,
    Accommodation,
    SafetyInfo,
    TravelResponse,
)

__all__ = [
    "TravelMode",
    "DepartureType",
    "FoodPreference",
    "TransportClass",
    "TravelRequest",
    "TransportationCost",
    "BudgetBreakdown",
    "Accommodation",
    "SafetyInfo",
    "TravelResponse",
]
"""

with open(os.path.join(models_dir, "requests.py"), "w") as f:
    f.write(requests_py)

with open(os.path.join(models_dir, "__init__.py"), "w") as f:
    f.write(init_py)

print("SUCCESS: Files created in", models_dir)
