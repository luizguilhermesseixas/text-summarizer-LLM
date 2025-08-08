from fastapi import APIRouter, HTTPException, Depends
from ..models import TextRequest, SummaryResponse
from ..services import OpenAIService
from ..exceptions import OpenAIException
from ..utils.dependencies import get_openai_service

router = APIRouter(prefix="/api/v1", tags=["text"])

@router.get("/health")
def health_check():
    """
    API health check endpoint
    """
    return {
        "status": "healthy", 
        "message": "API working correctly",
        "version": "1.0.0"
    }

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_text(
    request: TextRequest,
    openai_service: OpenAIService = Depends(get_openai_service)
):
    """
    Generates a summary of the provided text
    
    Args:
        request: Request data containing the text and summary type
        openai_service: OpenAI service injected via dependency
        
    Returns:
        Generated summary with additional information
        
    Raises:
        HTTPException: In case of processing error
    """
    try:
        result = openai_service.generate_summary(
            text=request.text,
            summary_type=request.summary_type
        )
        
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
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}") 