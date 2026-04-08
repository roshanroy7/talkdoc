from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    """
    Split documents into smaller chunks for embedding.
    chunk_size: number of characters per chunk
    chunk_overlap: characters shared between chunks to preserve context
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    return chunks