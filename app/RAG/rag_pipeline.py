from sentence_transformers import SentenceTransformer

from app.RAG.llm import AIClient
from app.db.vector_store import collection

model =SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = AIClient()

def generate_answer(query:str):

    # step 1 -- Embed query
    query_embedding = model.encode(query, normalize_embeddings=True)

    # step 2 -- Retrieve context
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results.get("documents",[])[0]
    print(documents)

    if not documents:
        return {
            "answer":"No relevant information found",
            "sources":[]
        }


    context = "\n\n".join(documents)
    print(context)

    # step 3 -- Build strict prompt
    prompt = build_prompt(context,query)

    #step 4 -- Call LLM
    answer = client.ask(prompt)

    return {
        "answer":answer,
        "sources": [doc for doc in documents]
    }





def build_prompt(context,query):
    return f"""
You are a strict AI assistant.
use info

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

