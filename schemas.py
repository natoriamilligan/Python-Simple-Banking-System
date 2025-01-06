from marshmallow import Schema, fields

class DepositSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    account_id = fields.Int(required=True)

class TransferSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    submitter_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)

class UpdateAccountSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True)

class AccountSchema(UpdateAccountSchema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    balance = fields.Str(dump_only=True)
    sent_transfers = fields.List(fields.Nested(TransferSchema()), dump_only=True)
    received_transfers = fields.List(fields.Nested(TransferSchema()), dump_only=True)
    deposits = fields.List(fields.Nested(DepositSchema()), dump_only=True)