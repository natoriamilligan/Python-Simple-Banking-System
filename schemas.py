from marshmallow import Schema, fields

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    recipient_account_id = fields.Integer(required=True)
    account_id = fields.Int(required=True)

class UpdateAccountSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True)

class AccountSchema(UpdateAccountSchema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    balance = fields.Str(dump_only=True)
    transactions = fields.List(fields.Nested(TransactionSchema()), dump_only=True)