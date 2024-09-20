from fastapi import APIRouter

from app.dts import (
    Name,
    Email,
)
from app.clients.scraper import ScraperClient

router = APIRouter()


@router.get("/user/name", tags=['user'])
async def get_user_name() -> Name:
    async with ScraperClient() as client:
        name: dict = await client.get_user_name()
    return Name(**name)


@router.get("/user/email", tags=['user'])
async def get_user_email() -> Email:
    async with ScraperClient() as client:
        email: dict = await client.get_user_email()
    return Email(**email)
