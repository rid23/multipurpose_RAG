
def chunk_text(text,size=500,overlap=100):

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + size
        chunk = text[start : end]

        #----------sentence boundary fix-------------
        if end < text_length:
            last_period = chunk.rfind(".")
            if last_period != -1:
                chunk = chunk[:last_period+1]

        chunks.append(chunk.strip())
        start += size - overlap

    return chunks


