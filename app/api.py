from fastapi import FastAPI
from pydantic import BaseModel
from agents.orquestrador import coordenador

app = FastAPI(
    title="Order Issue LLM Agent API",
    version="0.1.0",
    description="API para classificação automática de problemas em pedidos usando LLM Agents."
)

coordinator = coordenador()

class IssueInput(BaseModel):
    text: str

@app.post("/classify")
def classify_issue(payload: IssueInput):
    """
    Recebe a reclamação do cliente em texto livre
    e retorna um JSON estruturado com sentimento, categoria, urgência, resumo e recomendação.
    """
    result = coordinator.process(payload.text)
    return result

@app.get("/ping")
def ping():
    return {"status": "ok"}
