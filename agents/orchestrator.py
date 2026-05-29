from agents.budget_agent import calculate_budget
from agents.itinerary_agent import generate_itinerary
from agents.recommendation_agent import recommend_places
from agents.safety_agent import safety_analysis

def run_agents(query):

    budget = calculate_budget(query)

    itinerary = generate_itinerary(query)

    recommendations = recommend_places(query)

    safety = safety_analysis(query)

    return {
        "budget": budget,
        "itinerary": itinerary,
        "recommendations": recommendations,
        "safety": safety
    }