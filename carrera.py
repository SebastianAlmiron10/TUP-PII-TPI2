class Carrera():
    def __init__(self, nombre:str, cant_anios:int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cant_anios(self):
        return self.__cant_anios
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Cantidad de años: {self.cant_anios}'

        