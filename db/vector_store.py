import chromadb

# ----------------  initialize DB and persist directory
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory = "./chroma_db"
    )
)
collection = client.get_or_create_collection(name= "docs")



