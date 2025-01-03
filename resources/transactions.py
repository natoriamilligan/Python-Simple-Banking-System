from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AccountModel, TransactionModel
from schemas import TransactionSchema, AccountSchema

blp = Blueprint("transactions", __name__, description="Operation on transactions")

@blp.route("/account/<int:account_id>/transaction")
class AccountTransactions(MethodView):
    @blp.response(200, TransactionSchema(many=True))
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account.transactions.all()

    @blp.arguments(TransactionSchema)
    @blp.response(200, AccountSchema)
    def post(self, transaction_data, account_id):
        account = AccountModel.query.get_or_404(account_id)

        if transaction_data["type"] == "deposit":
            account.balance = account.balance + transaction_data["amount"]
            transaction = TransactionModel(**transaction_data)
        elif transaction_data["type"] == "withdrawal":
            if account.balance - transaction_data["amount"] < 0:
                abort(422, message="Not enough funds in the account")
            else:
                account.balance = account.balance - transaction_data["amount"]
                transaction = TransactionModel(**transaction_data)
        else:
            abort(400, message="Invalid JSON payload")

        try:
            db.session.add(transaction)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured adding the transaction to the database")

        return account


@blp.route("/transaction/<int:transaction_id>")
class Transaction(MethodView):
    def get(self, transaction_id):
        pass


