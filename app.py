print("---- Bienvenido al Menu ----")
print("1- Ingresar como Alumno")
print("2- Ingresar como Profesor")
print("3- Ver Cursos")
print("4- Salir")

respuesta2 = ''

while True:
        
    option = input("\n Ingrese la opción de menú: ")
   
    if option.isnumeric() == True:
        if int(option) == 1:
            print("")
        elif int(option) == 2:
            print("")
        elif int(option) == 3:
            print("")
        elif int(option) == 4:
            break
    else: 
        print("Ingrese una opción numérica")