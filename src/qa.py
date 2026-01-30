import os
from llama_cpp import Llama

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "phi-2.Q4_K_M.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    n_batch=64,
    verbose=False
)

def answer_question(context, question, prompt):
    if context is None:
        return (
            "Answer:\n"
            "The provided documents do not contain this information.\n\n"
            "Evidence:\n"
            "No relevant policy text found.\n\n"
            "Confidence:\n"
            "Low"
        )

    full_prompt = f"""
### Instruction:
You are a policy assistant. Answer the question using ONLY the context below.
If the answer is not present, say so clearly.

### Context:
{context}

### Question:
{question}

### Answer:
"""

    output = llm(
        full_prompt,
        max_tokens=150,
        temperature=0.0,
        stop=["###"]
    )

    return output["choices"][0]["text"].strip()
