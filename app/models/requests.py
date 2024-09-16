# app/models/requests.py

from pydantic import BaseModel, HttpUrl, Field

class SummarizeRequest(BaseModel):
  groq_api_key: str = Field(..., description="Your GROQ API key")
  url: HttpUrl = Field(..., description="The URL to summarize")
  language: str = Field("English", description="Language of the summary")