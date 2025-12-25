from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from typing import AsyncGenerator, Optional


class Database:
    _engine = None
    _session_factory = None
    _db_url: Optional[str] = None

    @classmethod
    def init(cls, db_url: str):
        """
        Initialize database configuration once (on startup).
        """
        if cls._db_url is None:
            cls._db_url = db_url

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            if cls._db_url is None:
                raise RuntimeError("Database is not initialized. Call Database.init(db_url) first.")

            cls._engine = create_async_engine(
                cls._db_url,
                echo=True,
                pool_pre_ping=True,
                pool_recycle=280,
            )
        return cls._engine

    @classmethod
    def get_session_factory(cls):
        if cls._session_factory is None:
            engine = cls.get_engine()
            cls._session_factory = async_sessionmaker(
                bind=engine,
                autoflush=False,
                autocommit=False,
                expire_on_commit=False,
            )
        return cls._session_factory


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session_factory = Database.get_session_factory()
    async with session_factory() as session:
        yield session