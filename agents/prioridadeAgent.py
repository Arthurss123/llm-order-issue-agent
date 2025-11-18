from .base_llm import LLMClient


niveis = ["baixa", "média", "alta", "critica"]

class agentePrioridade:
    SYSTEM_PROMPT = (
        "vocÊ decide a urgencia de um problema em um pedido de delivery" \
        "considere atraso grande, comida estragada como mais graves"
        "respoda apenas com: Baixa, média, alta ou critica"
    )

    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = LLMClient(model = model)

    def run (self, text: str) -> str:
        user_prompt = f"Texto do cliente: \n\"^{text}\"\n\nqual o nivel de urgencia?"
        result = self.llm.chat(self.SYSTEM_PROMPT, user_prompt)

        return result.lower().strip()