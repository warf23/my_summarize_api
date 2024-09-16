# app/api/endpoints/summarize.py
from fastapi import APIRouter, Depends
from app.models.requests import SummarizeRequest
from app.utils.validators import validate_url, validate_language
from app.core.config import settings
from app.services.summarization import summarize_content

from fastapi import HTTPException

router = APIRouter()

@router.post("/summarize")
async def summarize(request: SummarizeRequest):
  validate_url(request.url)
  validate_language(request.language, settings.language_codes)

  try:
      summary = await summarize_content(
          groq_api_key=request.groq_api_key,
          url=request.url,
          language=request.language,
          language_codes=settings.language_codes
      )
      return {"summary": summary}
  except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")