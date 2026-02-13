from src.loaders.pdf_loader import process_all_pdfs
from src.processing.text_splitter import split_documents
from src.embedding.embedding_manager import EmbeddingManager
from src.vectordb.vector_store import VectorStore


def main():

    print("\nStarting indexing pipeline...\n")

    # Initialize vector store FIRST
    vectorstore = VectorStore()

    # Prevent accidental overwriting
    if vectorstore.collection.count() > 0:
        print("Vector DB already exists. Delete it if you want to re-index.")
        return

    # Load PDFs
    documents = process_all_pdfs("data/pdf")

    # Split
    chunks = split_documents(documents)

    # Embeddings
    embedding_manager = EmbeddingManager()

    texts = [doc.page_content for doc in chunks]
    embeddings = embedding_manager.generate_embeddings(texts)

    # Store vectors
    vectorstore.add_documents(chunks, embeddings)

    print("\nIndexing completed...")


if __name__ == "__main__":
    main()
