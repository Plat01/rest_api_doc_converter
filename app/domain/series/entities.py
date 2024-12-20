from pydantic import BaseModel, constr
from datetime import datetime

class SeriesCreate(BaseModel):
    name: constr(pattern="^[a-zA-Z0-9-]+$") # type: ignore

class Series(BaseModel):
    id: str
    name: str
    created_at: datetime 