import random
import string

lista_cursos = []
class Curso():
    def __init__(self, nombre:str, contrasenia_matriculacion:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self) -> str:
        return f'\nMateria: {self.nombre}\nContraseña de matriculacion: {self.contrasenia_matriculacion}\n'

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def generar_contrasenia() -> str:
        characters = string.ascii_letters + string.digits
        contrasenia_matriculacion = ''.join(random.choice(characters) for i in range(6))
        return contrasenia_matriculacion
    
    def mostrar_cursos() -> str:
        for curso in lista_cursos:
            print(curso)
    
    
