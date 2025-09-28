import os

from fastapi import FastAPI

from app.api import transcripts

app = FastAPI()

app.include_router(transcripts.router, prefix="/transcripts", tags=["transcripts"])

if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))

    uvicorn.run(app, host=host, port=port)
