# Environment variables and configurations

from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI App"
    DEBUG: bool = False
    DATABASE_URL: str
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings() 