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
    extra_body={"reasoning": {"enabled": True}}
    )
    return response.choices[0].message.content
