from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload=data, key='mi_llave', algorithm='HS256')
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key='mi_llave', algorithms=['HS256'])
    return data