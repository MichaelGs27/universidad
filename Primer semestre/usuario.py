user = "Michael"
contra = 123

while True:
    userw = input("Ingrese su usuario: ")
    contrap = input("ingrese su contraseña: ")
    if userw == user and contrap == contra:
        print("Bienvenido.")
        break
    else:
        print("intentelo de nuevo.") 