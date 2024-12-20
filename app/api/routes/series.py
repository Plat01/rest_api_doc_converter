from fastapi import APIRouter, Depends, UploadFile, File
from typing import List
from app.services.series_service import SeriesService
from app.domain.series.entities import SeriesCreate, Series
from app.domain.documents.entities import Document
from app.api.dependencies import get_series_service

router = APIRouter()

@router.post("/series", response_model=Series)
async def create_series(
    series: SeriesCreate,
    service: SeriesService = Depends(get_series_service)
):
    return await service.create_series(series)

@router.get("/series", response_model=List[Series])
async def get_series(
    service: SeriesService = Depends(get_series_service)
):
    return await service.get_all_series()

@router.post("/series/{id}/documents")
async def upload_document(
    id: str,
    file: UploadFile = File(...),
    service: SeriesService = Depends(get_series_service)
):
    return await service.upload_document(id, file)

@router.get("/series/{id}/documents", response_model=List[Document])
async def get_documents(
    id: str,
    service: SeriesService = Depends(get_series_service)
):
    return await service.get_series_documents(id) 