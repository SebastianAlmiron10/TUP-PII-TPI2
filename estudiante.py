from usuario import *
from cursos import *
from data import *

def ingresar_alumno():
    email = input("Ingrese su email: \n")
    for alumno in lista_alumnos:
        if alumno.email == email:
            contrasenia = input("Ingrese su contraseña: \n")
            validacion_usuario = Usuario.validar_credenciales(email, contrasenia)
            if alumno.contrasenia == contrasenia:
                if (validacion_usuario):
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
            Estudiante.matricular_en_curso(estudiante)
        elif opt == 2:
            Estudiante.mostrar_mis_cursos()
        else:
            salir = False

