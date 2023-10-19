from usuario import *
import random
import string
from cursos import *
def generar_contraseña():
    
    caracteres = string.digits

   
    contraseña = ''.join(random.choice(caracteres) for _ in range(6))

    return contraseña


contraseña_generada = generar_contraseña()


print(contraseña_generada)


alumno1 = Estudiante("Augusto", "Poratti", "augusto.poratti1@gmail.com", "12345", 53056, 2023)
alumno2 = Estudiante("Sebastian", "Almiron", "sebastianr_almiron@hotmail.com", "12345", 53306, 2023)
alumno3 = Estudiante("Tadeo", "Junco", "tadeojunco@hotmail.com", "12345", 53044, 2023)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)

profe1 = Profesor("Juan", "Perez", "juanperez@gmail.com", "Licenciado en Matematica", 2008)

lista_profesores.append(profe1)

curso1 = Curso("INGLES 1", generar_contraseña())
curso2 = Curso("INGLES 2", generar_contraseña())
curso3 = Curso("PROGRAMACION 1",generar_contraseña())
curso4 = Curso("PROGRAMACION 2",generar_contraseña())
curso5 = Curso("LABORATORIO DE COMPUTACION 1",generar_contraseña())
curso6 = Curso("LABORATORIO DE COMPUTACION 2",generar_contraseña())

lista_cursos.append(curso1)
lista_cursos.append(curso2)
lista_cursos.append(curso3)
lista_cursos.append(curso4)
lista_cursos.append(curso5)
lista_cursos.append(curso6)



