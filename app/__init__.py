
from flask import Flask
from app.db import db, migrate
from app.views import api
from app.cache import init_redis
from flasgger import Swagger
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)
    api.init_app(app)

    with app.app_context():
        init_redis()

    return app
app = create_app()
