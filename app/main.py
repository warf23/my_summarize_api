# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import summarize

app = FastAPI()

# Add CORS middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Adjust as needed for security
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Include API routes
app.include_router(summarize.router)

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="127.0.0.1", port=8000 , reload=True)