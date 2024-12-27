from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AccountModel

blp = Blueprint("accounts", __name__, description="Operation on accounts")

@blp.route("/account")
class AccountList(MethodView):
    def get(self):
        return AccountModel.query.all()

    def post(self, account_data):
        account = AccountModel(**account_data)

        try:
            db.session.add(account)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item into the database")

        return account

@blp.route("/account/<int:account_id>")
class Account(MethodView):
    def get(self, account_id):
        pass

    def put(self, account_data, account_id):
        pass

    def delete(self, account_id):
        pass