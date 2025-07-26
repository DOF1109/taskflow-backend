from pydantic_settings import BaseSettings
from pydantic import EmailStr

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "a_very_secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///example.db"

    # Email settings
    EMAILS_ENABLED: bool = True
    SMTP_TLS: bool = True
    SMTP_PORT: int = 587
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_USER: str = "your-email@gmail.com"
    SMTP_PASSWORD: str = "your-password"
    EMAILS_FROM_EMAIL: EmailStr = "your-email@gmail.com"
    EMAILS_FROM_NAME: str = "TaskFlow"

    class Config:
        case_sensitive = True

settings = Settings() 