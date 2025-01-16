from marshmallow import Schema, fields, validate

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True, validate=validate.Length(max=120))

class Meta:
    fields = ("id", "name", "email")  


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)