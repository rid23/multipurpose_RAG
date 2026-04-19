import streamlit as st
import os

from app.RAG.document_processing import process_document
from app.RAG.rag_pipeline import generate_answer

# 1. App Configuration
st.set_page_config(page_title="Demo Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 Enterprise Support Agent")

# 2. The Sidebar
with st.sidebar:
    st.header("⚙️ Document Upload")
    st.write("Upload a PDF or Text file to give the AI temporary knowledge.")

    # file uploader!
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])

    if uploaded_file:
        save_path = os.path.join("uploads", uploaded_file.name)

        os.makedirs("uploads", exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        chunks = process_document(save_path)                                 #   called the document_processor function which returns no. of chunks and embed the vectors of file in chromadb

        st.success(f"Loaded: {uploaded_file.name}\n\nTotal chunks created: {chunks}")     #   to show how many no. of chunks created

    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    # 3. Initialize Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Draw Past Messages
for msg in st.session_state.messages:
    avatar_icon = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar_icon):
        st.write(msg["content"])

# 5. The Main Chat Loop
if prompt := st.chat_input("Ask a question about the documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Searching knowledge base and generating answer..."):

            reply = generate_answer(prompt)                                         # called function that matches the query within the given documents

            final_answer = f"I read your file and processed your question: '{prompt}'.\n ### This is a simulated response:\n\n {reply["answer"]}"     # passed the reply to final answer command whcih will be shown

            st.write(final_answer)

    st.session_state.messages.append({"role": "assistant", "content": final_answer})