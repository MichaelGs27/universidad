import threading
from mysql.connector import Error
from Logica import insertar_tipo_id
#Solicita datos por consola
codigo = input("Ingrese e código del tipo de identificación: ")
descripcion = input("Ingrese la descripcion del tipo de identificación: ")

#Crea y lanza el hilo que hace la inserción
hilo = threading.Thread(target=insertar_tipo_id, args=(codigo,descripcion)) 
hilo.start()
hilo.join()

print("n\ inserción finalizada con hilo.")