#  AI Support Agent (RAG-Based)

An AI-powered customer support system that answers queries strictly from your business documents using Retrieval-Augmented Generation (RAG).

Built for real-world use cases like:

* Customer support automation
* Internal knowledge base
* Document Q&A systems

---


#  Features

* 📄 Upload PDF / TXT documents
* 🔍 Intelligent semantic search (vector embeddings)
* 💬 Ask questions in natural language
* 🧾 Answers strictly from your data (no hallucination)
* 📌 Source-based responses (transparent & reliable)

---

```
User → Upload Document
        ↓
Text Extraction → Chunking → Embeddings
        ↓
     Vector DB (Chroma)
        ↓
User Query → Embedding → Similarity Search
        ↓
Context + Prompt → LLM
        ↓
Answer + Sources
```


```
ai-support-agent/
│
├── app/
│   ├── db/                              # Vector DB setup
│   └── RAG/                             # Core logic (RAG pipeline)
│        ├──  chunker.py                 # chunking logic
│        ├──  document_processing.py     # processing documents pipeline
│        ├──  embedding.py               # embedding vectors in to DB 
│        ├──  llm.py                     # ai bot
│        └──  rag_pipeline.py            # RAG pipeline controller
│
│
├── streamlit_app.py              # Simple UI
├── requirements.txt
└── .env

```

---

#  Setup & Installation (Local)

## 1. Clone the repo

```
git clone https://github.com/rid23/multipurpose_RAG.git
cd ai-support-agent
```

---

## 2. Create virtual environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```
python -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Add environment variables

inside `.env` file :

```
GEMINI_API_KEY=your_api_key_here
```

---


## 5. Run frontend


```
streamlit run streamlit_app.py
```


#  How to Use

1. Upload a document (PDF or TXT)
2. Ask a question
3. Get answers based only on uploaded data
4. View source references

---



#  Use Cases

* Small business customer support bot
* Legal document assistant
* Internal company knowledge system
* FAQ automation

---


#  Contributing

Pull requests are welcome. For major changes, open an issue first.

---

#  Contact

If you want to use this system for your business or collaborate, feel free to reach out.
