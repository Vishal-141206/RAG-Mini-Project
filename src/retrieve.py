def retrieve_context(vectordb, query, k=3):
    results = vectordb.similarity_search(query, k=k)

    if not results:
        return None
    return "\n\n".join(doc.page_content[:800] for doc in results)

