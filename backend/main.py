from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import Config
from app.routes import text_router

Config.validate()

app = FastAPI(
    title="Text Summarizer API",
    description="API for text summarization using OpenAI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text_router)

@app.get("/")
def read_root():
    """
    Root endpoint of the API
    """
    return {
        "message": "Text Summarizer API is running!",
        "version": "1.0.0",
        "docs": "/docs"
    }