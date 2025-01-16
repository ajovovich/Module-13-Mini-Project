from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ("id", "name", "price")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)