from fastapi import UploadFile
from app.domain.series.repositories import SeriesRepository
from app.domain.series.entities import Series, SeriesCreate
from app.domain.documents.entities import Document
from app.services.s3_service import S3Service
from app.core.config import settings

class SeriesService:
    def __init__(self, repository: SeriesRepository, s3_service: S3Service):
        self.repository = repository
        self.s3_service = s3_service

    async def create_series(self, series: SeriesCreate) -> Series:
        return await self.repository.create_series(series)
    
    async def get_all_series(self) -> list[Series]:
        return await self.repository.get_all_series()

    async def upload_document(self, id: str, file: UploadFile) -> Document:
        """Add document to S3 and save document metadata in the database

        Args:
            id (str): document id
            file (UploadFile): document file

        Returns:
            Document: document with file_url
        """

        try:
            file_url = self.s3_service.upload_file(file, settings.S3_BUCKET)
        except Exception as e:
            # raise HTTPException(status_code=500, detail=f"Failed to upload file to S3: {str(e)}")  # TODO: dont'work now (hav no access to aws)
            print(f"Failed to upload file to S3: {str(e)}")
            file_url = None

        document = await self.repository.upload_document(id, file)
        document.file_url = file_url
        return document

    async def get_series_documents(self, id: str) -> list[Document | None]:
        return await self.repository.get_series_documents(id)
