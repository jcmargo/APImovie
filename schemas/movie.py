from typing import Optional
from pydantic import BaseModel, Field

# Definición del modelo de película
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=20)   # Validar que tenga entre 5 y 20 caracteres
    overview: str = Field(min_length=10, max_length=50)  # Validar que tenga entre 10 y 50 caracteres
    year: int = Field(le=2022)  # Validar que el año sea menor o igual a 2022
    rating: float = Field(ge=1, le=10)  # Validar que el rating esté entre 1 y 10
    category: str = Field(min_length=5, max_length=30)  # Validar que tenga entre 5 y 30 caracteres

    # Clase para colocar atributos default
    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                'title': 'Titulo de pelicula',
                'overview': 'Descripcion',
                'year': 2022,
                'rating': 5,
                'category': 'categoria'
            }
        }