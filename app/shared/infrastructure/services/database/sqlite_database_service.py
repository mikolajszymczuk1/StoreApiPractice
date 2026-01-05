from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlmodel import SQLModel

from app.shared.domain.services.database.i_sqlite_database_service import ISQLiteDatabaseService


class SQLiteDatabaseService(ISQLiteDatabaseService):
    _engine: AsyncEngine
    _sessionmaker: async_sessionmaker[AsyncSession]

    def __init__(self, db_url: str, echo: bool = False) -> None:
        self._engine: AsyncEngine = create_async_engine(db_url, echo=echo, future=True)
        self._sessionmaker = async_sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    @property
    def session(self) -> async_sessionmaker[AsyncSession]:
        return self._sessionmaker

    async def init_models(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def dispose(self) -> None:
        await self._engine.dispose()

    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        async with self._sessionmaker() as session:
            try:
                yield session
            finally:
                pass
