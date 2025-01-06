import os
from flask import Flask
from flask_smorest import Api
from db import db

from resources.accounts import blp as AccountsBlueprint
from resources.deposits import blp as DepositsBlueprint

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Banking API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"

    db.init_app(app)

    api = Api(app)

    api.register_blueprint(AccountsBlueprint)
    api.register_blueprint(DepositsBlueprint)

    with app.app_context():
        db.create_all()


    return app


    