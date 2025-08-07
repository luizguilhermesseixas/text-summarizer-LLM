# Text Summarizer API - Backend

API para geração de resumos de texto usando OpenAI GPT-3.5-turbo.

## Estrutura do Projeto

```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py              # Configurações da aplicação
│   ├── models/                # Modelos Pydantic
│   │   ├── __init__.py
│   │   └── text_models.py     # Modelos para requisições/respostas
│   ├── services/              # Lógica de negócio
│   │   ├── __init__.py
│   │   └── openai_service.py  # Integração com OpenAI
│   ├── routes/                # Rotas da API (FastAPI)
│   │   ├── __init__.py
│   │   └── text_routes.py     # Endpoints de resumo
│   ├── exceptions/            # Exceções customizadas
│   │   ├── __init__.py
│   │   └── openai_exception.py
│   └── utils/                 # Utilitários
│       ├── __init__.py
│       └── dependencies.py    # Injeção de dependências
├── main.py                    # Aplicação principal FastAPI
├── run.py                     # Script para executar o servidor
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## Configuração

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure a variável de ambiente:

```bash
export OPENAI_API_KEY="sua_chave_api_aqui"
```

## Executando a API

```bash
python run.py
```

A API estará disponível em `http://localhost:8000`

## Endpoints

- `GET /` - Informações da API
- `GET /api/v1/health` - Verificação de saúde
- `POST /api/v1/summarize` - Gera resumo do texto

## Documentação

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Arquitetura

O projeto segue uma arquitetura modular com separação clara de responsabilidades:

- **Models**: Definição dos schemas de dados (Pydantic)
- **Services**: Lógica de negócio e integração com APIs externas
- **Routes**: Endpoints da API (FastAPI)
- **Exceptions**: Tratamento de erros customizados
- **Utils**: Utilitários e injeção de dependências
