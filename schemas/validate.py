#for sending data request
from marshmallow import Schema, fields

class ValidateRequestSchema(Schema):
    html_data= fields.Str(required=True, error='HTML Data is mandatory field.')
    url = fields.Str(required=True, error='Url is mandatory field.')
