# Importaciones de módulos y clases necesarios
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Importaciones personalizadas
from config.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router

# Creación de la aplicación FastAPI
app = FastAPI()
app.title = 'Mi aplicacion con fastAPI'
app.version = '0.0.1'

#Agregamos el middleware
app.add_middleware(ErrorHandler)

#Agregamos los routers
app.include_router(movie_router)
app.include_router(login_router)

# Creación de la base de datos
Base.metadata.create_all(bind=engine)



# Función de validación para consultas
def valid_querie(year: int, category: str, movie: dict):
    return movie['category'] == category and movie['year'] == year



# Ruta principal de la aplicación
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>hello world</h1>')



