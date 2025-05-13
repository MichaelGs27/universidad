#Importamos la clase automovil 
import claseautomovil
oAutomovil = claseautomovil.Automovil('','','',0) #Se crea el objeto 


print("-----BIENVENIDO------")
cMarca = input("Escribe la marca de su automovil: ")
cModelo = input("Escribe el modelo de su automovil: ")
cPlaca = input("Ingresa la placa de tu vehiculo: ")
nCilindraje = input("Ingresa el cilindraje de tu vehiculo: ")
nVelocidad = int(input("Escribe la velocidad de tu automovil : "))

    #Cambiamos el valor de las variables con la ayuda del set 
oAutomovil.setcMarca(cMarca)
oAutomovil.setcModelo(cModelo)
oAutomovil.setcPlaca(cPlaca)
oAutomovil.setnCilindraje(nCilindraje)
oAutomovil.setnVelocidad(nVelocidad)            #Cambiamos los valores actuales con el set 

while True:
    cOpcion = input("""Escribe si deseas 
                        1. Acelerar
                        2. Frenar 
                        3. Salir: """)       #Pedimos los datos del automovil al usuario 

    #Se crea un if para saber que opción elige 
    if cOpcion == "1":
        print("Su velocidad aumento 10km/h")        #Opción la que aumenta la velocidad 
        nVelocidad = oAutomovil.acelerar()          #Se cambia la velocidad con el metodo acelerar  
        print(oAutomovil.mostrar())   
    elif cOpcion == "2":
        print("Su velocidad disminuyo 5km/h")       #Opción que disminuye la velocidad 
        nVelocidad = oAutomovil.frenar()    
        print(oAutomovil.mostrar())        #Se cambia la velocidad con el metodo frenar 
    elif cOpcion=="3":
        print(oAutomovil.mostrar())
        break
    else:
        continuar = input("Presione Enter para volver al menú...")
        print("Opción Invalida.")   #Si ingresa un caracter invalido, sale este mensaje
