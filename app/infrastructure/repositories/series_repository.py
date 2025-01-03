from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import UploadFile
import uuid
import datetime

from app.domain.series.repositories import SeriesRepository
from app.domain.series.entities import Series, SeriesCreate
from app.domain.documents.entities import Document
from app.infrastructure.models import SeriesModel, DocumentModel
from app.domain.documents.entities import Document, DocumentStatus


class PostgresSeriesRepository(SeriesRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_series(self, series: SeriesCreate) -> Series:
        new_series = SeriesModel(id=series.name, name=series.name)
        self.session.add(new_series)
        await self.session.commit()
        await self.session.refresh(new_series)
        return Series(id=new_series.id, name=new_series.name, created_at=new_series.created_at)

    async def get_all_series(self) -> list[Series]:
        result = await self.session.execute(select(SeriesModel).options(selectinload(SeriesModel.documents)))
        series_list = result.scalars().all()
        return [
            Series(
                id=s.id,
                name=s.name,
                created_at=s.created_at,
                documents=[
                    Document(
                        id=d.id,
                        series_id=d.series_id,
                        original_filename=d.original_filename,
                        status=d.status,
                        created_at=d.created_at,
                        converted_at=d.converted_at
                    ) for d in s.documents
                ]
            ) for s in series_list
        ]

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

    async def get_series_documents(self, series_id: str) -> list[Document | None]:
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