from fastapi import UploadFile
from app.domain.series.repositories import SeriesRepository
from app.domain.series.entities import Series, SeriesCreate
from app.domain.documents.entities import Document

class SeriesService:
    def __init__(self, repository: SeriesRepository):
        self.repository = repository

    async def create_series(self, series: SeriesCreate) -> Series:
        return await self.repository.create_series(series)
    
    async def get_all_series(self) -> list[Series]:
        return await self.repository.get_all_series()

    async def upload_document(self, id: str, file: UploadFile) -> Document:
        return await self.repository.upload_document(id, file)

    async def get_series_documents(self, id: str) -> list[Document | None]:
        return await self.repository.get_series_documents(id)
