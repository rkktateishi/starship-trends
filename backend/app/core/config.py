import os

class Settings:
    PROJECT_NAME: str = "Starship Cos Trends"
    PROJECT_VERSION: str = "1.0.0"
    
    # Database Config
    SWAPI_URL: str = os.getenv("SWAPI_URL")
    REDIS: str = os.getenv("REDIS")
    DEFAULT_TTL: int = os.getenv("DEFAULT_TTL", 5 * 60) # Default TTL in seconds


settings = Settings()