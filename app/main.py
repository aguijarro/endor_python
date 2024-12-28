from fastapi import FastAPI, Depends
from app.core.config import get_settings, Settings

app = FastAPI()


@app.get("/health")
async def health(settings: Settings = Depends(get_settings)):
    return {"status": "healthy!"}

