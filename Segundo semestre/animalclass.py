#Se crea la clase animal 
class Animal:
    #Atributos
    __cHabitat = ''
    __cColor = ''
    __nPeso = ''
    #Constructor 
    def __init__(self,cHabitat, cColor, nPeso ):
        self.__cHabitat = cHabitat
        self.__cColor = cColor
        self.__nPeso = nPeso
    #Metodos
    def getcHabitat(self):         #Habitat del animal 
        return self.__cHabitat
    def setcHabitat(self, cHabitat):
        self.__cHabitat = cHabitat
    
    def getcColor(self):         #color del animal 
        return self.__cColor
    def setcColor(self, cColor):
        self.__cColor = cColor

    def getnPeso(self):         #Peso del animal 
        return self.__nPeso
    def setnPeso(self, nPeso):
        self.__nPeso = nPeso
#Se crea la sub clase del animal 1 
#Se crea la clase ingeniero 
class Perro(Animal):
    #Atributos 
    cTipoPerro = ''
    cTipoConcentrado = ''
    #Constructor 
    def __init__(self,cTipoPerro, cTipoConcentrado):
        self.cTipoPerro = cTipoPerro
        self.cTipoConcentrado = cTipoConcentrado
    #Metodos
    def getcTipoPerro(self):         #Tipo de perro 
        return self.cTipoPerro
    def setcTipoPerro(self, cTipoPerro):
        self.cTipoPerro = cTipoPerro

    def getcTipoConcentrado(self):         #Tipo de perro 
        return self.cTipoConcentrado
    def setcTipoConcentrado(self, cTipoConcentrado):
        self.cTipoConcentrado = cTipoConcentrado
    #Metodos Adicionales. Se crea el metodo programar 
    def hablar (self):
        return f"""---------------------------------------------
            Soy el animal perro, Mi habitat es: {self.getcHabitat()}
                Mi color es: {self.getcColor()}
                Mi peso es: {self.getnPeso()}kg
                Mi raza es: {self.getcTipoPerro()}
                Mi tipo de concentrado es :{self.getcTipoPerro()}"""
    
class Pescado(Animal):
    #Atributos 
    nTamaño = 0
    nVelocidad = 0
    #Constructor 
    def __init__(self,nTamaño, nVelocidad):
        self.nTamaño = nTamaño
        self.nVelocidad = nVelocidad

    #Metodos
    def getnTamaño(self):         #Tamaño de pescado
        return self.nTamaño
    def setnTamaño(self, nTamaño):
        self.nTamaño = nTamaño

    def getnVelocidad(self):         #Velocidad del pescado 
        return self.nVelocidad
    def setnVelocidad(self, nVelocidad):
        self.nVelocidad = nVelocidad
    #Metodos Adicionales. Se crea el metodo hablar  
    def hablar (self):
        return f"""--------------------------------------------------------
        Soy el animal Pescado, Mi habitat es: {self.getcHabitat()}
                Mi color es: {self.getcColor()}
                Mi peso es: {self.getnPeso()}kg
                Mi tamaño es: {self.getnTamaño()}
                Mi velocidad en el agua es :{self.getnVelocidad()}"""
    
class Leon(Animal):
    #Atributos 
    nEdad = 0
    cGenero =''
    #Constructor 
    def __init__(self,nEdad, cGenero):
        self.nEdad = nEdad
        self.cGenero = cGenero

    #Metodos
    def getnEdad(self):         #Edad del leon
        return self.nEdad
    def setnEdad(self, nEdad):
        self.nEdad = nEdad

    def getcGenero(self):         #genero del leon  
        return self.cGenero
    def setcGenero(self, cGenero):
        self.cGenero = cGenero
    #Metodos Adicionales. Se crea el metodo hablar  
    def hablar (self):
        return f"""--------------------------------------------------------------
        Soy el animal León, Mi habitat es: {self.getcHabitat()}
                Mi color es: {self.getcColor()}
                Mi peso es: {self.getnPeso()}kg
                Mi edad es: {self.getnEdad()}
                Mi genero es :{self.getcGenero()}"""
    

