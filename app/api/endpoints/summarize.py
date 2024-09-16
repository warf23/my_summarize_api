   # app/api/endpoints/summarize.py
from fastapi import APIRouter, Depends, HTTPException
from app.models.requests import SummarizeRequest
from app.utils.validators import validate_url, validate_language
from app.core.config import settings
from app.services.summarization import summarize_content
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/summarize")
async def summarize(request: SummarizeRequest):
       logger.info("Received summarize request: %s", request)
       
       
       validate_language(request.language, settings.language_codes)

       try:
           summary = await summarize_content(
               groq_api_key=request.groq_api_key,
               url=request.url,
               language=request.language,
               language_codes=settings.language_codes
           )
           logger.info("Summary generated successfully.")
           return {"summary": summary}
       except Exception as e:
           logger.error("Error during summarization: %s", str(e))
           raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")