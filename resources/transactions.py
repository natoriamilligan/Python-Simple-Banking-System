from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models import AccountModel

blp = Blueprint("transactions", __name__, description="Operation on transactions")

@blp.route("/account/<int:account_id>/transaction")
class AccountTransactions(MethodView):
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account.transactions.all()

    def post(self, account_data, account_id):
        account = AccountModel.query.get_or_404(account_id)

        if account_data["type"] == "deposit":
            account.balance = account.balance + account_data["amount"]
        elif account_data["type"] == "withdrawal":
            if account.balance - account_data["amount"] < 0:
                abort(422, message="Not enough funds in the account")
            else:
                account.balance = account.balance - account_data["amount"]
        else:
            abort(400, message="Invalid JSON payload")

        return {"message": f"Your new balance is ${account.balance}"}


@blp.route("/transaction/<int:transaction_id>")
class Transaction(MethodView):
    def get(self, transaction_id):
        pass


