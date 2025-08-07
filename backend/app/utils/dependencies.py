from ..services import OpenAIService
from ..config import Config

def get_openai_service() -> OpenAIService:
    return OpenAIService(api_key=Config.OPENAI_API_KEY) 