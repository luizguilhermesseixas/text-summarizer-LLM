from ..services import OpenAIService
from ..config import Config

def get_openai_service() -> OpenAIService:
    """
    Função de dependência para injetar o serviço da OpenAI
    
    Returns:
        Instância do OpenAIService configurada
    """
    return OpenAIService(api_key=Config.OPENAI_API_KEY) 