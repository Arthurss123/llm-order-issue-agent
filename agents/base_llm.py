import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class LLMClient:
    def __init__(self, model: str = "gpt-4o-mini"):
        api_key = os.getenv("OPENAI-API-KEY")
        self.client = OpenAI(api_key= api_key)
        self.model = model

    def chat (self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model = self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": user_prompt},
            ],

            temperature=0.2,
        )
        return response.choices[0].message.content.strip()