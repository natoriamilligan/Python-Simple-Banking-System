from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from db import db
from models import AccountModel, BlocklistModel
from schemas import AccountSchema, UpdateAccountSchema, LoginSchema, BlocklistSchema

blp = Blueprint("accounts", __name__, description="Operation on accounts")

@blp.route("/account")
class AccountList(MethodView):
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()

@blp.route("/create")
class CreateAccount(MethodView):
    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, account_data):
        if AccountModel.query.filter(AccountModel.username == account_data["username"]).first():
                abort(409, message="The username you entered is already taken")
                
        account = AccountModel(
            first_name=account_data["first_name"],
            last_name=account_data["last_name"],
            username=account_data["username"],
            password=pbkdf2_sha256.hash(account_data["password"])
            )
    
        try:
            db.session.add(account)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item into the database")

        return account
    
@blp.route("/login")
class AccountLogin(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, account_data):
        account = AccountModel.query.filter(AccountModel.username == account_data["username"]).first()

        if account and pbkdf2_sha256.verify(account_data["password"], account.password):
            access_token = create_access_token(identity=str(account.id), fresh=True)
            refresh_token = create_refresh_token(identity=str(account.id))
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            abort(401, message="Invalid credentials")

@blp.route("/logout")
class AccountLogout(MethodView):
    @jwt_required()
    @blp.arguments(BlocklistSchema)
    def post(self, blocklist_data):
        jti = get_jwt()["jti"]

        blocklist = BlocklistModel(jti=jti)
        
        db.session.add(blocklist)
        db.session.commit()

        return {"message": "Successfully logged out"}, 200
    
@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_account = get_jwt_identity()
        new_token = create_access_token(identity=current_account, fresh=False)
        return {"access_token": new_token}  


@blp.route("/account/<int:account_id>")
class Account(MethodView):
    @blp.response(200, AccountSchema)
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account
    
    @jwt_required()
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

    @jwt_required(fresh=True)
    def delete(self, account_id):
        account = AccountModel.query.get_or_404(account_id) 

        try:
            db.session.delete(account)
            db.session.commit()

            return {"message": "The account was successfully deleted."}
        except SQLAlchemyError:
            abort(500, message="An error occured while deleting the account")
