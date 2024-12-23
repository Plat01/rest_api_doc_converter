from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import UploadFile
from app.domain.documents.repositories import DocumentRepository
from app.domain.documents.entities import Document, DocumentStatus
from app.infrastructure.models import DocumentModel
import uuid
import datetime

class PostgresDocumentRepository(DocumentRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upload_document(self, series_id: str, file: UploadFile) -> Document:
        document_id = str(uuid.uuid4())
        original_filename = file.filename

        new_document = DocumentModel(
            id=document_id,
            series_id=series_id,
            original_filename=original_filename,
            status=DocumentStatus.PENDING,
            created_at=datetime.datetime.utcnow()
        )

        self.session.add(new_document)
        await self.session.commit()
        await self.session.refresh(new_document)

        return Document(
            id=new_document.id,
            series_id=new_document.series_id,
            original_filename=new_document.original_filename,
            status=new_document.status,
            created_at=new_document.created_at,
            converted_at=new_document.converted_at
        )

    async def get_documents_by_series(self, series_id: str) -> list[Document | None]:
        result = await self.session.execute(select(DocumentModel).where(DocumentModel.series_id == series_id))
        document_list = result.scalars().all()

        if document_list:
            return [
                Document(
                    id=d.id,
                    series_id=d.series_id,
                    original_filename=d.original_filename,
                    status=d.status,
                    created_at=d.created_at,
                    converted_at=d.converted_at
                ) for d in document_list
            ]
        
        return []
    