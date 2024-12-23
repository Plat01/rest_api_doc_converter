from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
from app.infrastructure.repositories.series_repository import PostgresSeriesRepository
from app.services.series_service import SeriesService
from app.services.s3_service import S3Service

async def get_series_service(
    session: AsyncSession = Depends(get_db)
) -> SeriesService:
    repository = PostgresSeriesRepository(session)
    s3_service = S3Service()
    return SeriesService(repository, s3_service) 
