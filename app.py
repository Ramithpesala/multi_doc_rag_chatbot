from fastapi import FastAPI
from pydantic import BaseModel

from src.embedding.embedding_manager import EmbeddingManager
from src.vectordb.vector_store import VectorStore
from src.retrieval.retriever import RAGRetriever
from src.llm.groq_client import get_llm
from src.pipeline.rag_pipeline import rag_sys


app = FastAPI(title="RAG API")


# Load EVERYTHING once at startup
print("\nLoading RAG system...\n")

vectorstore = VectorStore()
embedding_manager = EmbeddingManager()
retriever = RAGRetriever(vectorstore, embedding_manager)
llm = get_llm()

print("\nRAG system ready!\n")


# Request schema
class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "RAG API is running"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    response = rag_sys(
        request.question,
        retriever,
        llm
    )

    return {
        "question": request.question,
        "answer": response
    }
