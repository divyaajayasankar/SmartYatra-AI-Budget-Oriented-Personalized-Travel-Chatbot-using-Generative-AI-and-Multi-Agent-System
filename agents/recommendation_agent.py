from rag.embeddings import generate_embedding
from rag.vector_store import collection

def recommend_places(query):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results["documents"][0]