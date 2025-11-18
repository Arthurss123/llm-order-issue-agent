from .base_llm import LLMClient

class resumiragent:
    SYSTEM_PROMPT = (
        "vocÊ resume a reclamação de clientes em uma unica frase simples e objetiva" \
        "sem detalhamento que não seja necessarios"
    )

    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = LLMClient(model = model)

    def run (self, text: str) -> str:
        user_prompt = (
            f"Texto do cliente: \n\"^{text}\"\n\n"
            "Resuma o problema em uma frase curta e objetiva"
             )


        
        result = self.llm.chat(self.SYSTEM_PROMPT, user_prompt)

        return result.lower().strip()
    