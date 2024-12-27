import os
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api
from db import db

from resources.accounts import blp as AccountsBlueprint
from resources.transactions import blp as TransactionsBlueprint

load_dotenv()

app = Flask(__name__)

def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)

    api = Api(app)

    api.register_blueprint(AccountsBlueprint)
    api.register_blueprint(TransactionsBlueprint)

    with app.app_context():
        db.create_all()

    return app
    