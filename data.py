from usuario import *
from cursos import *

alumno1 = Estudiante("Augusto", "Poratti", "augusto.poratti1@gmail.com", "12345", 53056, 2023)
alumno2 = Estudiante("Sebastian", "Almiron", "sebastianr_almiron@hotmail.com", "12345", 53306, 2023)
alumno3 = Estudiante("Tadeo", "Junco", "tadeojunco@hotmail.com", "12345", 53044, 2023)
alumno3 = Estudiante("A", "B", "a@b.com", "12345", 54321, 2023)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)

profe1 = Profesor("Juan", "Perez", "j@gmail.com", '12345', "Licenciado en Matematicas", 2008)

lista_profesores.append(profe1)

curso1 = Curso("INGLES I", 'abcd')
curso2 = Curso("INGLES II", Curso.generar_contrasenia())
curso3 = Curso("PROGRAMACION I", Curso.generar_contrasenia())
curso4 = Curso("PROGRAMACION II", Curso.generar_contrasenia())
curso5 = Curso("LABORATORIO DE COMPUTACION I", Curso.generar_contrasenia())
curso6 = Curso("LABORATORIO DE COMPUTACION II", Curso.generar_contrasenia())

lista_cursos.append(curso1)
lista_cursos.append(curso2)
lista_cursos.append(curso3)
lista_cursos.append(curso4)
lista_cursos.append(curso5)
lista_cursos.append(curso6)

#for alumno in lista_alumnos:
#    print(alumno)
    
#for profesor in lista_profesores:
#    print(profesor)
    
#Curso.mostrar_cursos()