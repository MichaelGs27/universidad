import threading
import mysql.connector
from mysql.connector import Error
from Logica import insertar_multiples

#Listas para almacenar los datos ingresados 
registros =[]
llsalir = True
#Entrada multiples de registro
while llsalir:
    codigo = input("Ingrese el código del tipo de momento (o escriba 'salir' para terminar): ")
    if codigo.strip().lower()=='salir':
        break
    descripcion = input("Ingrese la descripcion del momento: ")
    registros.append((codigo,descripcion))
    print("Registro agregado a la lista.\n")
    
#Crear y ejecuatatr hilos de cada registro
hilos=[]
for codigo,descripcion in registros:
    hilo = threading.Thread(target=insertar_multiples, args=(codigo,descripcion))
    hilos.append(hilo)
    hilo.start()

#Espera que todos los hilos terminen
for hilo in hilos:
    hilo.join()