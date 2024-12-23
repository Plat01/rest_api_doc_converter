from fastapi import FastAPI
from sqlalchemy import create_engine
from app.api.routes import series
from app.infrastructure.models import Base
from app.core.config import settings

app = FastAPI(title="Document Conversion System")


# # TODO: create database with alembic
# sync_engine = create_engine(settings.DATABASE_URL.replace('postgresql+asyncpg', 'postgresql'))
# Base.metadata.create_all(bind=sync_engine)

app.include_router(series.router, prefix="/api", tags=["series"])
