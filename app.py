from usuario import *
from cursos import *
from data import *
from funciones import *


salir = True
while salir:
    
    while True:
        print('---- Bienvenido al Menu ----\n1 - Ingresar como Alumno.\n2 - Ingresar como Profesor.\n3 - Ver Cursos\n4 - Salir')
        try:
            opt = int(input('Ingresar opcion: '))
            if 1 <= opt <= 4:
                break
            else:
                print('\nIngresar una opción válida (1 - 2 - 3 - 4)\n')

        except ValueError:
            print('\nIngresar una opción válida (1 - 2 - 3 - 4)\n')
    
    if opt == 1:
        print('opt 1')
        ingresar_alumno()
    elif opt == 2:
        print('opt 2')
    elif opt == 3:
        print('\nCURSOS:')
        Curso.mostrar_cursos()
    else:
        salir = False