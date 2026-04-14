import uuid
from app.db.vector_store import collection
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_vectors(chunks):

    ids = []
    embeddings = []

    for chunk in chunks:
        ids.append(str(uuid.uuid4()))
        embeddings.append(model.encode(chunk))

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )


