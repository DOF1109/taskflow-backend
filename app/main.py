from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.session import engine
from app.db.base_class import Base
from app.api.v1.api import api_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router, prefix=settings.API_V1_STR)

def create_application() -> FastAPI:
    create_tables()
    application = FastAPI(
        title="TaskFlow API",
        description="A smart task management application with AI-powered features.",
        version="1.0.0",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    include_router(application)
    return application

app = create_application()

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskFlow API"} 