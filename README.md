# RAG Policy Assistant – Retrieval-Augmented Question Answering System

A production-ready **Retrieval-Augmented Generation (RAG)** application that answers user queries strictly based on company policy documents.  
The system is designed to **avoid hallucinations**, provide **grounded evidence**, and handle **unanswerable queries safely**.

🔗 **Live Demo:** https://Vishal1412-rag-policy.hf.space

---

## Problem Statement

Large Language Models often hallucinate when asked factual or policy-based questions.  
This project demonstrates how to mitigate that issue by combining **semantic retrieval** with **controlled generation**, ensuring answers are derived only from verified documents.

---

## System Architecture

The system follows a standard but carefully implemented RAG pipeline:

Policy Documents
↓
Document Chunking
↓
Sentence Embeddings
↓
Vector Store (ChromaDB)
↓
Semantic Retrieval (Top-K)
↓
LLM with Grounding Prompt
↓
Structured Answer (Answer + Evidence + Confidence)

---


Each component is modular and replaceable without affecting the rest of the pipeline.

---

## Data Preparation

- Policy documents are stored as plain text files.
- Documents are split using `RecursiveCharacterTextSplitter`.

**Chunking configuration:**
- Chunk size: **400 characters**
- Chunk overlap: **80 characters**

This preserves clause-level meaning while preventing context loss at chunk boundaries.

---

## Embeddings & Vector Store

- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Vector store:** ChromaDB (persistent, lightweight)
- **Similarity search:** cosine similarity

Embeddings are generated once per session and cached to reduce redundant computation.

---

## Retrieval Strategy

- **Top-K retrieval:** `k = 3`
- Only the most semantically relevant chunks are passed to the LLM.

This constraint:
- reduces irrelevant context
- improves answer precision
- significantly lowers hallucination risk

---

## Prompt Engineering

The prompt enforces strict grounding rules:

- Use **only** retrieved context
- No prior knowledge or assumptions
- Explicit refusal when information is missing
- Structured output format:
  - **Answer**
  - **Evidence**
  - **Confidence**

This ensures responses are:
- interpretable
- auditable
- evaluator-friendly

---

## LLM Integration

- **Inference:** Groq-hosted LLM (LLaMA-3.1 family)
- API-based inference for reliability and low latency
- No local model assumptions in deployment

The LLM layer is fully modular and can be swapped without changing the RAG pipeline.

---

## Edge Case Handling

The system explicitly handles failure modes:

- **No relevant retrieval:** responds that information is not available
- **Partially answerable queries:** answers only what is supported by context
- **Out-of-scope queries:** safely refused

This behavior is intentional and evaluated.

---

## Evaluation Methodology

A small evaluation set is used to test:

- Fully answerable questions
- Partially answerable questions
- Unanswerable questions

Evaluation criteria:
- Answer correctness
- Grounding and evidence usage
- Hallucination avoidance
- Clarity and structure

Results are documented separately.

---

## Tech Stack

- **Python**
- **LangChain**
- **Sentence Transformers**
- **ChromaDB**
- **Groq API**
- **Streamlit**
- **Hugging Face Spaces (deployment)**

---

## Key Design Decisions

- Explicit refusal is preferred over speculative answers
- Evidence is mandatory for trust and auditability
- Retrieval is limited to reduce noise
- Caching is used to improve runtime efficiency

---

## What This Project Demonstrates

- Practical understanding of RAG systems
- Awareness of LLM failure modes
- Prompt engineering for safety and reliability
- Real-world deployment and debugging experience
- Clean, modular system design

---
