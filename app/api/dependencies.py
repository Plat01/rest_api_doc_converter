from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
from app.infrastructure.repositories.series_repository import PostgresSeriesRepository
from app.services.series_service import SeriesService

async def get_series_service(
    session: AsyncSession = Depends(get_db)
) -> SeriesService:
    repository = PostgresSeriesRepository(session)
    return SeriesService(repository) 