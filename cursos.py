import random
import string


lista_cursos = []
class Curso():
    prox_cod = int(0) 

    def __init__(self, nombre:str, contrasenia_matriculacion:str, codigo:int) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        self.__codigo = codigo
        


    def __str__(self) -> str:
        return f'\nMateria: {self.nombre}\nContraseña de matriculacion: {self.contrasenia_matriculacion}\nCodigo: {self.codigo}'

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @staticmethod
    def generar_contrasenia() -> str:
        characters = string.ascii_letters + string.digits
        contrasenia_matriculacion = ''.join(random.choice(characters) for i in range(6))
        return contrasenia_matriculacion
    
    @staticmethod
    def generar_codigo() -> int:
        Curso.prox_cod += 1
        return Curso.prox_cod

    
    def mostrar_cursos() -> str:
        cursos_ordenados = sorted(lista_cursos, key=lambda curso: curso.nombre)
        for curso in cursos_ordenados:
            print(curso.nombre)
    
    def mostrar_cursos_enumerados() -> str:
        cursos_ordenados = sorted(lista_cursos, key=lambda curso: curso.nombre)
        for i, curso in enumerate(cursos_ordenados, start=1):
            print(f'{i} - {curso.nombre}')
        return cursos_ordenados
    
    def nuevo_archivo(archivo: object):
        pass

    
    
