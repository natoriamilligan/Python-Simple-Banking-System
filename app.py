import os
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api
from db import db

app = Flask(__name__)

def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    api = Api(app)