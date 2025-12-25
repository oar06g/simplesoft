import os
from dotenv import load_dotenv

load_dotenv()
# Database information
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORTS = os.getenv("DB_PORTS")
DB_NAME = os.getenv("DB_NAME")

_DB_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORTS}/{DB_NAME}"