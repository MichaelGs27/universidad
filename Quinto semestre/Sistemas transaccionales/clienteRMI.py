import Pyro5.api #Se importa Pyro5 para poder consumir servicios remotos 

#Solicita al usuario que introduzca el URI del servidor 
uri = input("Ingrese el URI del servicio modalidad: ")

#Crea un "proxy" que permite al cliente llamar métodos remosots como si fueran locales
tipos_id_remoto = Pyro5.api.Proxy(uri)

try:
    #Solicita al usuario que ingrese el código que desea consultar 
    codigo = input("Ingrese el codigo de tipo de identificación (ej: CC, TI, CE, PA): ")

    #Llama remotamente al metodo consultar_descripcion pasando el codigo 
    descripcion = tipos_id_remoto.consultar_descripcion(codigo.upper())
    
    #Muestra la descripción recibida desde el servidor 
    print(f"descripcion: {descripcion}")
    
except Exception as e:
    #Captura y muestra cualquier error ocurrido durante la comunicacion 
    print("Error: consultando el servicio remoto:",e)
