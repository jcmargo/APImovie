from sqlalchemy import Column, Integer, String, Float

from config.database import Base

#creamos el modelo para la base de datos
class Movie(Base):

    __tablename__ = 'Movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)