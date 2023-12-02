# Importaciones de módulos y clases necesarios
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Importaciones personalizadas
from utils.jwt_manager import create_token
from schemas.user import User               #Schema User


login_router = APIRouter()


# Ruta de autenticación
@login_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)