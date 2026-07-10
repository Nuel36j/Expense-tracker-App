"""
Centralized application settings.
Pulls values from environment variables / .env file so nothing
sensitive (DB URL, secret key) is hardcoded in source.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- App ---
    APP_NAME: str = "Expense Tracker API"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = False

    # --- Database ---
    DATABASE_URL: str = "sqlite:///./expense_tracker.db"

    # --- Auth / JWT ---
    SECRET_KEY: str = "df5067cbc4519a90a04114536551eecefb0fd5b96269181e9ef6249784ab6a52"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Single shared settings instance — import this everywhere else
settings = Settings()
