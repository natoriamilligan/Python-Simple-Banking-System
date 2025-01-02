from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AccountModel
from schemas import AccountSchema, UpdateAccountSchema

blp = Blueprint("accounts", __name__, description="Operation on accounts")

@blp.route("/account")
class AccountList(MethodView):
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()

    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, account_data):
        if AccountModel.query.filter(AccountModel.username == account_data["username"]).first():
                abort(409, message="The username you entered is already taken")
                
        account = AccountModel(**account_data)
    
        try:
            db.session.add(account)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item into the database")

        return account

@blp.route("/account/<int:account_id>")
class Account(MethodView):
    @blp.response(200, AccountSchema)
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account
    
    @blp.arguments(UpdateAccountSchema)
    @blp.response(201, AccountSchema)
    def put(self, account_data, account_id):
        account = AccountModel.query.get_or_404(account_id)

        if account:
            account.first_name = account_data["first_name"]
            account.last_name = account_data["last_name"]
            account.password = account_data["password"]
        else: 
            return {"message" : "This account does not exist"}

        db.session.add(account)
        db.session.commit()

        return account

    def delete(self, account_id):
        account = AccountModel.query.get_or_404(account_id) 

        try:
            db.session.delete(account)
            db.session.commit()

            return {"message":"The account was successfully deleted."}
        except SQLAlchemyError:
            abort(500, message="An error occured while deleting the account")
