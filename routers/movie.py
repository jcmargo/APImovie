# Importaciones de módulos y clases necesarios
from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse
from typing import List

# Importaciones personalizadas
from middlewares.jwt_bearer import JWTBearer
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.movie import MovieServices
from schemas.movie import Movie                   #Schema Movie


#Creamos el router
movie_router = APIRouter()



# Ruta para obtener todas las películas (se requiere autenticación)
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def return_movies() -> list[Movie]:
    db = Session()
    result = MovieServices(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))    #jsonable_encoder para volver la respuesta a objeto json



# Ruta para obtener una película por su ID
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movies(id: int = Path(ge=1, le=5000)) -> Movie:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'Mensaje': 'No fue encontrada la película'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))



# Ruta para obtener películas por categoría
@movie_router.get('/movie/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str =  Query(min_length=3, max_length=20)) -> List[Movie]:
    db = Session()
    result = MovieServices(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'Mensaje': 'No se encotraron peliculas con esta categoria'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))



# Ruta para crear una nueva película
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieServices(db).create_movie(movie)
    return JSONResponse(status_code=201, content={'Mensaje': 'Se creó correctamente la pelicula'})



# Ruta para actualizar una película por su ID
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'Mensaje': 'No fue encontrada la película'})
    
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={'message': 'Se ha actualizado'})



# Ruta para eliminar una película por su ID
@movie_router.delete('/movies/', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'Mensaje': 'No fue encontrada la película'})

    MovieServices(db).delete_movie(id)
    return JSONResponse(status_code=200, content={'Mensaje': 'Se ha eliminado la pelicula'})
      