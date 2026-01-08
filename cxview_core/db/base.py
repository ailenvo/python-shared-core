# core/db/base.py
from abc import ABC, abstractmethod
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession


class DBContext(ABC):

    @abstractmethod
    async def session(self) -> AsyncGenerator[AsyncSession, None]: ...

    @abstractmethod
    async def healthcheck(self) -> bool: ...

    @abstractmethod
    async def close(self) -> None: ...
