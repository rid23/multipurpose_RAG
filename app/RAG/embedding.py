import uuid
from app.db.vector_store import collection
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_vectors(chunks):

    ids = [str(uuid.uuid4()) for _ in chunks]
    embeddings = model.encode(chunks, normalize_embeddings=True).tolist()

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )


