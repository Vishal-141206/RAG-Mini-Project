# RAG Policy Assistant – Retrieval-Augmented Question Answering System

A production-ready Retrieval-Augmented Generation (RAG) application that answers user queries strictly based on company policy documents.  
The system is designed to avoid hallucinations, provide grounded evidence, and handle unanswerable queries safely.

Live Demo: https://Vishal1412-rag-policy.hf.space

---

## Objective

The goal of this project is to build a lightweight Retrieval-Augmented Generation (RAG) system that demonstrates practical skills in working with large language models. The focus is on designing constraint-based prompts, refining response quality through iteration, and critically evaluating model outputs for correctness and reliability.

The system prioritizes factual accuracy, transparency, and responsible model behavior over fluent but unsupported answers.

---

## Problem Statement

A collection of internal company policy documents is provided, including policies related to refunds, order cancellations, and shipping. The task is to develop a question-answering assistant that can intelligently retrieve relevant information from these documents and respond to user queries.

The assistant should:
- Retrieve the most relevant sections from the policy documents
- Generate answers that are strictly grounded in retrieved content
- Avoid fabricating information when the documents do not contain an answer
- Use structured prompts to ensure clarity and verifiability

This setup reflects real-world scenarios where language models must operate under strict factual constraints.

---

## Setup Instructions

1. Clone the repository

    git clone https://github.com/Vishal-141206/RAG-Mini-Project  
    cd RAG-Mini-Project  

2. Create and activate a virtual environment

    python -m venv venv  
    source venv/bin/activate  

3. Install dependencies

    pip install -r requirements.txt  

4. Set environment variables

    export GROQ_API_KEY=your_api_key_here  

5. Run the application

    streamlit run app.py  

The application will be available at http://localhost:8501.

---

## System Architecture

The system follows a standard but carefully implemented Retrieval-Augmented Generation (RAG) pipeline:

Policy Documents  
⟶
Document Chunking  
⟶
Sentence Embeddings  
⟶
Vector Store (ChromaDB)  
⟶
Semantic Retrieval (Top-K)  
⟶
LLM with Grounded Prompt  
⟶
Structured Answer (Answer + Evidence + Confidence)

Each component is modular and replaceable.

---

## Data Preparation

- Policy documents are stored as plain text files.
- Documents are split using RecursiveCharacterTextSplitter.

Chunking configuration:
- Chunk size: 400 characters
- Chunk overlap: 80 characters

This preserves clause-level meaning while reducing context loss at chunk boundaries.

---

## Embeddings & Vector Store

- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- Vector store: ChromaDB
- Similarity metric: cosine similarity

Embeddings are generated once per session and cached to improve efficiency.

---

## Retrieval Strategy

- Top-K retrieval: k = 3
- Only the most relevant chunks are passed to the LLM

This constraint:
- reduces irrelevant context
- improves answer precision
- significantly lowers hallucination risk


---

## Prompt Used

The system uses a strict grounding prompt to enforce reliable behavior:

    You are a policy-compliance assistant.

    Rules:
    - Use ONLY the information provided in the context.
    - Do NOT use prior knowledge or assumptions.
    - If the answer is not present, clearly state that it is unavailable.
    - Do NOT guess or infer missing details.

    Context:
    {context}

    Question:
    {question}

    Answer format:
    Answer:
    Evidence:
    Confidence:

This prompt design ensures responses are grounded, auditable, and safe.

---

## LLM Integration

- Inference is performed using a Groq-hosted LLM (LLaMA-3.1 family)
- API-based inference ensures low latency and reliability
- The LLM component is modular and can be replaced without changing the RAG pipeline

---

## Edge Case Handling

The system explicitly handles failure scenarios:
- No relevant retrieval results in a clear “information not available” response
- Partially supported questions are answered only where context exists
- Out-of-scope queries are safely refused

---

## Evaluation Results

The system was evaluated using a small set of representative questions:

| Question | Coverage | Result |
|--------|---------|--------|
| What is the refund policy? | Fully answerable | ✅ |
| Can an order be cancelled after shipping? | Fully answerable | ✅ |
| Are international returns supported? | Not covered | ❌ (Correct refusal) |
| Is there a cancellation fee for bulk orders? | Partially covered | ⚠️ |
| What payment methods are supported? | Not covered | ❌ |

Legend:
- ✅ Correct and grounded  
- ⚠️ Partially supported  
- ❌ Information unavailable (hallucination avoided)

---

## Trade-offs and Future Improvements

Trade-offs:
- Smaller chunk sizes improve retrieval precision but increase embedding count
- Limiting retrieval to top-k reduces hallucinations but may omit weaker signals
- Strict refusal behavior improves safety but may reduce perceived completeness

Future improvements:
- Automated evaluation with labeled QA pairs
- Support for PDF and HTML document ingestion
- Re-ranking of retrieved chunks
- Multi-turn conversational memory

---

## Tech Stack

- Python
- LangChain
- Sentence Transformers
- ChromaDB
- Groq API
- Streamlit
- Hugging Face Spaces

---

## What This Project Demonstrates

- Practical understanding of Retrieval-Augmented Generation
- Prompt engineering for hallucination control
- Evaluation-driven LLM development
- Real-world deployment and debugging experience
- Clean, modular system design

---
