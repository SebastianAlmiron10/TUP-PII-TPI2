from usuario import *
from cursos import *
from data import *

def ingresar_alumno():
    cl()
    email = input("Ingrese su email: \n")
    for alumno in lista_alumnos:
        if alumno.email == email:
            contrasenia = input("Ingrese su contraseña: \n")
            validacion_usuario = Usuario.validar_credenciales(email, contrasenia)
            if not(validacion_usuario):
                print("Usuario Invalido")
                break
            else:
                submenu_alumno(alumno)
                break
    else:
        print('Email no encontrado')
        

def submenu_alumno(estudiante):
    salir = True
    cl()
    while salir:
        
        while True:
            print('\n---- Menu Alumno----\n1 - Matricularse a un curso.\n2 - Ver curso.\n3 - Desmatricularse de un Curso\n4 - Volver al menu princpal')
            try:
                opt = int(input('Ingresar opcion: '))
                if 1 <= opt <= 3:
                    break
                else:
                    print('\nIngresar una opción válida (1 - 2 - 3)\n')
            except ValueError:
                print('\nIngresar una opción válida (1 - 2 - 3)\n')
        
        if opt == 1:
            Estudiante.matricular_en_curso(estudiante)
        elif opt == 2:
            cl()
            Estudiante.mostrar_mis_cursos(estudiante)
            cls()
        elif opt == 3:
            Estudiante.desmatricular_curso()
        else:
            salir = False

