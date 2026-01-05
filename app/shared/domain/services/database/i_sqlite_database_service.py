from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)


class ISQLiteDatabaseService(ABC):
    @property
    @abstractmethod
    def engine(self) -> AsyncEngine: ...

    @property
    @abstractmethod
    def session(self) -> async_sessionmaker[AsyncSession]: ...

    @abstractmethod
    async def init_models(self) -> None: ...

    @abstractmethod
    async def dispose(self) -> None: ...

    @abstractmethod
    def get_session(self) -> AbstractAsyncContextManager[AsyncSession]: ...
