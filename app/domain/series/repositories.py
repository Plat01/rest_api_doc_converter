from abc import ABC, abstractmethod
from fastapi import UploadFile
from .entities import Series, SeriesCreate
from app.domain.documents.entities import Document

class SeriesRepository(ABC):
    @abstractmethod
    async def create_series(self, series: SeriesCreate) -> Series:
        pass

    @abstractmethod
    async def get_all_series(self) -> list[Series]:
        pass

    @abstractmethod
    async def upload_document(self, series_id: str, file: UploadFile) -> Document:
        pass

    @abstractmethod
    async def get_series_documents(self, series_id: str) -> list[Document]:
        pass
    