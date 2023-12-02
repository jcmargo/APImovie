from pydantic import BaseModel

# Definición del modelo de usuario
class User(BaseModel):
    email: str
    password: str