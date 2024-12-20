from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile
from app.domain.series.repositories import SeriesRepository
from app.domain.series.entities import Series, SeriesCreate
from app.domain.documents.entities import Document

class PostgresSeriesRepository(SeriesRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_series(self, series: SeriesCreate) -> Series:
        # Implementation will come later
        pass

    async def get_all_series(self) -> list[Series]:
        # Implementation will come later
        pass

    async def upload_document(self, series_id: str, file: UploadFile) -> Document:
        # Implementation will come later
        pass

    async def get_series_documents(self, series_id: str) -> list[Document]:
        # Implementation will come later
        pass 