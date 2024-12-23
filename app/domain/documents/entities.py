from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class DocumentStatus(str, Enum):
    PENDING = "pending"
    CONVERTING = "converting"
    COMPLETED = "completed"
    FAILED = "failed"

class Document(BaseModel):
    id: str
    series_id: str
    original_filename: str
    status: DocumentStatus
    created_at: datetime
    converted_at: Optional[datetime] = None
    file_url: Optional[str] = None 