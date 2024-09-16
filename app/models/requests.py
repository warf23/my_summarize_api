# app/models/requests.py
from pydantic import BaseModel

class SummarizeRequest(BaseModel):
  groq_api_key: str
  url: str
  language: str = "English"