from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base
from app.domain.documents.entities import DocumentStatus

Base = declarative_base()

class SeriesModel(Base):
    __tablename__ = 'series'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    documents = relationship("DocumentModel", back_populates="series")

class DocumentModel(Base):
    __tablename__ = 'documents'

    id = Column(String, primary_key=True, index=True)
    series_id = Column(String, ForeignKey('series.id'), nullable=False)
    original_filename = Column(String)
    status = Column(Enum(DocumentStatus), default=DocumentStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    converted_at = Column(DateTime(timezone=True), nullable=True)

    series = relationship("SeriesModel", back_populates="documents") 
    