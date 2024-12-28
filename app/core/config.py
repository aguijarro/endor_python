# Environment variables and configurations
import logging

from functools import lru_cache
from typing import List
from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI App"
    DEBUG: bool = False
    DATABASE_URL: AnyUrl = None
    ALLOWED_ORIGINS: str = "http://localhost:3000"
    ENVIRONMENT: str = "development"
    
    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
    
    @property
    def env_file(self) -> str:
        return f"infrastructure/docker/{self.ENVIRONMENT}/.env.{self.ENVIRONMENT}"
    
    class Config:
        env_file = ".env.development"

@lru_cache
def get_settings() -> Settings:
    return Settings() 