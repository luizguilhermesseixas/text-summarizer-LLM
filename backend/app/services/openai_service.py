import openai
from typing import Dict, Any
from ..exceptions.openai_exception import OpenAIException

class OpenAIService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key
        
        # Configuração dos prompts por tipo de resumo
        self.size_prompts = {
            "pequeno": "Faça um resumo muito conciso, com no máximo 50 palavras.",
            "medio": "Faça um resumo moderado, com aproximadamente 100-150 palavras.",
            "grande": "Faça um resumo detalhado, com aproximadamente 200-300 palavras."
        }
    
    def generate_summary(self, text: str, summary_type: str) -> Dict[str, Any]:
        """
        Gera um resumo do texto usando a API da OpenAI
        
        Args:
            text: Texto original para ser resumido
            summary_type: Tipo de resumo (pequeno, medio, grande)
            
        Returns:
            Dicionário com o resumo e informações adicionais
        """
        try:
            if summary_type not in self.size_prompts:
                raise ValueError(f"Tipo de resumo inválido: {summary_type}")
            
            prompt = self._build_prompt(text, summary_type)
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "Você é um assistente especializado em criar resumos claros e precisos de textos."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            summary = response.choices[0].message.content.strip()
            word_count = len(summary.split())
            
            return {
                "summary": summary,
                "word_count": word_count,
                "model_used": "gpt-3.5-turbo"
            }
            
        except Exception as e:
            raise OpenAIException(f"Erro ao gerar resumo: {str(e)}")
    
    def _build_prompt(self, text: str, summary_type: str) -> str:
        """
        Constrói o prompt para a API da OpenAI
        
        Args:
            text: Texto original
            summary_type: Tipo de resumo
            
        Returns:
            Prompt formatado
        """
        return f"""
        {self.size_prompts[summary_type]}
        
        Texto original:
        {text}
        
        Resumo:
        """ 