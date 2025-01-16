from marshmallow import Schema, fields

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    order_date = fields.DateTime(required=True)
    quantity = fields.Int(required=True)

    class Meta:
        fields = ("id", "customer_id", "product_id","order_date", "quantity")


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)