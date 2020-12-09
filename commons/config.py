import secrets
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Cash Back'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 15
    SECRET_KEY: str = secrets.token_urlsafe(32)
    API_V1_STR: str = '/api/v1'
    HOST: str = '0.0.0.0'
    PORT: int = 5000
    DEBUG: bool = True

    # Database
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI')


settings = Settings()
