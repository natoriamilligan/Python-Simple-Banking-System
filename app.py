from flask import Flask
from flask_smorest import Api

app = Flask(__name__)

def create_app():
    api = Api(app)