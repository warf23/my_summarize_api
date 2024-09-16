# app/core/config.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
  groq_api_key: str
  language_codes: dict = {
      'English': 'en',
      'Arabic': 'ar',
      'Spanish': 'es',
      'French': 'fr',
      'German': 'de',
      'Italian': 'it',
      'Portuguese': 'pt',
      'Chinese': 'zh',
      'Japanese': 'ja',
      'Korean': 'ko'
  }

  class Config:
      env_file = ".env"

settings = Settings()