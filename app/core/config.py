from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET: str
    SQS_QUEUE_URL: str

    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = '0000'
    POSTGRES_DB: str = 'docs_db'
    DATABASE_URL: str = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'
    
    class Config:
        env_file = ".env"
        extra = 'allow'

settings = Settings() 
