'''
Configuration management for the Essay Writer application
Handles environment variables and application settings.
'''

from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Model Configuration
    base_url: str = Field("", env="BASE_URL")
    model_name: str = Field("gpt-3.5-turbo", env="MODEL_NAME")
    api_key: str = Field(..., env="API_KEY")

    # Tavily configuration
    tavily_api_key: str = Field(..., env="TAVILY_API_KEY")

    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()

def get_settings() -> Settings:
    """Get application settings instance."""
    return settings
