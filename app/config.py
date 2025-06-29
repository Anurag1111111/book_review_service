from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False") == "True"
    SWAGGER = {
        "title": os.getenv("SWAGGER_TITLE", "Book Review API"),
        "uiversion": int(os.getenv("SWAGGER_UIVERSION", "3"))
    }
    REDIS_URL = os.getenv("REDIS_URL")
