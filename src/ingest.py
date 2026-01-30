from langchain_community.document_loaders import TextLoader

def load_documents():
    documents = []

    documents += TextLoader(
        "data/refund_policy.txt",
        encoding="utf-8"
    ).load()

    documents += TextLoader(
        "data/cancellation_policy.txt",
        encoding="utf-8"
    ).load()

    documents += TextLoader(
        "data/shipping_policy.txt",
        encoding="utf-8"
    ).load()

    return documents
