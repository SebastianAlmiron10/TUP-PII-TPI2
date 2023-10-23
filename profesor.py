from usuario import *
from cursos import *
from data import *

def ingresar_profesor():
    email_profe = input("Ingrese su email: \n")
    for profesor in lista_profesores:
        if profesor.email == email_profe:
            contrasenia = input("Ingrese su contraseña: \n")
            if profesor.contrasenia == contrasenia:
                submenu_profe(profesor)
                break
            else:
                print('La contraseña es incorrecta.')
                break
    else:
        print('Email no encontrado, darse de alta en alumnado')

def submenu_profe(profe):
    salir = True
    while salir:
        
        while True:
            print('\n---- Menu Profesor----\n1 - Dictar curso.\n2 - Ver curso.\n3 - Volver al menu principal\n')
            try:
                opt = int(input('Ingresar opcion: '))
                if 1 <= opt <= 3:
                    break
                else:
                    print('\nIngresar una opción válida (1 - 2 - 3)\n')
            except ValueError:
                print('\nIngresar una opción válida (1 - 2 - 3)\n')
        
        if opt == 1:
            Profesor.dictar_curso(profe)
        elif opt == 2:
           Profesor.mostrar_mis_cursos_profe(profe)
        else:
            salir = False        