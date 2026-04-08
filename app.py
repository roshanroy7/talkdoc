import streamlit as st
from dotenv import load_dotenv
import tempfile
import os

from src.loader import load_document
from src.chunker import chunk_documents
from src.embedder import create_vector_store
from src.retriever import create_retriever

load_dotenv()

st.set_page_config(page_title="TalkDoc",layout="centered")
st.title("TalkDoc")
st.caption("Upload any document and ask questions about it")

if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])
    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name
            documents = load_document(tmp_path)
            chunks = chunk_documents(documents)
            vector_store = create_vector_store(chunks)
            st.session_state.retriever = create_retriever(vector_store)
            os.unlink(tmp_path)
        st.success(f"Ready! {len(chunks)} chunks indexed.")
        st.session_state.chat_history = []

if st.session_state.retriever is None:
    st.info("Upload a document on the left to get started.")
else:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.chat_input("Ask anything about your document...")
    if question:
        with st.chat_message("user"):
            st.write(question)
        st.session_state.chat_history.append({"role": "user", "content": question})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.retriever.invoke(question)
                st.write(answer)

        st.session_state.chat_history.append({"role": "assistant", "content": answer})