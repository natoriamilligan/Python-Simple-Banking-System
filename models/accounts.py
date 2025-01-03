from db import db
from models.transactions import TransactionModel

class AccountModel(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    balance = db.Column(db.Float(precision=2), default=0, unique=False, nullable=False)
    received_transactions = db.relationship("TransactionModel", foreign_keys=[TransactionModel.recipient_id], back_populates="recipient", lazy="dynamic", cascade="all, delete")
    submitted_transactions = db.relationship("TransactionModel", foreign_keys=[TransactionModel.submitter_id], back_populates="submitter", lazy="dynamic", cascade="all, delete")