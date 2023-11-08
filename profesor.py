from usuario import *
from cursos import *
from data import *

def ingresar_profesor():
    cl()
    while True:
        print('1 - Iniciar Sesion.\n2 - Darse de Alta.\n3 - Salir')
        try:
            opt = int(input('Ingresar opcion: '))
            if 1 <= opt <= 3:
                break
            else:
                print('\nIngresar una opción válida (1 - 2 - 3)\n')

        except ValueError:
            print('\nIngresar una opción válida (1 - 2 - 3)\n')

    if opt == 1:
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
            print("Email no encontrado")
            cls()
    elif opt == 2:
        cl()
        codigo_alta = input("Ingrese el Codigo para Darse de Alta: ")
        if (codigo_alta.lower() == "admin"):
            alta_profesor()
        else:
            cl()
            print("Codigo Incorrecto")
            cls()
                
    elif opt == 3:
        pass


def alta_profesor():
    cl()
    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ") 
    titulo = input("Ingrese el Titulo que Tiene: ")
    while True:
        try:
            anio_egreso = int(input("Ingrese el Año de Egreso: "))
            if (anio_egreso < 1900 or anio_egreso > 3000):
                cl()
                print("Ingrese un Numero Válido\n")
            else:    
                break
        except ValueError:
            cl()
            print("Ingrese un Numero Válido\n")
    email = input("Ingrese su Email: ")

    email_repetido = False
    for profesor in lista_usuarios:
        if (email == profesor.email):
            cl()
            print("El Mail ya se Encuentra Registrado.")
            email_repetido = True
            cls()
            break
    
    if not(email_repetido):
        contrasenia = input("Ingrese una Contraseña para su Cuenta: ")
        profe_x = Usuario(nombre, apellido, email, contrasenia) #Creamos el Usuario
        lista_usuarios.append(profe_x)
        profe_X = Profesor(profe_x.nombre, profe_x.apellido, profe_x.email, profe_x.contrasenia, titulo, anio_egreso) #Creamos la Cuenta con la Informacion del Profesor
        lista_profesores.append(profe_X)
        cl()
        print("Registro Exitoso")
        cls()


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