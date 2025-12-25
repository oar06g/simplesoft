from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator 
from sqlalchemy.ext.asyncio import AsyncEngine
from contextlib import asynccontextmanager

from src.api import AuthService
from shared.database import Database
from src.models import Base
from src.settings import _DB_URL


@asynccontextmanager
async def lifespan(app: FastAPI):
    Database.init(_DB_URL)
    engine: AsyncEngine = Database.get_engine()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose

app = FastAPI( debug=True, title="Simplesoft", version="0.1.0", lifespan=lifespan )
Instrumentator().instrument(app).expose(app)
app.include_router(AuthService().router)
