class OpenAIException(Exception):
    """Exceção customizada para erros relacionados à API da OpenAI"""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message) 