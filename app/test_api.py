import pytest
from httpx import AsyncClient

from app.main import fastapi_app


@pytest.mark.asyncio
async def test_get_name():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        response = await ac.get("/user/name")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_email():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        response = await ac.get("/user/email")
    assert response.status_code == 200
