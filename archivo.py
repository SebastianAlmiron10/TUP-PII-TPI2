from cursos import *
from datetime import *

lista_archivos = []
class Archivo():
    def __init__(self, nombre:str, fecha:date, formato:str) -> None:
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato
        
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha(self):
        return self.__fecha

    @property
    def formato(self):
        return self.__formato
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Fecha: {self.fecha} - Formato: {self.formato}'
    
