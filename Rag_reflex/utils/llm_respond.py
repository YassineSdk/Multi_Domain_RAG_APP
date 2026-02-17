from openai import OpenAI 



def llm_response(question):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )
    response = client.chat.completions.create(
    model="openrouter/aurora-alpha",
    messages=[
        {"role": "assistant", "content": question}
    ],
    extra_body={"reasoning": {"enabled": True}}  # enables step-by-step reasoning
    )
    return response.choices[0].message
