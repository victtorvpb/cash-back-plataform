import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Cash Back'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 15
    SECRET_KEY: str = 'v9la8dfl9t4lSTiMjYetrkF7YxgCFblAEJaU3o2G4cs'
    API_V1_STR: str = '/api/v1'
    HOST: str = '0.0.0.0'
    PORT: int = 5000
    DEBUG: bool = True
    ALGORITHM: str = 'HS512'
    CREDIT_SERVICE_TOKEN: str = 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm&#39'
    FIRST_SUPERUSER: str = 'admin@admin.com'
    FIRST_SUPERUSER_PASSWORD: str = 'admin'

    # Database
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI')


settings = Settings()
