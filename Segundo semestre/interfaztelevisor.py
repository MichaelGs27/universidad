#Se impota la clase 
#Se crea la clase 
class Televisor:
    #Atributos
    __Marca = color = TipoDeTelevisor = ""
    __Tamaño = TamañoDeLaPantalla = 0
    #Constructor
    def __init__(self, __Marca, color, TipoDeTelevisor, __Tamaño, TamañoDeLaPantalla):
        self.__Marca = __Marca
        self.color = color
        self.TipoDeTelevisor = TipoDeTelevisor
        self.__Tamaño = __Tamaño
        self.TamañoDeLaPantalla = TamañoDeLaPantalla

    #Metodos
    def getMarca(self):         #Marca del televisor
        return self.__Marca
    def setMarca(self, Marca):
        self.__Marca = Marca
    
    def getcolor(self):         #Color del televisor 
        return self.color
    def setcolor(self, color):
        self.color = color

    def getTipoDeTelevisor(self):         #Tipo de televisor
        return self.TipoDeTelevisor
    def setTipoDeTelevisor(self, TipoDeTelevisor):
        self.TipoDeTelevisor = TipoDeTelevisor
    
    def getTamaño(self):         #Tamaño del televisor 
        return self.__Tamaño
    def setTamaño(self, Tamaño):
        self.__Tamaño = Tamaño

    def getTamañoDeLaPantalla(self):        #Tamaño de la pantalla del televisor 
        return self.TamañoDeLaPantalla
    def setTamañoDeLaPantalla(self, TamañoDeLaPantalla):
        self.TamañoDeLaPantalla = TamañoDeLaPantalla
#Metodo adicional control remoto
    def ControlRemoto (self):
        return "Control remoto activado"

#Se crea la clase LED 
class Led(Televisor):
    #Atributos
    nBrillo = nResolucion = 0
    #Constructor
    def __init__(self, nBrillo, nResolucion): 
        self.nBrillo = nBrillo
        self.nResolucion = nResolucion
    #Metodos
    def getnBrillo(self):         #Brillo del televisor 
        return self.nBrillo
    def setnBrillo(self, nBrillo):
        self.nBrillo = nBrillo

    def getnResolucion(self):        #Resolución de la pantalla del televisor 
        return self.nResolucion
    def setnResolucion(self, nResolucion):
        self.nResolucion = nResolucion
#Metodo adicional para el control remoto del televisor LED
    def ControlRemoto(self):
        return "Control remoto activado para televisor LED."
    #Metodo acional para mostrar para imprimir los resultados del usuario 
    def mostrar(self):
        return f"""---------------Información del televisor---------------
        La marca de su televisor es: {self.getMarca()}
        El color de su televisor es: {self.getcolor()}
        Su tipo de televisor es: {self.getTipoDeTelevisor()}
        El tamaño de su televisor es: {self.getTamaño()}
        El tamaño de la pantalla de su televisor es: {self.getTamañoDeLaPantalla()}
        El brillo de su televisor es: {self.getnBrillo()}
        La resolución de su televisor es: {self.getnResolucion()}"""
#Se crea la clase SmartTV
class SmartTV(Televisor):
    #Atributos
    cSistemaOperativo = ""
    nCantidadHDMI = 0
    #Constructor
    def __init__(self, cSistemaOperativo, nCantidadHDMI): 
        self.cSistemaOperativo = cSistemaOperativo
        self.nCantidadHDMI = nCantidadHDMI
    #Metodos
    def getcSistemaOperativo(self):         #Sistema operativo del televisor 
        return self.cSistemaOperativo
    def setcSistemaOperativo(self, cSistemaOperativo):
        self.cSistemaOperativo = cSistemaOperativo

    def getnCantidadHDMI(self):        #Cantidad de puertos HDMI del televisor  
        return self.nCantidadHDMI
    def setnCantidadHDMI(self, nCantidadHDMI):
        self.nCantidadHDMI = nCantidadHDMI
#Metodo adicional para el control remoto del Smart TV
    def ControlRemoto(self):
        return "Control remoto activado para televisor SmartTV."
    #Metodo adicional para mostrar para imprimir los resultados del usuario 
    def mostrar(self):
        return f"""---------------Información del televisor---------------
        La marca de su televisor es: {self.getMarca()}
        El color de su televisor es: {self.getcolor()}
        Su tipo de televisor es: {self.getTipoDeTelevisor()}
        El tamaño de su televisor es: {self.getTamaño()}
        El tamaño de la pantalla de su televisor es: {self.getTamañoDeLaPantalla()}
        El sistema operativo de su televisor es: {self.getcSistemaOperativo()}
        La cantidad de HDMI de su televisor es: {self.getnCantidadHDMI()}"""
while True:
    try:
        cOpcion = int(input("""-----------------BIENVENIDO------------------
                        Digita una opción 
                        1. LED 
                        2. SmartTV 
                        3. Salir: """))
    except: 
        print("Digite una opción valida.")
    else:
        if cOpcion == 1:
            oLED = Led(0,0) #Se crea el objeto
            cColor = input("¿Cuál es el color del televisor?: ")
            cTipoTelevisor = input("¿Cuál es el tipo de televisor?: ")
            cTamañoPantalla = input("¿Cuál es el tamaño de la pantalla?: ")
            nBrillo = input("¿Cuál es el brillo del televisor?: ")
            nResolución = input("¿Cuál es la resolución del televisor?: ")
            #Cambiamos el valor 
            oLED.setMarca("Samsung")
            oLED.setcolor(cColor)
            oLED.setTipoDeTelevisor(cTipoTelevisor)
            oLED.setTamaño("42 Pulgadas")
            oLED.setTamañoDeLaPantalla(cTamañoPantalla)
            oLED.setnBrillo(nBrillo)
            oLED.setnResolucion(nResolución)
            print(oLED.mostrar())
            cOpcion1 = int(input("""¿Quieres prender el control remoto? 
                             1.Si  
                             2.No: """))
            if cOpcion1 == 1:
                print(oLED.ControlRemoto())
                break
            else:
                print("Su control remoto no ha sido activado.")
                break
            #Opcion para smart TV
        if cOpcion == 2:
            oSmart = SmartTV(0,0) #Se crea el objeto
            cColor = input("¿Cuál es el color del televisor?: ")
            cTipoTelevisor = input("¿Cuál es el tipo de televisor?: ")
            cTamañoPantalla = input("¿Cuál es el tamaño de la pantalla?: ")
            cSistemaOperativo = input("¿Cuál es el sistema operativo de su televisor?: ")
            nCantidadHDMI = input("¿Cuantas entradas de HDMI tiene su televisor?: ")
            #Cambiamos el valor 
            oSmart.setMarca("Samsung")
            oSmart.setcolor(cColor)
            oSmart.setTipoDeTelevisor(cTipoTelevisor)
            oSmart.setTamaño("42 Pulgadas")
            oSmart.setTamañoDeLaPantalla(cTamañoPantalla)
            oSmart.setcSistemaOperativo(cSistemaOperativo)
            oSmart.setnCantidadHDMI(nCantidadHDMI)
            print(oSmart.mostrar())
            cOpcion1 = int(input("""¿Quieres prender el control remoto? 
                1.Si 
                2.No: """))
            if cOpcion1 == 1:
                print(oSmart.ControlRemoto())
                break
            else:
                print("Su control remoto no ha sido activado.")
                break
        elif cOpcion == 3:
            print("Cerrando el programa...")
            break

