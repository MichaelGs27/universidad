def nVerificarCredenciales(nUsuario, nContrasena):
    if nUsuario == "Vendedor14" and len(nContrasena) == 10:
        print("Acceso concedido")
        nMostrarMenu()
    else:
        print("Error: Usuario o contraseña incorrectos")

def nMostrarMenu():
    while True:
        print("Seleccione una opción:")
        print("1. Compra")
        print("2. Renta")
        print("3. Entrega")
        print("4. Salir")

        nOpcion = input("Ingrese el número de opción: ")

        if nOpcion == "1":
            print("Ha seleccionado la opción de Compra")
            nGenerarTicketCompra()
            continuar = input("Presione Enter para volver al menú...")
        elif nOpcion == "2":
            print("Ha seleccionado la opción de Renta")
            continuar = input("Presione Enter para volver al menú...")
        elif nOpcion == "3":
            print("Ha seleccionado la opción de Entrega")
            continuar = input("Presione Enter para volver al menú...")
        elif nOpcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
            continuar = input("Presione Enter para volver al menú...")

def nGenerarTicketCompra():
    nNombrePelicula = input("Ingrese el nombre del pelicula: ")
    nCantidad = int(input("Ingrese la cantidad a comprar: "))
    nPrecioUnitario = float(input("Ingrese el precio unitario: "))
    nTotal = nCantidad * nPrecioUnitario

    print("***** Ticket de Compra *****")
    print("Producto:", nNombrePelicula)
    print("Cantidad:", nCantidad)
    print("Precio unitario:", nPrecioUnitario)
    print("Total a pagar:", nTotal)
    print("*****************************")

# Solicitar usuario y contraseña al usuario
usuario = input("Ingrese el usuario: ")
contrasena = input("Ingrese la contraseña: ")

# Verificar las credenciales
nVerificarCredenciales(usuario, contrasena)
