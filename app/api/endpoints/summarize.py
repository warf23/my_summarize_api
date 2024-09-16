# app/api/endpoints/summarize.py

from fastapi import APIRouter, HTTPException
from app.models.requests import SummarizeRequest
from app.utils.validators import validate_language
from app.core.config import settings
from app.services.summarization import summarize_content
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/summarize")
async def summarize(request: SummarizeRequest):
  logger.info("Received summarize request with URL: %s and Language: %s", request.url, request.language)
  
  validate_language(request.language, settings.language_codes)

  try:
      summary = await summarize_content(
          groq_api_key=request.groq_api_key,
          url=str(request.url),  # Ensure 'url' is a string
          language=request.language,
          language_codes=settings.language_codes
      )
      logger.info("Summary generated successfully for URL: %s", request.url)
      return {"summary": summary}
  except HTTPException as he:
      logger.error("HTTP Exception: %s", he.detail)
      raise he
  except Exception as e:
      logger.error("Unexpected error: %s", str(e))
      raise HTTPException(status_code=500, detail="An unexpected error occurred.")