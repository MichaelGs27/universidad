#Creamos la clase motocicleta 
from datetime import datetime, timedelta
class Motocicleta:
    #Se crean los atributos 
    cNuevo = '' 
    cColor = ''
    cMatricula = ''
    nCombustibleLitros = 10
    nNumeroRuedas = 2
    cMarca = ''
    cModelo = 0
    dFechaFabricacion = 0
    nVelocidadPunta = ''
    nPeso = 0.0
    cMotor = False
    nValor = 20000000.00
    nGasolina = 0
    #Constructor
    def __init__(self,cNuevo, cColor, cMatricula, nCombustibleLitros, nNumeroRuedas, cMarca, cModelo, dFechaFabricacion, nVelocidadPunta, nPeso, cMotor,nValor,nGasolina ):
        self.cNuevo = cNuevo
        self.cColor = cColor
        cMatricula = cMatricula
        self.nCombustibleLitros = nCombustibleLitros
        self.nNumeroRuedas = nNumeroRuedas
        self.cMarca = cMarca
        self.cModelo = cModelo
        self.dFechaFabricacion = dFechaFabricacion
        self.nVelocidadPunta = nVelocidadPunta
        self.nPeso = nPeso
        self.cMotor = False 
        self.nValor = nValor
        self.nGasolina = nGasolina
    #metodos
    def getcNuevo(self):       #Nueva motocicleta
        return self.cNuevo
    def setcNuevo(self, cNuevo):
        self.cNuevo = cNuevo
    
    def getcColor(self):           #Color de la moto
        return self.cColor
    def setcColor(self, cColor):
        self.cColor = cColor

    def getcMatricula(self):         #Matricula de la moto  
        return self.cMatricula
    def setcMatricula(self, cMatricula):
        self.cMatricula = cMatricula
    
    def getnCombustibleLitros(self):       #Combustible litros 
        return self.nCombustibleLitros
    def setnCombustibleLitros(self, nCombustibleLitros):
        self.nCombustibleLitros = nCombustibleLitros
    
    def getnNumeroRuedas(self):           #Números de ruedas 
        return self.nNumeroRuedas
    def setnNumeroRuedas(self, nNumeroRuedas):
        self.nNumeroRuedas = nNumeroRuedas

    def getcMarca(self):         #Marca de la moto  
        return self.cMarca
    def setcMarca(self, cMarca):
        self.cMarca = cMarca

    def getcModelo(self):         #Modelo de la moto 
        return self.cModelo
    def setcModelo(self, cModelo):
        self.cModelo = cModelo
    
    def getdFechaFabricacion(self):       #Fecha de fabricación de la moto 
        return self.dFechaFabricacion
    def setdFechaFabricacion(self, dFechaFabricacion):
        self.dFechaFabricacion = dFechaFabricacion
    
    def getnVelocidadPunta(self):           #Velocidad de punta de la moto 
        return self.nVelocidadPunta
    def setnVelocidadPunta(self, nVelocidadPunta):
        self.nVelocidadPunta = nVelocidadPunta

    def getnPeso(self):         #Peso de la moto
        return self.nPeso
    def setnPeso(self, nPeso):
        self.nPeso = nPeso

    def getcMotor(self):         #Motor de la moto
        return self.cMotor
    def setcMotor(self, cMotor):
        self.cMotor = False 

    def getnValor(self):         #Valor de la moto
        return self.nValor
    def setnValor(self, nValor):
        self.nValor = nValor   

    def getnGasolina(self):         #Cantidad de gasolina que ingresa el usuario 
        return self.nGasolina
    def setnGasolina(self, nGasolina):
        self.nGasolina = nGasolina   
#Metodo adicional para arrancar la moto
    def arrancar(self):
        if self.cMotor is False:
            cRespuesta = input("""¿Quieres arrancar el motor? 
            Si. 
            No. : """)
            if cRespuesta.lower() == "si":  #Utilizamos el .lower() para convertir la cadena de texto en minuscula.
                self.cMotor = "si"
                return "El motor ha arrancado."
            else:
                return "No se ha arrancado el motor."
        else:
            return "El motor ya estaba en marcha." 
#Metodo adcional para detener la moto
    def detener(self):
        if self.cMotor is False:
            cRespuesta = input("""¿Quieres detener el motor? 
            Si. 
            No. : """)
            if cRespuesta.lower() == "si":      #Utilizamos el .lower() para convertir la cadena de texto en minuscula.
                self.cMotor = "si"
                return "El motor se ha detenido."
            else:
                return "No se ha detenido el motor."
        else:
            return "El motor ya estaba detenido."   
