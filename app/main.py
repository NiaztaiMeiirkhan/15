from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to FastAPI Config App",
        "database_url": settings.database_url,
        "redis_host": settings.redis_host,
    }
