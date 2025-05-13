#Importamos la clase 
import clases2
#Se crea el objeto 
oMotocicleta = clases2.Motocicleta('','','',10,2,'',0,0,'',0.0,'',20000000.00,0)
oCuatrimoto = clases2.Cuatrimoto(4,5000)
while True:
    cOpcion1 = int(input("""--------------------BIENVENIDO------------------
    Seleccione una opción 
    1. Moto
    2. Cuatrimoto
    3. Salir: """))
    if cOpcion1 == 1: 
        try:
            #Pedimos los datos al usuario
            cNuevo = input("¿Su moto es nueva?: ")
            cColor = input("Indique el color de la moto: ")
            cMatricula = input("Escribe la matricula de la moto: ")
            cMarca = input("indique la marca de la moto: ")
            cModelo = input("Escribe el modelo de la moto: ")
            nVelocidadPunta = int(input("Escribe la velocidad punta de la moto: "))
            nPeso = input("Escribe el peso de la moto: ")
        except:
            print("Escribe valores validos.")
        else: 
            #Utilizamos el set para cambiar el nombre de las variables
            oMotocicleta.setcNuevo(cNuevo)
            oMotocicleta.setcColor(cColor)
            oMotocicleta.setcMatricula(cMatricula)
            oMotocicleta.setnCombustibleLitros(10)
            oMotocicleta.setnNumeroRuedas(2)
            oMotocicleta.setcMarca(cMarca)
            oMotocicleta.setdFechaFabricacion("27/05/2017")
            oMotocicleta.setcModelo(cModelo)
            oMotocicleta.setnVelocidadPunta(nVelocidadPunta)
            oMotocicleta.setnPeso(nPeso)
            oMotocicleta.setnValor(20000000.00)
            #Imprimimos en pantalla el valor de la moto y la información de la moto.
        print(oMotocicleta.valor())
        print(oMotocicleta.infoTanque())
        #Creamos un while para saber cuanto desea tanquear la moto
        while True:
            cOpcion = int(input("""Escribe si deseas
                                1. Arrancar 
                                2. Detener
                                3. Tanquear 
                                4. Salir: """))     #Pedimos los datos del automovil al usuario 
            #Se crea un if para saber que opción elige 
            if  cOpcion == 1:
                print(oMotocicleta.arrancar())  #Mostramos en pantalla el resultado
                continuar = input("Presione Enter para volver al menú...")
            elif cOpcion ==2:
                print(oMotocicleta.detener())       #Mostramos en pantalla el resultado
                continuar = input("Presione Enter para volver al menú...")
            elif cOpcion == 3:
                nGasolina = int(input("""------------------------------------------------------------------
                ¿Cuantos Litros desea tanquear? """))        #Pedimos la cantidad de litros a tanquear 
                oMotocicleta.setnGasolina(nGasolina)        #Cambiamos el valor de la variable por la cantidad que ingreso el usuario 
                print(oMotocicleta.tanquear())      #Mostramos en pantalla el resultado
                continuar = input("Presione Enter para volver al menú...")
            elif cOpcion == 4:
                print("Volviendo al menú principal...")
                #Mostramos los valores ingresados en pantalla
                print(oMotocicleta.infomoto())
                break
            else:
                print("Opción inválida")
                continuar = input("Presione Enter para volver al menú...")
    elif cOpcion1 == 2:
        #Clase cuatrimoto
        try:
            #Pedimos los datos al usuario
            cNuevo = input("¿La cuatrimoto es nueva?: ")
            cColor = input("Indique el color de la cuatrimoto: ")
            cMatricula = input("Escribe la matricula de la cuatrimoto: ")
            cMarca = input("indique la marca de la cuatrimoto: ")
            cModelo = input("Escribe el modelo de la cuatrimoto: ")
            nVelocidadPunta = int(input("Escribe la velocidad punta de la cuatrimoto: "))
        except:
            print("Escribe valores validos.")
        else: 
            #Utilizamos el set para cambiar el nombre de las variables
            oCuatrimoto.setcNuevo(cNuevo)
            oCuatrimoto.setcColor(cColor)
            oCuatrimoto.setcMatricula(cMatricula)
            oCuatrimoto.setnCombustibleLitros(15)
            oCuatrimoto.setnNumeroRuedas(4)
            oCuatrimoto.setcMarca(cMarca)
            oCuatrimoto.setdFechaFabricacion("27/05/2017")
            oCuatrimoto.setcModelo(cModelo)
            oCuatrimoto.setnVelocidadPunta(nVelocidadPunta)
            oCuatrimoto.setnPeso(5000)
        #Se muestra en pantalla la información del tanque.
        print(oCuatrimoto.infoTanque())
        while True:
            cOpcion = int(input("""Escribe si deseas
                                1. Arrancar 
                                2. Detener
                                3. Tanquear 
                                4. Salir: """))     #Pedimos los datos del automovil al usuario 
            #Se crea un if para saber que opción elige 
            if  cOpcion == 1:
                print(oCuatrimoto.arrancar())  #Mostramos en pantalla el resultado
                continuar = input("Presione Enter para volver al menú...")
            elif cOpcion ==2:
                print(oCuatrimoto.detener())       #Mostramos en pantalla el resultado
                continuar = input("Presione Enter para volver al menú...")
            elif cOpcion == 3:
                nGasolina = int(input("""------------------------------------------------------------------
                ¿Cuantos Litros desea tanquear? """))        #Pedimos la cantidad de litros a tanquear 
                oCuatrimoto.setnGasolina(nGasolina)        #Cambiamos el valor de la variable por la cantidad que ingreso el usuario 
                print(oCuatrimoto.tanquear())      #Mostramos en pantalla el resultado
                continuar = input("Presione Enter para volver al menú...")
            elif cOpcion == 4:
                print("Volviendo al menú principal...")
                #Mostramos los valores ingresados en pantalla
                print(oCuatrimoto.infocuatrimoto())
                break
    elif cOpcion1 == 3:
        print("Vuelva pronto.")
        break


            
        
