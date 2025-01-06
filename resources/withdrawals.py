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

@blp.route("/withdrawal/<int:withdrawal_id>")
class Deposit(MethodView):
    @blp.response(200, WithdrawalSchema)
    def get(self, withdrawal_id):
        withdrawal = WithdrawalModel.query.get_or_404(withdrawal_id)
        return withdrawal