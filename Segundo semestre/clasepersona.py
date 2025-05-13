#Importamos la libreria datetime para las fecha
from datetime import datetime, timedelta
#Se crea la clase Persona 
class Persona:
    #Atributos
    cNombre = ''
    dFechaNacimiento = 0
    nNumDocumento = 0

     #Constructor

    def __init__(self,cNombre, dFechaNacimiento, nNumDocumento):
        self.cNombre = cNombre
        self.dFechaNacimiento = dFechaNacimiento
        self.nNumDocumento = nNumDocumento

    def getcNombre(self):       #Nombre de la persona 
        return self.cNombre
    def setcNombre(self, cNombre):
        self.cNombre = cNombre
    
    def getdFechaNacimiento(self):           #Fecha de Nacimiento de la persona 
        return self.dFechaNacimiento
    def setdFechaNacimiento(self, dFechaNacimiento):
        self.dFechaNacimiento = dFechaNacimiento

    def getnNumDocumento(self):         #Documento de la persona 
        return self.nNumDocumento
    def setnNumDocumento(self, nNumDocumento):
        self.nNumDocumento = nNumDocumento
    
    def esMayorDeEdad (self):           #Calculo si es mayor de Edad 
        dFechaNaci = self.getdFechaNacimiento()
        dFechaNaci = dFechaNaci
        nFechaActual = datetime.now()       #Fecha de hoy
        nFechaNacimiento = datetime.strptime(dFechaNaci, "%d/%m/%Y")
        nEdad = nFechaActual.year - nFechaNacimiento.year
        if nEdad >= 18:
            nMayorEdad = True
        else:
            nMayorEdad = False
        return nMayorEdad
    
    def mostrar (self):
        cPersona = self.getcNombre()
        dFechaNacimiento = self.getdFechaNacimiento()
        nNumDocumento = self.getnNumDocumento()
        return f"El nombre de la persona es {cPersona} La fecha de nacimiento es:  {dFechaNacimiento} El número de documento es: {nNumDocumento}"