from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("accounts", __name__, description="Operation on accounts")

        