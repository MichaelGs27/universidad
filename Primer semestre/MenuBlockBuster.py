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
            print("----------Ha seleccionado la opción de Compra------------")
            nGenerarTicketCompra()
            continuar = input("Presione Enter para volver al menú...")
        elif nOpcion == "2":
            print("--------Ha seleccionado la opción de Renta------------")
            print("Por cada dia de renta se cobran $12.50.")
            print("Si es de terror, se aplica un incremento del 12% a la renta diaria.")
            print("Si es de ciencia ficcion, se aplica un incremento del 7% a la renta diaria.")
            print("Si es de niños, se aplica un descuento a la renta diaria de 5% a la renta diaria") 
            print("Si es romantica, se aplica un descuento del 10% a la renta diaria.")
            print("En caso de ser de otra categoria, no aplica ningun descuento.")

            nGenerarTicketRenta()
            continuar = input("Presione Enter para volver al menú...")
        elif nOpcion == "3":
            print("-----------Ha seleccionado la opción de Entrega---------------")
            print("Por ser mayor a 3 días se cobrará un incremento del 30% de lo contrario seguira con el precio natural")
            nGenerarTicketEntrega()
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
    nTotal = nCantidad * 78

    print("***** Ticket de Compra *****")
    print(f"Producto: {nNombrePelicula}")
    print(f"Cantidad: {nCantidad}")
    print(f"Precio unitario: {78}")
    print("Total a pagar: ${:.2f}".format(nTotal))
    print("*****************************")

def nGenerarTicketRenta():
    nTotalPeliculaRenta = 12.50
    nCategoriaPelicula = input.upper("Ingrese la categoria de la pelicula(EN MAYUSCULA): ")
    nCantidad = int(input("Ingrese la cantidad a comprar: "))
    if nCategoriaPelicula == "TERROR":
        nTotalPeliculaRenta *= 1.12
    elif nCategoriaPelicula == "CIENCIA FICCION":
        nTotalPeliculaRenta *= 1.07
    elif nCategoriaPelicula == "NIÑOS":
        nTotalPeliculaRenta *= 0.95
    elif nCategoriaPelicula == "ROMANTICA":
        nTotalPeliculaRenta *= 0.90
    elif nCategoriaPelicula == "OTRA":
        nTotalPeliculaRenta = nTotalPeliculaRenta/ 3 * nCantidad

    print("***** Ticket de Compra *****")
    print(f"Producto: {nCategoriaPelicula}")
    print(f"Cantidad:{nCantidad}")
    print("Total a pagar: ${:.2f}".format(nTotalPeliculaRenta))
    print("*****************************")

def nGenerarTicketEntrega():
    from datetime import datetime, timedelta
    nFechaRenta = datetime.strptime(input("Ingrese la fecha de renta (DD-MM-AAAA): "),"%d-%m-%Y")
    nFechaEntrega = datetime.strptime(input("Ingrese la fecha de entrega (DD-MM-AAAA): "),"%d-%m-%Y")
    print()
    nDiasRenta = (nFechaEntrega - nFechaRenta).days
    nRentaDiaria = 12.50
    nCostoTotal = nRentaDiaria *12.50
    if nDiasRenta > 3:
        nRentaDiaria *= 1.30

    nCostoTotal = nRentaDiaria * nDiasRenta

    print("***** Ticket de Compra *****")
    print(f"Fecha de la renta: {nFechaRenta}")
    print(f"Fecha de la entegra:{nFechaEntrega}")
    print("Total a pagar: ${:.2f}".format(nCostoTotal))
    print("*****************************")


# Solicitar usuario y contraseña al usuario
nUsuario = input("Ingrese el usuario: ")
nContrasena = input("Ingrese la contraseña: ")

# Verificar las credenciales
nVerificarCredenciales(nUsuario, nContrasena)
