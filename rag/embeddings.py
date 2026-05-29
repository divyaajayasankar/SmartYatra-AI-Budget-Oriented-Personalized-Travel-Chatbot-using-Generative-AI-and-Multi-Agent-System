def generate_embedding(text):

    embedding = [
        float(ord(c))
        for c in text[:100]
    ]

    while len(embedding) < 100:
        embedding.append(0.0)

    return embedding