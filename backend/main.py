from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import Config
from app.routes import text_router

# Valida configurações
Config.validate()

# Criação da aplicação FastAPI
app = FastAPI(
    title="Text Summarizer API",
    description="API para geração de resumos de texto usando OpenAI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(text_router)

@app.get("/")
def read_root():
    """
    Endpoint raiz da API
    """
    return {
        "message": "API do Resumidor de Texto está no ar!",
        "version": "1.0.0",
        "docs": "/docs"
    }