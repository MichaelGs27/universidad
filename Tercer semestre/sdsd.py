Id = []
Nombre = []
Apellido = []
Telefono = []
Email = []

def insertar():
    Id.append(input("Digite su ID: "))
    Nombre.append(input("Digite su nombre: "))
    Apellido.append(input("Digite su apellido: "))
    Telefono.append(input("Digite su telefono: "))
    Email.append(input("Digite su email: "))

def consultar():
    buscar_id = input("Digite el ID que desea consultar: ")
    if buscar_id in Id:
        index = Id.index(buscar_id)
        print("ID:", Id[index])
        print("Nombre:", Nombre[index])
        print("Apellido:", Apellido[index])
        print("Telefono:", Telefono[index])
        print("Email:", Email[index])
    else:
        print("El ID no existe.")

def actualizar():
    buscar_id = input("Digite el ID que desea actualizar: ")
    if buscar_id in Id:
        index = Id.index(buscar_id)
        Nombre[index] = input("Nuevo nombre: ")
        Apellido[index] = input("Nuevo apellido: ")
        Telefono[index] = input("Nuevo telefono: ")
        Email[index] = input("Nuevo email: ")
        print("Registro actualizado exitosamente.")
    else:
        print("El ID no existe.")

def eliminar():
    buscar_id = input("Digite el ID que desea eliminar: ")
    if buscar_id in Id:
        index = Id.index(buscar_id)
        del Id[index]
        del Nombre[index]
        del Apellido[index]
        del Telefono[index]
        del Email[index]
        print("Registro eliminado exitosamente.")
    else:
        print("El ID no existe.")

while True:
    print("\n1 Insertar \n2 Actualizar \n3 Consultar \n4 Eliminar \n5 Salir")
    opcion = int(input("Digite su opción: "))
    if opcion == 1:
        insertar()
    elif opcion == 2:
        actualizar()
    elif opcion == 3:
        consultar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        break
    else:
        print("Opción inválida.")
