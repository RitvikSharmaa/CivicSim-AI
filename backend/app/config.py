from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    # MongoDB
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "civicsim_ai"
    
    # Security
    secret_key: str = "change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # OpenRouter API (optional)
    openrouter_api_key: str = ""
    openrouter_model: str = "arcee-ai/trinity-large-preview:free"
    
    # Demo Mode
    demo_mode: bool = True
    
    # CORS
    allowed_origins: str = "http://localhost:3000"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    
    # Performance optimizations
    enable_caching: bool = True
    cache_ttl: int = 3600  # 1 hour
    max_workers: int = 4
    batch_size: int = 1000
    
    # ML optimizations
    use_gpu: bool = False  # Set to True if GPU available
    model_precision: str = "float32"  # or "float16" for faster inference
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        
    @property
    def mongodb_url(self) -> str:
        """Backward compatibility"""
        return self.mongodb_uri
    
    @property
    def database_name(self) -> str:
        """Backward compatibility"""
        return self.mongodb_db_name
    
    @property
    def cache_ttl_seconds(self) -> int:
        """Backward compatibility"""
        return self.cache_ttl

@lru_cache()
def get_settings():
    return Settings()
