# app/openai_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_chat_completion(prompt: str, system_prompt: str = "You are a beverage formulation expert.") -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
