import os
from flask import Flask, jsonify
from flask_smorest import Api
from db import db
from flask_jwt_extended import JWTManager

from resources.accounts import blp as AccountsBlueprint
from resources.deposits import blp as DepositsBlueprint
from resources.withdrawals import blp as WithdrawalsBlueprint
from resources.transfers import blp as TransfersBlueprint

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Banking API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"

    db.init_app(app)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "79023088310581544527589837667420155225"
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    api.register_blueprint(AccountsBlueprint)
    api.register_blueprint(DepositsBlueprint)
    api.register_blueprint(WithdrawalsBlueprint)
    api.register_blueprint(TransfersBlueprint)

    with app.app_context():
        db.create_all()


    return app


    