# 📑 Multi-Document RAG Chatbot

A **context-aware Multi-Document Retrieval-Augmented Generation (RAG) chatbot** that allows users to interact with multiple PDF documents through natural language queries. The chatbot retains **conversation memory**, enabling meaningful follow-up questions and coherent multi-turn conversations.

---

## Features

- Read and process multiple PDF documents  
- Extract and chunk text into smaller, meaningful segments  
- Generate vector embeddings using HuggingFace models  
- Store embeddings persistently in ChromaDB  
- Perform semantic search for relevant document context  
- Maintain conversational memory across user interactions  
- Generate accurate, context-aware responses using **LLaMA 3.3 70B** via Groq  
- Interactive web interface built with Streamlit  

---

## 🧠 How It Works

**Pipeline Overview:**

PDF Documents → Text Extraction → Text Chunking → Vector Embeddings (HuggingFace) → ChromaDB (Vector Store) → Semantic Retrieval → LLaMA 3.3 70B (Groq) → Conversational Response



---

## 🛠️ Tech Stack

- **LangChain** – RAG pipeline & conversational retrieval  
- **ChromaDB** – Vector database for semantic search  
- **HuggingFace Embeddings** – Text vectorization  
- **Groq (LLaMA 3.3 70B)** – Large Language Model inference  
- **Streamlit** – User interface  
- **Python** – Core implementation  

---

## 📂 Project Structure

Multi_document_RAG_chatbot/
│
├── main.py # Streamlit application
├── vectorize_documents.py # PDF processing & embedding generation
├── vector_db_dir/ # Persistent ChromaDB storage
├── config.json # API key configuration (ignored in Git)
├── config.example.json # Example configuration file
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/multi-document-rag-chatbot.git
cd multi-document-rag-chatbot

---

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate

