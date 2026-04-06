from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.document_loaders import Docx2txtLoader
import os

def load_document(file_path: str):
    """
    Load a document from a file path.
    Supports PDF, TXT, and DOCX files.
    """
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)
    elif extension == ".txt":
        loader = TextLoader(file_path)
    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")

    documents = loader.load()
    return documents