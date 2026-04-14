from app.RAG.chunker import chunk_text, chunk_word
from app.RAG.embedding import embed_vectors
from pypdf import PdfReader


def process_document(path):
    if path.endswith(".pdf"):
        text = load_pdf(path=path)
    else:
        text = load_doc(path=path)

    if not text:
        return 0

    text = text.replace("\n"," ").strip()

    chunks = chunk_text(text=text)

    embed_vectors(chunks)

    return len(chunks)





#----------------------------- pdf loader
def load_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()

        if content:
            text += content

    return text



#----------------------------- txt loader
def load_doc(path):
    with open(path,"r",encoding="utf-8") as file:
        text = file.read()

    return text

