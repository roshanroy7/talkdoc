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
    You are a helpful assistant that answers questions based on the provided document context.
    Be conversational, detailed and thorough in your answers.
    Use all the relevant information from the context below.
    If the context contains lists, explain each point.
    If you find relevant information, elaborate on it — don't just summarise briefly.
    Only say you don't know if the information is truly not in the context.

    Context: {context}
    Question: {question}

    Answer:
    """)

    retriever = vector_store.as_retriever(search_kwargs={"k": 6})

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain