from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

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
    
    @jwt_required()
    @blp.arguments(DepositSchema)
    @blp.response(200, DepositSchema)
    def post(self, deposit_data, account_id):
        if AccountModel.query.filter(AccountModel.id == account_id).first():
            account = AccountModel.query.get_or_404(account_id)
            account.balance = account.balance + deposit_data["amount"]
        else:
            abort(404, message="Recipient not found")

        deposit = DepositModel(account_id=account_id, **deposit_data)
        
        try:
            db.session.add(deposit)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured adding the deposit to the database")

        return deposit
    
@blp.route("/deposit/<int:deposit_id>")
class Deposit(MethodView):
    @blp.response(200, DepositSchema)
    def get(self, deposit_id):
        deposit = DepositModel.query.get_or_404(deposit_id)
        return deposit
    

