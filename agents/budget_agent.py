import pandas as pd

df = pd.read_excel(
    r"data\india_tourist_places.xlsx"
)


def calculate_budget(query):

    matched = df[
        df.astype(str).apply(
            lambda row: row.str.contains(
                query,
                case=False,
                na=False
            ).any(),
            axis=1
        )
    ]

    if len(matched) == 0:

        return {
            "hotel_cost": 4000,
            "food_cost": 2000,
            "transport_cost": 3000,
            "total_cost": 9000
        }

    return {
        "hotel_cost": 3500,
        "food_cost": 1200,
        "transport_cost": 2500,
        "total_cost": 7200
    }