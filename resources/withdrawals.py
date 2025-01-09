from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AccountModel, WithdrawalModel
from schemas import WithdrawalSchema, AccountSchema

blp = Blueprint("withdrawals", __name__, description="Operation on withdrawals")

@blp.route("/account/<int:account_id>/withdrawal")
class AccountWithdrawal(MethodView):
    @blp.response(200, WithdrawalSchema(many=True))
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account.withdrawals.all()
    
    @blp.arguments(WithdrawalSchema)
    @blp.response(200, WithdrawalSchema)
    def post(self, withdrawal_data, account_id):
        if AccountModel.query.filter(AccountModel.id == account_id).first():
            account = AccountModel.query.get_or_404(account_id)
            if account.balance - withdrawal_data["amount"] < 0:
                abort(422, message="Not enough funds in the account")
            else:
                account.balance = account.balance - withdrawal_data["amount"]
        else:
            abort(404, message="Recipient not found")

        withdrawal = WithdrawalModel(account_id=account_id, **withdrawal_data)
        
        try:
            db.session.add(withdrawal)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured adding the withdrawal to the database")

        return withdrawal

@blp.route("/withdrawal/<int:withdrawal_id>")
class Deposit(MethodView):
    @blp.response(200, WithdrawalSchema)
    def get(self, withdrawal_id):
        withdrawal = WithdrawalModel.query.get_or_404(withdrawal_id)
        return withdrawal