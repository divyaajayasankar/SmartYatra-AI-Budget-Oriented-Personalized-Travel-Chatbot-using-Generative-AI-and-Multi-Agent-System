import math


def calculate_distance(source, destination):

    return {
        "source": source,
        "destination": destination,
        "distance_km": round(
            math.floor(abs(len(source) - len(destination)) * 12 + 120),
            2
        ),
        "estimated_time": f"{round((abs(len(source) - len(destination)) + 4), 1)} hrs"
    }


def get_route_details(source, destination):

    route = calculate_distance(source, destination)

    return {
        "route": f"{source} → {destination}",
        "distance": route["distance_km"],
        "travel_time": route["estimated_time"],
        "recommended_transport": "Train"
    }