from pydantic_settings import BaseSettings

# Configuration settings for the application
# This class uses Pydantic to manage settings and environment variables
class Settings(BaseSettings):
    OPENAI_API_KEY : str
    model: str


    class Config:
        env_file = '.env'
        env_encoding = 'utf-8'
        case_sensitive = True


setting = Settings()
