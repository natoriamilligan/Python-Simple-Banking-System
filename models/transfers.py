from db import db

class TransferModel(db.Model):
    __tablename__ = "transfers"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    submitter_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), unique=False, nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), unique=False, nullable=False)
    submitter = db.relationship("AccountModel", foreign_keys=[submitter_id], back_populates="sent_transfers")
    recipient = db.relationship("AccountModel", foreign_keys=[recipient_id], back_populates="received_transfers")