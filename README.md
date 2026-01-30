# RAG-Mini-Project

# RAG Mini Project – Policy QA Assistant

## Architecture Overview
The system follows a basic Retrieval-Augmented Generation (RAG) flow:

Documents → Chunking → Embeddings → Vector Store → Semantic Retrieval → LLM → Answer

---

## Data Preparation
Policy documents are loaded as plain text and split into chunks using
`RecursiveCharacterTextSplitter`.

- Chunk size: 400 characters
- Chunk overlap: 80 characters

This size preserves clause-level meaning in policy text while overlap prevents
information loss at chunk boundaries.

---

## RAG Pipeline
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- Vector store: Chroma
- Retrieval: semantic similarity search with top-k = 3
- Retrieved chunks are passed to the LLM as context

Limiting retrieval to top-k reduces irrelevant context and hallucinations.

---

## Prompt Engineering
The prompt explicitly instructs the model to:
- Answer only from retrieved context
- Avoid using prior knowledge
- Clearly refuse when information is missing
- Return a structured response (Answer, Evidence, Confidence)

This prompt design improves grounding and answer reliability.

---

## Evaluation
A small evaluation set includes:
- Fully answerable questions
- Partially answerable questions
- Unanswerable questions

Evaluation focuses on accuracy, hallucination avoidance, and clarity.
Results are recorded in `eval/evaluation.md`.

---

## Edge Case Handling
- If no relevant documents are retrieved, the system responds that the information
  is not available.
- If the question is outside the knowledge base, the system explicitly refuses.

---

## LLM Note
A local instruction-tuned LLM is used for generation to ensure deterministic,
offline execution. The LLM component is modular and can be replaced without
changes to the RAG pipeline.
