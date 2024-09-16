# app/utils/validators.py
import validators
from fastapi import HTTPException



def validate_url(url: str):
  if not validators.url(url):
      raise HTTPException(status_code=400, detail="Invalid URL")

def validate_language(language: str, language_codes: dict):
  if language not in language_codes:
      raise HTTPException(status_code=400, detail="Invalid language")