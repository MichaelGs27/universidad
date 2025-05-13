#crear lista
Id = []
Nombre = []
Apellido = []
Telefono=[]
Email = []
print("-------------------Bienvenido-------------------")
while True:         #Se inicia el bucle
    print("-----------------------------------")
    print("1 Insertar \n2 Actualizar \n3 Consultar \n4 Eliminar \n5 Salir")
    options = int(input("Digite su opción: "))   #Opcion para saber que ingresa el usuario
    if options==1:      #Opcion 1, insertar
        #Se agregan los datos con el .append() 
        Id.append(input("Digite su ID: "))
        Nombre.append(input("Digite su nombre: "))
        Apellido.append(input("Digite su apellido: "))
        Telefono.append(input("Digite su telefono: "))
        Email.append(input("Digite su email: "))
    elif options==2:    #Opcion 2, Actualizar
        buscarID = input("Digite el ID que desea actualizar: ")    #Busca el id para poder actualizar
        if buscarID in Id:
            index = Id.index(buscarID)      #.index() para buscar el indice en la lista
            #Se actualizan los datos 
            Nombre[index] = input("Nuevo nombre: ")
            Apellido[index] = input("Nuevo apellido: ")
            Telefono[index] = input("Nuevo telefono: ")
            Email[index] = input("Nuevo email: ")
            print("Registro actualizado exitosamente.")
        else:
            print("El ID no existe.")   #Si no se encuentra el indice aparece este mensaje
    elif options==3:    #Opción 3, consultar
        buscarID = input("Digite el ID que desea consultar: ")  #Busca el id para poder consultar
        if buscarID in Id:
            index = Id.index(buscarID)      #.index() para buscar el indice en la lista
            #Muestra los datos en pantalla
            print("ID:", Id[index])
            print("Nombre:", Nombre[index])
            print("Apellido:", Apellido[index])
            print("Telefono:", Telefono[index])
            print("Email:", Email[index])
        else:
            print("El ID no existe.")   #Si no se encuentra el indice aparece este mensaje
    elif options ==4:   #Opción 4, para eliminar 
        buscarID = input("Digite el ID que desea eliminar: ")   #.index() para buscar el indice en la lista
        #Se elimina la lista 
        if buscarID in Id:
            index = Id.index(buscarID)
            del Id[index]
            del Nombre[index]
            del Apellido[index]
            del Telefono[index]
            del Email[index]
            print("Registro eliminado exitosamente.")
        else:
            print("El ID no existe.")   #Si no se encuentra el indice aparece este mensaje
    elif options==5:    #Opcion 5, Salir 
        break   #Termina el bucle
    else:
        print("Opción Invalida.")   #Si ingresa un caracter invalido, sale este mensaje