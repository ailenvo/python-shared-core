import os

from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", default="DEV")
PORT = os.getenv("PORT", default="8000")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# SECRET KEY
SECRET_KEY = os.getenv("SECRET_KEY")
INTERNAL_SECRET_KEY = os.getenv("INTERNAL_SECRET_KEY")

# Database
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
BD_NAME = os.getenv("BD_NAME")

# REDIS
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DATABASE = os.getenv("REDIS_DATABASE")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
