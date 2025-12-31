from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# loading the embedding model
embeddings = HuggingFaceEmbeddings()

loader = DirectoryLoader(
    path="data",
    glob="./*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500,
)
text_chunk = text_splitter.split_documents(documents)

vectordb = Chroma.from_documents(
    documents=text_chunk,
    embedding=embeddings,
    persist_directory="vector_db_dir"
)

print("Document Vectorized")

