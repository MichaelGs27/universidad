#Importamos la clase automovil 
import claseautomovil
oAutomovil = claseautomovil.Moto(0,'') #Se crea el objeto 


print("-----BIENVENIDO------")
cMarca = input("Escribe la marca de su automovil: ")
cModelo = input("Escribe el modelo de su automovil: ")
nCilindraje = input("Ingresa el cilindraje de tu vehiculo: ")
nNumRuedas = input("Ingrese cuantas ruedas tiene su vehiculo: ")
cPlaca = input("Ingresa la placa de tu vehiculo: ")
nVelocidad = int(input("Escribe la velocidad de tu automovil : "))

    #Cambiamos el valor de las variables con la ayuda del set 
oAutomovil.setcMarca(cMarca)
oAutomovil.setcModelo(cModelo)
oAutomovil.setcPlaca(cPlaca)
oAutomovil.setnCilindraje(nCilindraje)
oAutomovil.setnNumRuedas(nNumRuedas)
oAutomovil.setnVelocidad(nVelocidad)            #Cambiamos los valores actuales con el set 

cOpcion = input("""Escribe si deseas 
                    1. Acelerar
                    2. Frenar:  """)       #Pedimos los datos del automovil al usuario 

#Se crea un if para saber que opción elige 
if cOpcion == "1":
    print("Su velocidad aumento 10km/h")        #Opción la que aumenta la velocidad 
    nVelocidad = oAutomovil.acelerar()          #Se cambia la velocidad con el metodo acelerar
elif cOpcion == "2":
    print("Su velocidad disminuyo 5km/h")       #Opción que disminuye la velocidad 
    nVelocidad = oAutomovil.frenar()            #Se cambia la velocidad con el metodo frenar 

print(oAutomovil.infomoto())

