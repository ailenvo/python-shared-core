from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy import text
from db.base import DBContext


class PostgresDBContext(DBContext):
    def __init__(
        self,
        connection_string: str,
        echo: bool = False,
        pool_size: int = 10,
        max_overflow: int = 20,
    ):
        self.engine = create_async_engine(
            connection_string,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self._sessionmaker = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
        )

    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._sessionmaker() as session:
            yield session

    async def healthcheck(self) -> bool:
        try:
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            return True
        except Exception:
            return False

    async def close(self) -> None:
        await self.engine.dispose()
