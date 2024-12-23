from pydantic import BaseModel, Field, constr
from datetime import datetime
from app.domain.documents.entities import Document

class SeriesCreate(BaseModel):
    name: constr(pattern="^[a-zA-Z0-9-]+$") # type: ignore

class Series(BaseModel):
    id: str
    name: str
    created_at: datetime
    documents: list[Document] = Field(default_factory=list)
    