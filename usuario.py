from cursos import *

lista_alumnos = []
lista_profesores = []
lista_usuarios = []

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
     
    def validar_credenciales(email:str, contrasenia:str) -> bool:
        email_valido = False
        contrasenia_valida = False
        for usuario_a_validar in lista_usuarios:
            if (usuario_a_validar.email == email):
                email_valido = True
                if usuario_a_validar.contrasenia == contrasenia:
                    contrasenia_valida = True
                    return contrasenia_valida
                else:
                    return contrasenia_valida
        if (email_valido == False):
            return email_valido


                        
        

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo:int, anio_inscripcion_carrera:int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__lista_cursos_matriculados = []

    def __str__(self) -> str:
        return f'\nNombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nContraseña: {self.contrasenia}\nLegajo: {self.legajo}\nAño Inscripcion: {self.anio_inscripcion_carrera}\n'
    
    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @property
    def lista_cursos_matriculados(self):
        return self.__lista_cursos_matriculados
    
    def matricular_en_curso(estudiante):
        cursos_mostrados = Curso.mostrar_cursos_enumerados()
        curso_id = int(input('Ingresar numero de curso que quieres inscribirte: '))
            
        if 1 <= curso_id <= len(cursos_mostrados):
            selected_curso = cursos_mostrados[curso_id - 1]
            estudiante.lista_cursos_matriculados.append(selected_curso)
            print('\nCurso añadido con exito\n')
        else:
            print('Numero de curso invalido')
    
    def mostrar_mis_cursos(self):
        for curso in self.lista_cursos_matriculados:
            print(curso)
    

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo:str, anio_egreso:int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def __str__(self) -> str:
        return f'\nNombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nContraseña: {self.contrasenia}\nTitulo: {self.titulo}\nAño egreso: {self.anio_egreso}\n'
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    def dictar_curso(curso: Curso):
        pass

