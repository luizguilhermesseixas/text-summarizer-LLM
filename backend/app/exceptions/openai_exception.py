class OpenAIException(Exception):
    """Custom exception for errors related to the OpenAI API"""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message) 