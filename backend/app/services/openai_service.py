import openai
from typing import Dict, Any
from ..exceptions.openai_exception import OpenAIException

class OpenAIService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key
        
        self.size_prompts = {
            "small": "Make a very concise summary, with a maximum of 50 words.",
            "medium": "Make a moderate summary, with approximately 100-150 words.",
            "large": "Make a detailed summary, with approximately 200-300 words."
        }
    
    def generate_summary(self, text: str, summary_type: str) -> Dict[str, Any]:
        """
        Generates a summary of the text using the OpenAI API
        
        Args:
            text: Original text to be summarized
            summary_type: Summary type (small, medium, large)
            
        Returns:
            Dictionary with the summary and additional information
        """
        try:
            if summary_type not in self.size_prompts:
                raise ValueError(f"Invalid summary type: {summary_type}")
            
            prompt = self._build_prompt(text, summary_type)
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an assistant specialized in creating clear and accurate text summaries."
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
            raise OpenAIException(f"Error generating summary: {str(e)}")
    
    def _build_prompt(self, text: str, summary_type: str) -> str:
        """
        Builds the prompt for the OpenAI API
        
        Args:
            text: Original text
            summary_type: Summary type
            
        Returns:
            Formatted prompt
        """
        return f"""
        {self.size_prompts[summary_type]}
        
        Original text:
        {text}
        
        Summary:
        """ 