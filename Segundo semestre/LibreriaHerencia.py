#Se crea la clase persona 
class Persona:
    #Atributos 
    __nNumDocumento = ''
    __cNombreComleto = ''
    __dFechaNacimiento = ''
    #Constructor 
    def __init__(self,nNumDocumento, cNombreComleto,dFechaNacimiento):
        self.__nNumDocumento = nNumDocumento
        self.__cNombreComleto = cNombreComleto
        self.__dFechaNacimiento = dFechaNacimiento
    #Metodos
    def getnNumDocumento(self):       #Documento de la persona 
        return self.__nNumDocumento
    def setnNumDocumento(self, nNumDocumento):
        self.__nNumDocumento = nNumDocumento
    
    def getcNombreComleto(self):           #Nombre completo de la persona 
        return self.__cNombreComleto
    def setcNombreComleto(self, cNombreComleto):
        self.__cNombreComleto = cNombreComleto

    def getdFechaNacimiento(self):         #Fecha de nacimiento de la persona 
        return self.__dFechaNacimiento
    def setdFechaNacimiento(self, dFechaNacimiento):
        self.__dFechaNacimiento = dFechaNacimiento
    #Metodos adicionales. Se crea el motodo caminar 

    def caminar (self):
        return 'Estoy caminando.'
    
#Se crea la clase ingeniero 
class Ingeniero(Persona):
    #Atributos 
    nSueldo = 0.0
    #Constructor 
    def __init__(self,nSueldo):
        self.nSueldo = nSueldo
    #Metodos
    def getnSueldo(self):         #Sueldo de la persona 
        return self.nSueldo
    def setnSueldo(self, nSueldo):
        self.nSueldo = nSueldo
    #Metodos Adicionales. Se crea el metodo programar 
    def programar (self):
        return 'Soy programador freeLance.'
    
#Se crea la clase Tecnico 
class Tecnico(Ingeniero):
    #Atributos 
    cLugarTrabajo = ''
    cPaisVivienda = ''
    #Constructor 
    def __init__(self,cLugarTrabajo, cPaisVivienda ):
        self.cLugarTrabajo = cLugarTrabajo
        self.cPaisVivienda = cPaisVivienda
    #Metodos
    def getcLugarTrabajo(self):         #Lugar de trabajo de la persona 
        return self.cLugarTrabajo
    def setcLugarTrabajo(self, cLugarTrabajo):
        self.cLugarTrabajo = cLugarTrabajo
    
    def getcPaisVivienda(self):         #Lugar de trabajo de la persona 
        return self.cPaisVivienda
    def setcPaisVivienda(self, cPaisVivienda):
        self.cPaisVivienda = cPaisVivienda





