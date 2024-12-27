from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("transactions", __name__, description="Operation on transactions")