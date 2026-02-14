# Conversational RAG System (FastAPI + Streamlit)

A modular, production-style Retrieval-Augmented Generation (RAG) system that enables conversational querying over PDF documents.

This project includes:

- Offline document indexing

- Persistent Chroma vector database

- SentenceTransformer embeddings

- Groq LLM integration

- FastAPI backend (AI service)

- Streamlit frontend (chat UI)

- Conversation memory support

- Modular architecture<br><br>





## Architecture

```text
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
Retriever (ChromaDB)
        ↓
Embeddings (SentenceTransformers)
        ↓
Groq LLM
```
## Project Structure

```
multi_document_rag_chatbot/
│
├── app.py                  # FastAPI backend
├── streamlit_app.py        # Streamlit chat UI
├── index.py                # Offline indexing pipeline
├── query.py                # CLI querying
│
├── src/
│   ├── loaders/
│   ├── processing/
│   ├── embedding/
│   ├── vectordb/
│   ├── retrieval/
│   ├── llm/
│   └── pipeline/
│
├── data/
│   ├── pdf/
│   └── vector_store/
│
├── requirements.txt
└── README.md
```

## Features

- Modular codebase

- Persistent vector storage

- Conversation-aware querying

- FastAPI REST API

- Streamlit Chat UI

- Safe indexing protection

- Scalable architecture


## Installation
### 1️⃣ Clone Repository
```bash
git clone <your-repo-url>
cd rag_sys
```

### 2️⃣ Create Virtual Environment
### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```
### Mac/Linux
```bash
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a ```.env``` file in root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

## Indexing Documents (Run Once)

Place your PDFs inside:

```bash

data/pdf/
```

Then run:

```bash
python index.py
```

This will:

- Load PDFs

- Split into chunks

- Generate embeddings

- Store vectors in ChromaDB

⚠️ If vector DB already exists, indexing will stop to prevent duplicates.

To re-index:

Delete:
```bash
data/vector_store/
```

Then run ```index.py``` again.
---
## Start Backend (FastAPI)
```bash
uvicorn app:app --reload
```

Access API docs:
```bash
http://127.0.0.1:8000/docs
```

Test endpoint:
```bash
POST /ask
```
```json
Example JSON:

{
  "question": "What are the symptoms of respiratory infections?"
}
```

## Start Streamlit UI

In a new terminal (backend must be running):

```bash
streamlit run streamlit_app.py
```

Open:
```
http://localhost:8501
```

You now have a conversational document assistant.


## Conversation Memory

The Streamlit UI maintains session-based chat history using:
```
st.session_state
```

Conversation history is sent to the backend for contextual responses.

For performance, only the last N messages should be sent to avoid token explosion.


## Technologies Used

- FastAPI

- Streamlit

- ChromaDB

- SentenceTransformers (all-MiniLM-L6-v2)

- Groq LLM

- LangChain components

- Python 3.12


## Development Workflow
###Add new documents:

1. Place PDFs in ```data/pdf```

2. Delete ```data/vector_store```
3. Run ```python index.py```

### Query:

- Use Streamlit UI

- Or call FastAPI endpoint



## Performance Notes

- Embedding model loads once at backend startup

- Vector DB is persistent

- Streamlit acts as frontend only

- Backend scales independently



## Author

<p>
<b>Ramith Pesala</b><br>
AI Engineer | RAG Systems | LLM Applications
</p>

## Why This Project Is Valuable

This repository demonstrates:

- Real-world RAG architecture

- Backend–frontend separation

- Modular AI engineering

- Scalable system design

- Production-ready patterns

It is not a notebook demo — it is a deployable AI system.

