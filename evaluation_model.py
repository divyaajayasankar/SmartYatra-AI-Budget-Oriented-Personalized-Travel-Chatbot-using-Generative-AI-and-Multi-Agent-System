import pandas as pd

# ------------------------------------------
# LOAD DATASET
# ------------------------------------------

df = pd.read_csv(
    "data/enhanced_india_tourist_dataset.csv"
)

# ------------------------------------------
# EVALUATION
# ------------------------------------------

total_places = len(df)

safe_places = len(
    df[df["women_safety"] == "High"]
)

avg_budget = df["budget"].mean()

avg_safety = df["safety_score"].mean()

# ------------------------------------------
# PRINT RESULTS
# ------------------------------------------

print("\n========== MODEL EVALUATION ==========\n")

print(f"Total Tourist Places : {total_places}")

print(f"High Women Safety Places : {safe_places}")

print(f"Average Budget : ₹{round(avg_budget, 2)}")

print(f"Average Safety Score : {round(avg_safety, 2)}")

print("\n======================================\n")