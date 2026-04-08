from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

def create_retriever(vector_store):
    """
    Create a retrieval chain using free local Mistral via Ollama.
    """
    llm = OllamaLLM(model="mistral")

    prompt = PromptTemplate.from_template("""
    You are a helpful assistant. Use the following context from the 
    uploaded document to answer the question accurately.
    If you don't know the answer from the context, say 
    "I couldn't find that in the document."

    Context: {context}
    Question: {question}

    Answer:
    """)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain