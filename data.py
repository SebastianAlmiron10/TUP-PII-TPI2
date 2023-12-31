from usuario import *
from cursos import *
from archivo import *
from datetime import *

augusto = Usuario("Augusto", "Poratti", "augusto.poratti1@gmail.com", "12345")
sebastian = Usuario("Sebastian", "Almiron", "sebastianr_almiron@hotmail.com", "12345")
tadeo = Usuario("Tadeo", "Junco", "tadeojunco@hotmail.com", "12345")
ejemplo = Usuario("A", "B", "a@b.com", "12345")

lista_usuarios.append(augusto)
lista_usuarios.append(sebastian)
lista_usuarios.append(tadeo)
lista_usuarios.append(ejemplo)

alumno1 = Estudiante(augusto.nombre, augusto.apellido, augusto.email, augusto.contrasenia, 53056, 2023)
alumno2 = Estudiante(sebastian.nombre, sebastian.apellido, sebastian.email, sebastian.contrasenia, 53306, 2023)
alumno3 = Estudiante(tadeo.nombre, tadeo.apellido, tadeo.email, tadeo.contrasenia, 53044, 2023)
alumno4 = Estudiante(ejemplo.nombre, ejemplo.apellido, ejemplo.email, ejemplo.contrasenia, 54321, 2023)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)
lista_alumnos.append(alumno4)

Juan = Usuario("Juan", "Perez", "j@gmail.com", '12345')
lista_usuarios.append(Juan)

profe1 = Profesor(Juan.nombre, Juan.apellido, Juan.email, Juan.contrasenia, "Licenciado en Matematicas", 2008 )
lista_profesores.append(profe1)

curso1 = Curso("INGLES I", "a12345", Curso.generar_codigo())
curso2 = Curso("INGLES II", "ab1234", Curso.generar_codigo())
curso3 = Curso("PROGRAMACION I", "abc123", Curso.generar_codigo())
curso4 = Curso("PROGRAMACION II", "abcd12", Curso.generar_codigo())
curso5 = Curso("LABORATORIO DE COMPUTACION I", "abcde1", Curso.generar_codigo())
curso6 = Curso("LABORATORIO DE COMPUTACION II", "abcdef", Curso.generar_codigo())


lista_cursos.append(curso1)
lista_cursos.append(curso2)
lista_cursos.append(curso3)
lista_cursos.append(curso4)
lista_cursos.append(curso5)
lista_cursos.append(curso6)