#Se crea el metodo para la información del tanque
    def infoTanque (self):
        cMarca = self.getcMarca()
        cModelo = self.getcModelo()
        return f"La motocicleta de marca {cMarca} y modelo {cModelo} actualmente tiene 10 litros de gasolina y su capacidad maxima es 20, le faltan 10 litros de gasolina para llenar el tanque."
    #Se crea el metodo para dar el valor de la moto 
    def valor (self):
        nValor = self.getnValor()
        cMarca = self.getcMarca()
        cModelo = self.getcModelo()
        return f"""----Precio de la Moto-------
La motocicleta de marca {cMarca} y modelo {cModelo} actualmente tiene un precio de ${nValor}"""
    #Se crea el metodo para tanquear la moto 
    def tanquear (self):
        if self.getnGasolina() <= 10:
            nGasolina = self.getnGasolina() + self.getnCombustibleLitros()
            return f"Usted tiene {nGasolina} litros de gasolina." 
        elif self.getnGasolina() >10:
            return f"No puede pasarse de gasolina, ingrese un valor valido."
    #Se crea el motodo info moto para mostrar toda la informacion de la moto
    def infomoto (self):
        nCombustible = self.getnCombustibleLitros() + self.getnGasolina()
        return f"""---------------------------------------------------------------
Su moto es nueva: {self.getcNuevo()}
La fecha de salida de su moto es: {self.getdFechaFabricacion()}
El número de ruedas de su moto es: {self.getnNumeroRuedas()}
El color de su moto es: {self.getcColor()}
La matricula de su moto es: {self.getcMatricula()}
La marca de su moto es: {self.getcMarca()}
El modelo de su moto es: {self.getcModelo()}
La velocidad punta es: {self.getnVelocidadPunta()} km/h
El peso de su moto es: {self.getnPeso()} kg
El combustible de su moto es: {nCombustible}"""  
#Se crea la clase Cuatrimoto heredando los atributos de motocicleta
class Cuatrimoto(Motocicleta):
    #Atributos
    nNumeroRuedas = 4
    nPeso = 5000
    #Constructor
    def __init__(self,nNumeroRuedas,nPeso):
        self.nNumeroRuedas = nNumeroRuedas
        self.nPeso = nPeso

    def getnNumeroRuedas(self):           #Números de ruedas 
        return self.nNumeroRuedas
    def setnNumeroRuedas(self, nNumeroRuedas):
        self.nNumeroRuedas = nNumeroRuedas

    def getnPeso(self):         #Peso de la moto
        return self.nPeso
    def setnPeso(self, nPeso):
        self.nPeso = nPeso
#Se crea un metodo adicional arrancar
    def arrancar(self):
        if self.cMotor is False:
            cRespuesta = input("""¿Quieres arrancar el motor? 
            Si. 
            No. : """)
            if cRespuesta.lower() == "si":  #Utilizamos el .lower() para convertir la cadena de texto en minuscula.
                self.cMotor = "si"
                return "El motor ha arrancado."
            else:
                return "No se ha arrancado el motor."
        else:
            return "El motor ya estaba en marcha." 
#Metodo adcional para detener la moto
    def detener(self):
        if self.cMotor is False:
            cRespuesta = input("""¿Quieres detener el motor? 
            Si. 
            No. : """)
            if cRespuesta.lower() == "si":      #Utilizamos el .lower() para convertir la cadena de texto en minuscula.
                self.cMotor = "si"
                return "El motor se ha detenido."
            else:
                return "No se ha detenido el motor."
        else:
            return "El motor ya estaba detenido."
        
#Se crea un metodo adicional detener
    def infoTanque (self):
        cMarca = self.getcMarca()
        cModelo = self.getcModelo()
        return f"La cuatrimoto de marca {cMarca} y modelo {cModelo} actualmente tiene  15 litros de gasolina y su capacidad maxima es 30, le faltan 15 litros de gasolina para llenar el tanque."
#Se crea el metodo para tanquear la moto 
    def tanquear (self):
        if self.getnGasolina() <= 15:
            nGasolina = self.getnGasolina() + self.getnCombustibleLitros()
            return f"Usted tiene {nGasolina} litros de gasolina." 
        elif self.getnGasolina() >30:
            return f"No puede pasarse de gasolina, ingrese un valor valido."
#Se crea el motodo info moto para mostrar toda la informacion de la moto
    def infocuatrimoto (self):
        nCombustible = self.getnCombustibleLitros() + self.getnGasolina()
        return f"""---------------------------------------------------------------
Su cuatrimoto es nueva: {self.getcNuevo()}
La fecha de salida de su cutrimoto es: {self.getdFechaFabricacion()}
El número de ruedas de su cuatrimoto es: {self.getnNumeroRuedas()}
El color de su cuatrimoto es: {self.getcColor()}
La matricula de su cuatrimoto es: {self.getcMatricula()}
La marca de su cuatrimoto es: {self.getcMarca()}
El modelo de su cuatrimoto es: {self.getcModelo()}
La velocidad punta es: {self.getnVelocidadPunta()} km/h
El peso de su cuatrimoto es: {self.getnPeso()} kg
El combustible de su cuatrimoto es: {nCombustible}"""

       