from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select

# Custom modules
from src.models import User
from src.schemas import CreateUser
from src.utils import hash_password
from shared.database import get_db


class AuthService:
    """A simple authentication service."""

    def __init__(self):
        self.router = APIRouter(prefix="/auth", tags=["authentication"])

        @self.router.get("/health")
        async def health(db: AsyncSession = Depends(get_db)):
            result = await db.execute(text("SELECT 1;"))
            return {"status": result.scalar()}

        @self.router.post("/register")
        async def register(data: CreateUser, db: AsyncSession = Depends(get_db)):

            # Check if user exist with email
            result = await db.execute(
                select(User).where(User.email == data.email)
            )
            existig_email = result.scalar_one_or_none()
            if existig_email:
                raise HTTPException(400, detail="Email already registered.")
            hashed_password = hash_password(data.password)
            new_user = User(
                fullname=data.fullname,
                age=data.age,
                email=data.email,
                password=hashed_password,
                job_title=data.job_title,
                years_of_experience=data.years_of_experience
            )
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            return {"status": 201, "detail": "User created"}