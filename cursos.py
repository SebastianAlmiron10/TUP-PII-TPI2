

class Curso():
    def __init__(self, nombre:str, contrasenia_matriculacion:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self) -> str:
        pass    

    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def generar_contrasenia() -> str:
        pass

    