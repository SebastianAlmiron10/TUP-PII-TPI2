from usuario import *
from cursos import *
from data import *

def ingresar_profesor():
    cl()
    email = input("Ingrese su email: \n")
    for profesor in lista_profesores:
        if profesor.email == email:
            contrasenia = input("Ingrese su contraseña: \n")
            validacion_usuario = Usuario.validar_credenciales(email, contrasenia)
            if not(validacion_usuario):
                print("Usuario Invalido")
                break
            else:
                submenu(profesor)
                break
    else:
        print('Email no encontrado')

def submenu(profe):
    salir = True
    cl()
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