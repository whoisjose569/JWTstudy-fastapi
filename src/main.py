from fastapi import FastAPI
from src.controllers.auth import router


app = FastAPI()

app.include_router(router)
