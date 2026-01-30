import streamlit as st

from src.ingest import load_documents
from src.chunk import chunk_documents
from src.store import create_vectorstore
from src.retrieve import retrieve_context
from src.prompt import PROMPT
from src.qa import answer_question

@st.cache_resource
def setup_rag():
    docs = load_documents()
    chunks = chunk_documents(docs)
    vectordb = create_vectorstore(chunks)
    return vectordb

st.set_page_config(page_title="RAG Policy Assistant", layout="centered")

st.title("RAG Policy Assistant")
st.write("Ask questions about company policies.")

vectordb = setup_rag()

question = st.text_input("Ask a policy question:")

if question:
    context = retrieve_context(vectordb, question)
    answer = answer_question(context, question, PROMPT)
    st.markdown(answer)
