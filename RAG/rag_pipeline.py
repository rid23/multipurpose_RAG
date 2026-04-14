from sentence_transformers import SentenceTransformer

from app.RAG.llm import AIClient
from app.db.vector_store import collection

model =SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = AIClient()

def generate_answer(query:str):

    # step 1 -- Embed query
    query_embedding = model.encode(query)

    # step 2 -- Retrieve context
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results.get("documents",[[]])[0]

    if not documents:
        return {
            "answer":"No relevant information found",
            "sources":[]
        }

    context = "\n\n".join(documents)

    # step 3 -- Build strict prompt
    prompt = build_prompt(context,query)

    #step 4 -- Call LLM
    answer = client.ask(prompt)

    return {
        "answer":answer,
        "sources":documents
    }





def build_prompt(context,query):
    return f"""
You are a strict AI assistant.

RULES:
1. Answer ONLY from the provided context
2. DO NOT use outside knowledge
3. If answer is not in context, say:
        'I could not find this in provided documents'
4. Be concise and clear

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""