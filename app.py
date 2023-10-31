from usuario import *
from cursos import *
from data import *
from estudiante import *
from profesor import *




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
        ingresar_alumno()  
        cls()
    elif opt == 2:
        ingresar_profesor()
        cl()
    elif opt == 3:
        cl()
        print('\nCURSOS:')
        Curso.mostrar_cursos()
        cls()
    else:
        salir = False