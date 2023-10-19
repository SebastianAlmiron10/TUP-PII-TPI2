from cursos import *

lista_alumnos = []
lista_profesores = []

class Usuario():

    def __init__(self, nombre:str, apellido:str, email:str, contrasenia:str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email =  email
        self._contrasenia = contrasenia
    
    def __str__(self) -> str:
        pass

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def email(self):
        return self._email
    @property
    def contrasenia(self):
        return self._contrasenia
    
    def validar_credenciales(self, email:str, contrasenia:str) -> bool:

        pass

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo:int, anio_inscripcion_carrera:int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    def __str__(self) -> str:
        return f'\nNombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nContraseña: {self.contrasenia}\nLegajo: {self.legajo}\nAño Inscripcion: {self.anio_inscripcion_carrera}\n'
    
    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    def matricular_en_curso(self, curso: Curso):
        pass
    

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo:str, anio_egreso:int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def __str__(self) -> str:
        return super().__str__()
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    def dictar_curso(curso: Curso):
        pass

