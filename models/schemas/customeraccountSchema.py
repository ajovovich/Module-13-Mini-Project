from marshmallow import Schema, fields

class CustomerAccount(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    username = fields.Str(required=True)
    password_hash = fields.Str(load_only=True)

class Meta:
    fields = ("id","customer_id", "username", "password")

customer_account_schema = CustomerAccount()
customer_accounts_schema = CustomerAccount(many=True)