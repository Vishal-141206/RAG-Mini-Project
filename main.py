from src.ingest import load_documents
from src.chunk import chunk_documents
from src.store import create_vectorstore
from src.retrieve import retrieve_context
from src.prompt import PROMPT
from src.qa import answer_question

def main():
    docs = load_documents()
    chunks = chunk_documents(docs)
    vectordb = create_vectorstore(chunks)

    print("RAG Policy Assistant is ready.")
    print("Type a question (Ctrl+C to exit)\n")

    while True:
        question = input("Ask a policy question: ").strip()

        if not question:
            print("Please enter a question.\n")
            continue

        context = retrieve_context(vectordb, question)

        answer = answer_question(context, question, PROMPT)

        print("\n" + answer + "\n")

if __name__ == "__main__":
    main()
