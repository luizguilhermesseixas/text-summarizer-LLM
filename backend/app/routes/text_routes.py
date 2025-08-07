from fastapi import APIRouter, HTTPException, Depends
from ..models import TextRequest, SummaryResponse
from ..services import OpenAIService
from ..exceptions import OpenAIException
from ..utils.dependencies import get_openai_service

router = APIRouter(prefix="/api/v1", tags=["text"])

@router.get("/health")
def health_check():
    """
    Endpoint de verificação de saúde da API
    """
    return {
        "status": "healthy", 
        "message": "API funcionando corretamente",
        "version": "1.0.0"
    }

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_text(
    request: TextRequest,
    openai_service: OpenAIService = Depends(get_openai_service)
):
    """
    Gera um resumo do texto fornecido
    
    Args:
        request: Dados da requisição contendo o texto e tipo de resumo
        openai_service: Serviço da OpenAI injetado via dependência
        
    Returns:
        Resumo gerado com informações adicionais
        
    Raises:
        HTTPException: Em caso de erro no processamento
    """
    try:
        # Gera o resumo usando o serviço
        result = openai_service.generate_summary(
            text=request.text,
            summary_type=request.summary_type
        )
        
        # Retorna a resposta formatada
        return SummaryResponse(
            original_text=request.text,
            summary_type=request.summary_type,
            summary=result["summary"],
            word_count=result["word_count"]
        )
        
    except OpenAIException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}") 