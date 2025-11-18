from .SentimentoAgent import SentimentAgent
from .classificadorAgent import AgentClassificador
from .prioridadeAgent import agentePrioridade
from .resumoagent import resumiragent

class coordenador:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.sentimento_agent = SentimentAgent(model = model)
        self.classificador_agent = AgentClassificador(model = model)
        self.prioridade_agent = agentePrioridade(model = model)
        self.resumo_agent = resumiragent(model = model)

    def process(self, text: str) -> dict:
        sentimento = self.sentimento_agent.run(text)
        categoria = self.classificador_agent.run(text)
        urgencia = self.prioridade_agent.run(text)
        resumo = self.resumo_agent.run(text)

        recomendacao = self._recommend_action(sentimento, categoria, urgencia)

        return {
            "sentimento": sentimento,
            "categoria": categoria,
            "urgencia": urgencia,
            "resumo": resumo,
            "recomendacao": recomendacao,
        }
    
    def _recommend_action(self, sentimento: str, categoria: str, urgencia: str) -> str:
        # Regra bem simples para começar
        if urgencia in ["alta", "crítica"]:
            return "Encaminhar para atendimento humano e avaliar compensação."
        if categoria == "atraso":
            return "Analisar histórico do entregador e ajustar previsão de entrega."
        if categoria == "comida fria":
            return "Notificar restaurante e revisar embalagens/procedimentos."
        return "Registrar ocorrência e acompanhar recorrência."