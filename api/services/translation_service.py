import os
from openai import OpenAI

def translate_text_pipeline(text: str, src_lang: str, tgt_lang: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a translator. Translate from {src_lang} to {tgt_lang}. Return only the translated text."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
