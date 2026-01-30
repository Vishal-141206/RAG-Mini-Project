from langchain_community.document_loaders import TextLoader
import os

DATA_DIR = "policy_docs"

def load_documents():
    documents = []

    files = [
        "refund_policy.txt",
        "cancellation_policy.txt",
        "shipping_policy.txt",
    ]

    for file in files:
        file_path = os.path.join(DATA_DIR, file)
        documents.extend(
            TextLoader(file_path, encoding="utf-8").load()
        )

    return documents
