from fastapi import FastAPI
from app.api.routes import series

app = FastAPI(title="Document Conversion System")

app.include_router(series.router, prefix="/api", tags=["series"])
