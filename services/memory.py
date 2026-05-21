conversation_memory = []


def save_conversation(user_query, bot_response):

    conversation_memory.append({
        "user": user_query,
        "assistant": bot_response
    })


def get_conversation_history():

    return conversation_memory[-5:]