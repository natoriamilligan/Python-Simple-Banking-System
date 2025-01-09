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
    
@blp.route("/transfer")
class AccountTransfer(MethodView):
    @blp.arguments(TransferSchema)
    @blp.response(200, TransferSchema)
    def post(self, transfer_data):

        if transfer_data["submitter_id"] == transfer_data["recipient_id"]:
            abort(400, message="The submitter cannot be the same as the reciever.")
        else:
            submitter = AccountModel.query.get_or_404(transfer_data["submitter_id"])
            recipient = AccountModel.query.get_or_404(transfer_data["recipient_id"])

            if submitter.balance - transfer_data["amount"] < 0:
                abort(422, message="Not enough funds in the submitter's account")
            else:
                submitter.balance = submitter.balance - transfer_data["amount"]
                recipient.balance = recipient.balance + transfer_data["amount"]

            transfer = TransferModel(**transfer_data)
            
            try:
                db.session.add(transfer)
                db.session.commit()
            except SQLAlchemyError:
                abort(500, message="An error occured adding the transaction to the database")

            return transfer

        
