from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AccountModel, DepositModel
from schemas import DepositSchema, AccountSchema

blp = Blueprint("deposits", __name__, description="Operation on deposits")

@blp.route("/account/<int:account_id>/deposit")
class AccountDeposit(MethodView):
    @blp.response(200, DepositSchema(many=True))
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account.deposits.all()

@blp.route("/deposit/<int:deposit_id>")
class Deposit(MethodView):
    @blp.response(200, DepositSchema)
    def get(self, deposit_id):
        deposit = DepositModel.query.get_or_404(deposit_id)
        return deposit
    
@blp.route("/transaction")
class CreateAccountTransactions(MethodView):

    def post(self, transaction_data):
        pass
    
    """
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

        """
