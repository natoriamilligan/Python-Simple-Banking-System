from db import db

class AccountModel(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    first_namme = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    balance = db.Column(db.Float(precision=2), unique=False, nullable=False)
    transaction_history = db.relationship("TransactionModel", back_populates="accounts", lazy="dynamic", cascade="all, delete")