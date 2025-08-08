from pydantic import BaseModel, Field
from typing import Literal

class TextRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=10000, description="Text to be summarized")
    summary_type: Literal["small", "medium", "large"] = Field(..., description="Desired summary type")

class SummaryResponse(BaseModel):
    original_text: str
    summary_type: str
    summary: str
    word_count: int 