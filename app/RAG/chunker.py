
def chunk_text(text,size=1200,overlap=150):

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + size
        chunk = text[start : end]

        chunks.append(chunk.strip())
        start += size - overlap

    return chunks

