import os
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api
from db import db

from resources.accounts import blp as AccountsBlueprint
from resources.transactions import blp as TransactionsBlueprint

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Banking API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)

    api = Api(app)

    api.register_blueprint(AccountsBlueprint)
    api.register_blueprint(TransactionsBlueprint)

    with app.app_context():
        db.create_all()


    return app


    