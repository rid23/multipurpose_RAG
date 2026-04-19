import chromadb

# ----------------  initialize DB with persistence directory
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory = "./chroma_db"
    )
)
collection = client.get_or_create_collection(name= "docs1")



