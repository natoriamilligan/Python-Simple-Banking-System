from marshmallow import Schema, fields

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    recipient = fields.Str(required=True)
    type = fields.Str(required=True)

class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    balance = fields.Float(dump_only=True)
    transactions = fields.List(fields.Nested(TransactionSchema()), dump_only=True)
