from .base_llm import LLMClient

class SentimentAgent:
    SYSTEM_PROMPT = (
        "você é um analisador de sentimentso de reclamções de clientes"
        "Responda APENAS com uma das opções: positivos, neutro ou negativo"
    )

    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = LLMClient(model = model)

    def run (self, text: str) -> str:
        user_prompt = f"Texto do cliente: \n\"^{text}\"\n\nQual é o sentimento?"
        result = self.llm.chat(self.SYSTEM_PROMPT, user_prompt)

        return result.lower().strip()
    
    