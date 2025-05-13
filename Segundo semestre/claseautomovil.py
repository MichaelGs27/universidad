class Automovil:
    #Se crean los atributos 
    cMarca = ''
    cModelo = ''
    nCilindraje = 0
    nVelocidad = 0
    #Constructor
    def __init__(self, cMarca, cModelo, nCilindraje, nVelocidad):
        self.cMarca = cMarca
        self.cModelo = cModelo
        self.nCilindraje = nCilindraje
        self.nVelocidad = nVelocidad
    #metodos

    def getcMarca(self):         #Marca del automovil
        return self.cMarca
    def setcMarca(self, cMarca):
        self.cMarca = cMarca

    def getcModelo(self):         #Modelo del automovil
        return self.cModelo
    def setcModelo(self, cModelo):
        self.cModelo = cModelo

    def getcPlaca(self):         #Placa del automovil  
        return self.cPlaca
    def setcPlaca(self, cPlaca):
        self.cPlaca = cPlaca

    def getnCilindraje(self):         #Cilindraje del automovil 
        return self.nCilindraje
    def setnCilindraje(self, nCilindraje):
        self.nCilindraje = nCilindraje
    
    def getnVelocidad(self):           #Velocidad del automovil
        return self.nVelocidad
    def setnVelocidad(self, nVelocidad):
        self.nVelocidad = nVelocidad

    #Metodo para acelerar 
    def acelerar (self):
        nVelocidad = self.getnVelocidad()       #Traemos la velocidad que el usuario digito
        nVelocidad = nVelocidad + 10       #Se hace la operacion para la velocidad 
        self.setnVelocidad(nVelocidad)        #Retorna el nuevo valor 

    def frenar (self):      #Metodo frenar 
        nFrenar = self.getnVelocidad()       #Traemos la velocidad que el usuario digito
        nVelocidad = nFrenar - 5        #Se hace la operacion para la velocidad 
        self.setnVelocidad(nVelocidad)          #Retorna el nuevo valor
    
    #Mostrar en pantalla 
    def mostrar (self):
        cMarca = self.getcMarca()
        cModelo = self.getcModelo()
        cPlaca = self.getcPlaca()
        nCilindraje = self.getnCilindraje()
        nVelocidad = self.getnVelocidad()

        return f"""La marca del automovil es: {cMarca} 
        El modelo del automovil es:  {cModelo} 
        La placa de su automovil es: {cPlaca}
        El cilindraje de su automovil es: {nCilindraje}
        La velocidad de tu vehiculo es: {nVelocidad}km/h"""

#Se crea la clase moto heredando la clase automovil
class Moto (Automovil):
    #Atributos
    nNumRuedas = 0
    cPlaca = ''

    #Constructor
    def __init__(self,nNumRuedas, cPlaca):
        self.nNumRuedas = nNumRuedas
        self.cPlaca = cPlaca

    def getnNumRuedas(self):         #Numero de ruedas del automovil
        return self.nNumRuedas
    def setnNumRuedas(self, nNumRuedas):
        self.nNumRuedas = nNumRuedas

    def getcPlaca(self):         #Placa del automovil  
        return self.cPlaca
    def setcPlaca(self, cPlaca):
        self.cPlaca = cPlaca


    def infomoto (self):
        cMarca = self.getcMarca()
        cModelo = self.getcModelo()
        nCilindraje = self. getnCilindraje()
        cPlaca = self.getcPlaca()
        nVelocidad = self.getnVelocidad()
        return f"""La Marca de su moto es: {cMarca}
        El modelo y cilindraje son: {cModelo} , {nCilindraje}
        Número de la placa es: {cPlaca}
        Su nueva velocidad es: {nVelocidad}km/h"""


