def ask_llm(prompt):

    prompt = prompt.lower()

    if "goa" in prompt:
        return """
        Goa Trip Plan

        Day 1:
        - Baga Beach
        - Fort Aguada
        - Cruise Dinner

        Day 2:
        - Dudhsagar Falls
        - Calangute Beach
        - Shopping

        Estimated Budget: ₹8000
        Safety Score: 8/10
        """

    elif "kerala" in prompt:
        return """
        Kerala Trip Plan

        Day 1:
        - Munnar Tea Gardens

        Day 2:
        - Alleppey Boat House

        Estimated Budget: ₹12000
        Safety Score: 9/10
        """

    else:
        return f"""
        AI Travel Plan Generated

        Destination Request:
        {prompt}

        Estimated Budget: ₹10000

        Safety Score: 8/10
        """