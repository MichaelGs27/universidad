def imprimir_ticket(titulo, total):
    print("*******************************")
    print("          TICKET DE VENTA      ")
    print("*******************************")
    print("Película: {}".format(titulo))
    print("Total a pagar: ${:.2f}".format(total))
    print("*******************************\n")

def compra_peliculas():
    cantidad = int(input("Ingrese la cantidad de películas a comprar: "))
    total = cantidad * 78
    imprimir_ticket("Compra", total)

def renta_peliculas():
    cantidad = int(input("Ingrese la cantidad de películas a rentar: "))
    dias = int(input("Ingrese la cantidad de días de renta: "))
    categoria = input("Ingrese la categoría de la película: ")

    costo_diario = 12.50
    porcentaje_descuento = 0

    if categoria == "terror":
        costo_diario *= 1.12
    elif categoria == "ciencia ficcion":
        costo_diario *= 1.07
    elif categoria == "niños":
        costo_diario *= 0.95
    elif categoria == "romántica":
        costo_diario *= 0.90

    total = cantidad * (costo_diario * dias)
    imprimir_ticket("Renta", total)

def entrega_peliculas():
    fecha_renta = input("Ingrese la fecha de renta (formato: dd/mm/yyyy): ")
    fecha_entrega = input("Ingrese la fecha de entrega (formato: dd/mm/yyyy): ")

    dias_atraso = (fecha_entrega - fecha_renta).days - 3
    costo_diario = 12.50 * 1.30
    total = costo_diario * dias_atraso
    imprimir_ticket("Entrega tardía", total)

def menu():
    print("*******************************")
    print("           MENÚ                ")
    print("*******************************")
    print("(1) Compra")
    print("(2) Renta")
    print("(3) Entrega")
    print("*******************************\n")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        compra_peliculas()
    elif opcion == "2":
        renta_peliculas()
    elif opcion == "3":
        entrega_peliculas()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
