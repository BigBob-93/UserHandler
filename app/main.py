from fastapi import FastAPI

from app.api import router

fastapi_app = FastAPI()
fastapi_app.include_router(router=router)
