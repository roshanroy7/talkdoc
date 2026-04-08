from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import os

def create_vector_store(chunks):
    """
    Convert chunks into vectors and store them in ChromaDB.
    Uses free local Ollama embeddings — no API key needed.
    """
    embeddings = OllamaEmbeddings(model="mistral")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB")
    return vector_store


def load_vector_store():
    """
    Load an existing ChromaDB vector store from disk.
    """
    embeddings = OllamaEmbeddings(model="mistral")

    vector_store = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return vector_store