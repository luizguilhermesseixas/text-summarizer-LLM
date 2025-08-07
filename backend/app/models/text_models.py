from pydantic import BaseModel, Field
from typing import Literal

class TextRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=10000, description="Texto para ser resumido")
    summary_type: Literal["pequeno", "medio", "grande"] = Field(..., description="Tipo de resumo desejado")

class SummaryResponse(BaseModel):
    original_text: str
    summary_type: str
    summary: str
    word_count: int 