from abc import ABC
from aiohttp import ClientSession


class APIClient(ABC):
    def __init__(self, base_url: str):
        self.base_url: str = base_url

    async def __aenter__(self) -> 'APIClient':
        self.client = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        await self.client.close()
