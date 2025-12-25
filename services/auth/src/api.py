from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from src.models import User
from shared.database import get_db


class AuthService:
    """A simple authentication service."""

    def __init__(self):
        self.router = APIRouter(prefix="/auth", tags=["auth"])

        @self.router.get("/health")
        async def health(db: AsyncSession = Depends(get_db)):
            result = await db.execute(text("SELECT 1;"))
            return {"status": result.scalar()}