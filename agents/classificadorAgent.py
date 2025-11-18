from .base_llm import LLMClient

categorias = [
    "atraso",
    "comida fria",
    "embalagem",
    "preço",
    "pedido errado",
    "entrega",
    "outro",
]

class AgentClassificador:
    SYSTEM_PROMPT = (
        "Você é um classifacodr de problemas de delivery" \
        "vocÊ deve responder apenas com uma das categorais:" \
        "atraso, comida fria, embalagem, preço, pedido errado, entrega, outro" \
        "se tiver mais que um dos problemas, selecione apenas um principal"
    )

    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = LLMClient(model = model)
    
    def run(self, text: str) -> str:
        user_prompt = (
            f"texto do cliente:\n\"{text}\"\n\n"
            f"Qual a categoria do problema?\n"
            f"opções: {', '.join(categorias)}"
        )

        result = self.llm.chat(self.SYSTEM_PROMPT, user_prompt)
        return result.lower().strip()