from db import db

class DepositModel(db.Model):
    __tablename__ = "deposits"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=False, nullable=False)
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    account = db.relationship("AccountModel", back_populates="deposits")