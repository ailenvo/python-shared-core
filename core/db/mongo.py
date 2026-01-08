from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)


class MongoDBContext:
    def __init__(
        self,
        connection_string: str,
        database_name: str,
        min_pool_size: int = 5,
        max_pool_size: int = 20,
    ):
        self.client = AsyncIOMotorClient(
            connection_string,
            minPoolSize=min_pool_size,
            maxPoolSize=max_pool_size,
        )
        self.database: AsyncIOMotorDatabase = self.client[database_name]

    def get_collection(self, name: str) -> AsyncIOMotorCollection:
        return self.database.get_collection(name)

    async def healthcheck(self) -> bool:
        try:
            result = await self.database.command("ping")
            return result.get("ok") == 1
        except Exception:
            return False

    async def close(self) -> None:
        self.client.close()

    async def get_connection_stats(self) -> dict:
        try:
            stats = await self.database.command("serverStatus")
            return stats.get("connections", {})
        except Exception as e:
            raise Exception(f"Cannot get MongoDB stats: {e}")
