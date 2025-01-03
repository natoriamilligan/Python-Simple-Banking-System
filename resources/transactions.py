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

@blp.route("/transaction/<int:transaction_id>")
class Transaction(MethodView):
    @blp.response(200, TransactionSchema)
    def get(self, transaction_id):
        transaction = TransactionModel.query.get_or_404(transaction_id)
        return transaction
    
@blp.route("/transaction")
class CreateAccountTransactions(MethodView):
    @blp.arguments(TransactionSchema)
    @blp.response(200, TransactionSchema)
    def post(self, transaction_data):
        if AccountModel.query.filter(AccountModel.id == transaction_data["recipient_id"]).first():
            submitter_account = AccountModel.query.get_or_404(transaction_data["submitter_id"])
            if transaction_data["type"] == "deposit":
                submitter_account.balance = submitter_account.balance + transaction_data["amount"]
            elif transaction_data["type"] == "withdrawal":
                if submitter_account.balance - transaction_data["amount"] < 0:
                    abort(422, message="Not enough funds in the account")
                else:
                    submitter_account.balance = submitter_account.balance - transaction_data["amount"]
            elif transaction_data["type"] == "transfer":
                if submitter_account.balance - transaction_data["amount"] < 0:
                    abort(422, message="Not enough funds in the account")
                else:
                    submitter_account.balance = submitter_account.balance - transaction_data["amount"]
                    
                    recipient_account = AccountModel.query.get_or_404(transaction_data["recipient_id"])
                    recipient_account.balance = recipient_account.balance + transaction_data["amount"]
            else:
                abort(400, message="Invalid JSON payload")
        else:
            abort(404, message="Recipient not found")

        transaction = TransactionModel(**transaction_data)
        
        try:
            db.session.add(transaction)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured adding the transaction to the database")

        return transaction

