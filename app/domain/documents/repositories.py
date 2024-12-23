from abc import ABC, abstractmethod
from fastapi import UploadFile
from app.domain.documents.entities import Document

class DocumentRepository(ABC):
    @abstractmethod
    async def upload_document(self, series_id: str, file: UploadFile) -> Document:
        pass

    @abstractmethod
    async def get_documents_by_series(self, series_id: str) -> list[Document]:
        pass 