from typing import Any

from fastapi.exceptions import HTTPException

from app.clients.base import APIClient


class ScraperClient(APIClient):
    def __init__(self):
        super().__init__('https://randomuser.me/api/')
        self.include_query_param = 'inc'

    async def __get_user_data(self, value: str) -> dict[str, Any]:
        response = await self.client.get(
            self.base_url,
            params={self.include_query_param: value}
        )

        if response.status == 200:
            return await response.json()
        else:
            raise HTTPException(response.status, detail="Request failed")

    async def get_user_name(self) -> dict[str, str]:
        data = await self.__get_user_data(value='name')
        return data.get('results')[0].get('name')

    async def get_user_email(self) -> dict[str, str]:
        data = await self.__get_user_data(value='email')
        return data.get('results')[0]
