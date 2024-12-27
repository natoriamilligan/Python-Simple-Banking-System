from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("accounts", __name__, description="Operation on accounts")

@blp.route("/account")
class AccountList(MethodView):
    def get(self):
        pass

    def post(self, account_data):
        pass

@blp.route("/account/<int:account_id>")
class Account(MethodView):
    def get(self, account_id):
        pass

    def put(self, account_data, account_id):
        pass

    def delete(self, account_id):
        pass