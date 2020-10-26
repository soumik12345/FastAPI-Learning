from fastapi import FastAPI
from .api import ping
from .api.routes import items


backend = FastAPI()


backend.include_router(ping.router)
backend.include_router(items.router)
