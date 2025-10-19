from functools import wraps
from marshmallow import ValidationError, Schema
from flask import jsonify, request

def validate_schema(schema: Schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                return jsonify(err.messages), 400
            return f(*args, **kwargs, **data)
        return decorated_function
    return decorator

BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def custom_base62_encode(number: int):
    if number == 0:
        return BASE62_ALPHABET[0]

    result = ""
    base = len(BASE62_ALPHABET)
    while number > 0:
        number, remainder = divmod(number, base)
        result = BASE62_ALPHABET[remainder] + result

    return result

def custom_base62_decode(encoded_string: str):
    base = len(BASE62_ALPHABET)
    result = 0
    for char in encoded_string:
        result = result * base + BASE62_ALPHABET.index(char)

    return result