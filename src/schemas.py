from marshmallow import Schema, fields

class URLSchema(Schema):
    url = fields.Url(required=True)