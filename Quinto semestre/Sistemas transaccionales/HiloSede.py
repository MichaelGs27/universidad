import threading
import mysql.connector
from mysql.connector import Error
from Logica import insertar_tipo_sede
from Logica import actualizar_tipo_sede

Menu = 0
Salir  = "Si" or "si"
while Menu == 0:
    try:
        nOpcion = int(input("""--------------MENU Sede-----------------
                            0. Salir
                            1. Crear Sede
                            2. Actualizar Sede
                            3. Consultar Sede
                            4. Eliminar Sede: """))
    except:
        print("Valores invalidos.")
    else:   
        if nOpcion ==1:
            #Solcita datos por consola
            codigo = input("Digite el codigo de la sede: ")
            descripcion = input("Digite el nombre de la sede: ")

            #Crea y lamza el hilo que hace la inserción
            hilo = threading.Thread(target=insertar_tipo_sede, args=(codigo, descripcion))
            hilo.start()
            hilo.join()
            print("\n Inserción finalizada con hilo")
        #Opcion Actualiar 
        elif nOpcion == 2:

            #Solcita datos por consola
            codigo = input("Digite el codigo de la sede: ")
            descripcion = input("Digite el nombre nuevo de la sede: ")

            #Crea y lamza el hilo que hace la inserción
            hilo = threading.Thread(target=actualizar_tipo_sede, args=(codigo, descripcion))
            hilo.start()
            hilo.join()
            print("\n Inserción finalizada con hilo")
        elif nOpcion == 0:
                Salir = str(input("¿Deseas salir de programa?(Si/No): "))
                if Salir == 'Si' or 'si':
                        print("Hasta luego...")   
                        break                
                else:
                    print("Sigues en el programa...")
        else:
                print("Opcion invalida, intente de nuevo")