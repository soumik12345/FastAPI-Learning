from fastapi import FastAPI
from .api import ping


backend = FastAPI()


backend.include_router(ping.router)
