# LLM Agent – Classificação Automática de Problemas em Pedidos

Sistema inteligente baseado em modelos de Linguagem (LLMs) para analisar reclamações de clientes em texto livre, classificando automaticamente sentimento, categoria do problema, urgência, resumo e recomendação.  
O projeto é voltado para plataformas de delivery, SAC, monitoramento de satisfação e automação de atendimento.

---

# 2. Índice

- [1. Índice](#2-índice)
- [2. Visão Geral](#3-visão-geral)
- [3. Pré-requisitos](#3-pré-requisitos)
- [4. Instalação](#4-instalação)
- [5. Uso](#5-uso)
- [6. Configuração](#6-configuração)
- [7. Estrutura do Projeto](#9-estrutura-do-projeto)
- [8. Como Contribuir](#10-como-contribuir)
- [9. Licença](#11-licença)

---

# 2. Visão Geral

Este projeto implementa um sistema multi-agente utilizando LLMs para análise automática de reclamações de clientes.

### Principais Funcionalidades

- **Análise de Sentimento**  
  Detecta se o cliente está positivo, neutro ou negativo.

- **Classificação de Problemas**  
  Identifica o tipo principal da reclamação: atraso, comida fria, embalagem, preço, pedido errado, entrega.

- **Avaliação de Urgência**  
  Define criticidade: baixa, média, alta ou crítica.

- **Resumo Automático**
  Gera uma frase curta descrevendo o problema.

- **Recomendação Automática**
  Sugere ação operacional com base no contexto.


# 3. Pré-requisitos 

- OpenAI GPT (LLM)
- FastAPI
- Python
- Docker (opcional)
- pytest para testes

# 4. Instalação
1 - Clone o repositorio
 ```bash
git clone https://github.com/seu-usuario/llm-agent-order-issues.git
cd llm-agent-order-issues
 ```


2 - Crie o ambiente virtual

```bash
python -m venv venv
venv/bin/activate
```

3 - Instale as dependências

```bash
pip install requirements.txt
```
4 - Configure sua chave de API
```bash
OPENAI_API_KEY = "chave_api"
```

# 5. Uso

 - Rode a Api
```bash
python main.py
```

- Acesse a doc interativa

```bash
http://0.0.0.0:8000/docs
```
- Exemplo de request

```bash
{
  "text": "Meu pedido atrasou 50 minutos e ainda chegou frio."
}
```

# 6. Configuração

- crie um arquivo .env na raiz contendo

```bash
OPENAI_API_KEY= "chave_api
```
- É gerado um exemplo em:
```bash
.env.example
```
# 7. Estrutura do projeto

```bash
├── agents/
│   ├── base_llm.py
│   ├── classifier_agent.py
│   ├── sentiment_agent.py
│   ├── priority_agent.py
│   ├── summarizer_agent.py
│   └── coordinator.py
│
├── app/
│   ├── api.py
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── main.py
└── README.md

 ```

# 8. Como contribuir com o projeto?

- 1 Realize uma fork do projeto

- 2 Crie um branch seguindo esse padrão:

```bash
feature/nome-da-feature
fix/nome-do-fix
doc/ajuste-documentacao
```
- 3 Faça commits semânticos

- 4 Envie uma Pull Request detalhando a mudança

# 9. Licença
Este projeto está licenciado sob MIT License
Arquivo disponivel em: LICENSE.MD

