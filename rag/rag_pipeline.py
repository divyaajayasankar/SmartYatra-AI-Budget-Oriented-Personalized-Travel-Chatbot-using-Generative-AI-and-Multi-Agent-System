import pandas as pd

from rag.vector_store import collection
from rag.embeddings import generate_embedding


def ingest_data():

    df = pd.read_excel(
        r"data\india_tourist_places.xlsx"
    )

    print(df.columns)

    # LIMIT TO FIRST 100 ROWS
    df = df.head(100)

    documents = []
    embeddings = []
    ids = []

    for idx, row in df.iterrows():

        text = f"""
        Place: {row.get('place_name', '')}
        State: {row.get('state', '')}
        City: {row.get('city', '')}
        Type: {row.get('type', '')}
        Budget: {row.get('avg_budget', '')}
        Safety: {row.get('safety_score', '')}
        """

        embedding = generate_embedding(text)

        documents.append(text)

        embeddings.append(embedding)

        ids.append(str(idx))

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print("Data successfully ingested")


if __name__ == "__main__":
    ingest_data()