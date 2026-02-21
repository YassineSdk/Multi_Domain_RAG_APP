from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def llm_response(question: str, model: str = "llama-3.3-70b-versatile") -> str:
    key = os.getenv("LLMKEY")
    client = Groq(api_key=key)
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": question}
        ],
        model=model,
    )
    return response.choices[0].message.content
