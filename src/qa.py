import os
from groq import Groq

def answer_question(context: str, question: str, prompt_template: str) -> str:
    """
    Generate an answer using Groq LLM based on retrieved context.
    """

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY not found."

    client = Groq(api_key=api_key)

    prompt = prompt_template.format(
        context=context,
        question=question
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a precise policy assistant. Answer strictly from the context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=400
    )

    return response.choices[0].message.content.strip()
