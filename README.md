# TalkDoc 

A RAG-powered document Q&A system. Upload any PDF or text file and ask questions about it in plain English.

Built with LangChain, ChromaDB, OpenAI, and Streamlit.

## What it does

- Upload one or multiple PDFs or text files
- Automatically chunks, embeds, and indexes your documents
- Ask questions in plain English and get accurate, grounded answers
- See the exact source chunk the answer came from

## Tech stack

- LangChain — document loading, chunking, retrieval chain
- ChromaDB — local vector database
- OpenAI API — embeddings + language model
- Streamlit — web interface

## Project structure

talkdoc/
│
├── src/
│   ├── loader.py       # document loading (PDF, TXT, DOCX)
│   ├── chunker.py      # text splitting
│   ├── embedder.py     # embedding + vector store
│   └── retriever.py    # retrieval chain
│
├── app.py              # Streamlit UI
├── requirements.txt    # dependencies
└── .gitignore

## Setup

coming soon

## Demo

! [TalkDoc Demo](assets/demo.png)

## Status

In progress
