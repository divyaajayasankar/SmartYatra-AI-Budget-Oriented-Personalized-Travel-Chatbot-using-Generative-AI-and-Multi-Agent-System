import pandas as pd
import random

# Read Excel dataset
df = pd.read_excel("india_tourist_places.xlsx")

# Add enhanced columns
df["hotel_cost_per_night"] = [
    random.randint(500, 5000) for _ in range(len(df))
]

df["food_cost_per_day"] = [
    random.randint(300, 2000) for _ in range(len(df))
]

df["transport_cost"] = [
    random.randint(200, 3000) for _ in range(len(df))
]

df["railway_distance_km"] = [
    random.randint(1, 20) for _ in range(len(df))
]

df["bus_distance_km"] = [
    random.randint(1, 15) for _ in range(len(df))
]

df["airport_distance_km"] = [
    random.randint(5, 50) for _ in range(len(df))
]

df["safety_score"] = [
    round(random.uniform(5, 10), 1) for _ in range(len(df))
]

df["family_friendly"] = [
    random.choice(["Yes", "No"]) for _ in range(len(df))
]

# Save enhanced dataset
df.to_csv(
    "india_tourist_places.csv",
    index=False
)

print("Enhanced dataset created successfully")