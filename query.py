from src.embedding.embedding_manager import EmbeddingManager
from src.vectordb.vector_store import VectorStore
from src.retrieval.retriever import RAGRetriever
from src.llm.groq_client import get_llm
from src.pipeline.rag_pipeline import rag_sys


def main():

    print("\nStarting query pipeline...\n")

    # Load existing vector DB
    vectorstore = VectorStore()

    # IMPORTANT — do NOT call add_documents here

    embedding_manager = EmbeddingManager()

    retriever = RAGRetriever(vectorstore, embedding_manager)

    llm = get_llm()

    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        response = rag_sys(query, retriever, llm)

        print("\nAnswer:\n")
        print(response)


if __name__ == "__main__":
    main()
