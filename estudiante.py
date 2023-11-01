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
        print('Email no encontrado, Debe darse de Alta en Alumnado.')
        

def submenu_alumno(estudiante):
    cl()
    salir = True
    while salir:
        
        while salir:
            print('\n---- Menu Alumno ----\n1 - Matricularse a un curso.\n2 - Desmatricularse de un Curso.\n3 - Ver curso. \n4 - Volver al menu princpal.')
            try:
                opt = int(input('Ingresar opcion: '))
                if 1 <= opt <= 4:
                    if opt == 1:
                        Estudiante.matricular_en_curso(estudiante)
                    elif opt == 2:
                        Estudiante.desmatricular_curso(estudiante)
                    elif opt == 3:
                        cl()
                        Estudiante.mostrar_mis_cursos(estudiante)
                        cls()
                    elif opt == 4:
                        salir = False
                        break
                else:
                    print('\nIngresar una opción válida (1 - 2 - 3 - 4)\n')
            except:
                print('\nIngresar una opción válida (1 - 2 - 3 - 4)\n')
        
            
                
