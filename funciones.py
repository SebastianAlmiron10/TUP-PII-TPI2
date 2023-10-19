from usuario import *
from data import *
from cursos import *

def ingresar_alumno():
    email = input("Ingrese su email: \n")
    for alumno in lista_alumnos:
        if alumno.email == email:
            contrasenia = input("Ingrese su contraseña: \n")
            if alumno.contrasenia == contrasenia:
                submenu_alumno()
                break
            else:
                print('La contraseña es incorrecta.')
                break
    else:
        print('Email no encontrado')

def submenu_alumno():
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
            print('opt 1')
        elif opt == 2:
            Curso.mostrar_cursos()
        else:
            salir = False

