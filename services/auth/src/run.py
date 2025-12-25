from fastapi import FastAPI
from src.api import AuthService
from shared.database import Database
from src.settings import _DB_URL


app = FastAPI()
app.include_router(AuthService().router)

# @app.on_event("startup")
# def startup():
#     Database.init(_DB_URL)