from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TransferModel, AccountModel
from schemas import TransferSchema

blp = Blueprint("transfers", __name__, description="Operation on transfers")

@blp.route("/account/<int:account_id>/sent_transfers")
class AccountSentTransdfer(MethodView):
    @blp.response(200, TransferSchema(many=True))
    def get(self, account_id):
        account = TransferModel.query.get_or_404(account_id)
        return account.sent_transfers.all()
    
@blp.route("/account/<int:account_id>/received_transfers")
class AccountReceivedtransfer(MethodView):
    @blp.response(200, TransferSchema(many=True))
    def get(self, account_id):
        account = TransferModel.query.get_or_404(account_id)
        return account.received_transfers.all()
    
