import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#creamos la base de datos
sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))  #se lee la ruta de este archivo

database_url  = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'   #creamos la direccion de la base de datos

engine = create_engine(database_url, echo=True)   #creamos el motor de la base de datos

Session = sessionmaker(bind=engine)  #Se crea session para conectarse a la base de datos, se enlaza con el comando "bind" y se iguala a engine

Base = declarative_base()  #sirve para manipular las tablas de datos
