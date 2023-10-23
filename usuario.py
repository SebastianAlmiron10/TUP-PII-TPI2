from cursos import *
from extras import *

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
        cl()
        cursos_mostrados = Curso.mostrar_cursos_enumerados()
        curso_id = int(input('\nIngresar numero de curso que quieres inscribirte: '))
        
        try:
            if 1 <= curso_id <= len(cursos_mostrados):
                selected_curso = cursos_mostrados[curso_id - 1]
                curso_ya_matriculado = False
                
                for curso_matriculado in estudiante.lista_cursos_matriculados:
                    if selected_curso.nombre == curso_matriculado.nombre:
                        print('\nYa estás matriculado en este curso\n')
                        curso_ya_matriculado = True
                        break
                if not curso_ya_matriculado:
                    contrasenia_curso = str(input('Ingresar clave de matriculacion: '))
                    if selected_curso.contrasenia_matriculacion == contrasenia_curso:
                        estudiante.lista_cursos_matriculados.append(selected_curso)
                        print('\nCurso añadido con exito\n')
                        cls()
                    else:
                        print('clave incorrecta\n\n')   
                        cls()   
            else:
                print('\nNumero de curso invalido\n')
                cls()
        except:
            print('Opcion invalida')
            cls()
    
    def mostrar_mis_cursos(Estudiante):
        for curso in Estudiante.lista_cursos_matriculados:
            print(curso)
    
class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo:str, anio_egreso:int) -> None:
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__lista_dictar_cursos = []
    
    def __str__(self) -> str:
        return f'\nNombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nContraseña: {self.contrasenia}\nTitulo: {self.titulo}\nAño egreso: {self.anio_egreso}\n'
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    @property
    def lista_dictar_cursos(self):
        return self.__lista_dictar_cursos

    def dictar_curso(profe):
        curso_nuevo = input("\nIngrese el nombre del curso: ")
        contrasenia_nuevo_curso = Curso.generar_contrasenia()
        
        curso_new = Curso(curso_nuevo, contrasenia_nuevo_curso)
        profe.lista_dictar_cursos.append(curso_new)
        lista_cursos.append(curso_new)
        print("\nSe agrego con exito\n")
        cls()
        
    def mostrar_mis_cursos_profe(profe):
        cl()
        for i, curso_profe in enumerate(profe.lista_dictar_cursos, start=1):
            print(f'{i} - {curso_profe.nombre}')
        
        try:
            curso_id = int(input('Ingresar numero de curso: '))
            if 1 <= curso_id <= len(profe.lista_dictar_cursos):
                curso_seleccionado = profe.lista_dictar_cursos[curso_id - 1]
                print(f'\nCurso seleccionado: {curso_seleccionado}')
                cls()
            else:
                print('Número de curso inválido.')
                cls()
        except:
            print('Opcion invalida')
            cls()