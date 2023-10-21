from usuario import *
from data import *
from cursos import *

def ingresar_alumno():
    email = input("Ingrese su email: \n")
    for alumno in lista_alumnos:
        if alumno.email == email:
            contrasenia = input("Ingrese su contraseña: \n")
            if alumno.contrasenia == contrasenia:
                submenu_alumno(alumno)
                break
            else:
                print('La contraseña es incorrecta.')
                break
    else:
        print('Email no encontrado')

def submenu_alumno(estudiante):
    salir = True
    while salir:
        
        while True:
            print('\n---- Menu Alumno----\n1 - Matricularse a un curso.\n2 - Ver curso.\n3 - Volver al menu principal\n')
            try:
                opt = int(input('Ingresar opcion: '))
                if 1 <= opt <= 3:
                    break
                else:
                    print('\nIngresar una opción válida (1 - 2 - 3)\n')
            except ValueError:
                print('\nIngresar una opción válida (1 - 2 - 3)\n')
        
        if opt == 1:
            cursos_mostrados = Curso.mostrar_cursos_enumerados()
            curso_id = int(input('Ingresar numero de curso que quieres inscribirte: '))
            
            if 1 <= curso_id <= len(cursos_mostrados):
                selected_curso = cursos_mostrados[curso_id - 1]
                estudiante.cursos_matriculados.append(selected_curso)
                print('\nCurso añadido con exito\n')
            else:
                print('Numero de curso invalido')
        elif opt == 2:
            Curso.mostrar_cursos()
        else:
            salir = False

