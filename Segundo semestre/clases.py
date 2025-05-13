#Clase 
from typing import Any
import datetime
from datetime import date 
from datetime import timedelta


class TipoId:
    #Atributos
    nCodTipoId = ''
    nNombreTipoId = ''
  
    #Crear Constructor 
    def __init__(self,nCodTipoId,nNombreTipoId):
        self.nCodTipoId = nCodTipoId
        self.nNombreTipoId = nNombreTipoId

    #Metodos
    def getnCodTipoId(self):
        return self.nCodTipoId
    
    def setnCodTipoId(self, nCodTipoId ):
        self.nCodTipoId=nCodTipoId

    def getnNombreTipoId(self):
        return self.nNombreTipoId
    
    def setnNombreTipoId(self, nNombreTipoId ):
        self.nNombreTipoId=nNombreTipoId

#Clase Libro 
class Libros:
    cCodLibro = ''
    cAutor = ''
    nNumPag = 0
    cCategoria = ''
    nAñoPublicacion = 0
    cNomLibro = ''
    cEstado = ''
    cVitualFisico = ''
    cIdioma = ''
    cEditoria = ''

    #Constructor
    def __init__(self, cCodLibro, cAutor, nNumPag, cCategoria, nAñoPublicacion, cNomLibro, cEstado, cVitualFisico, cIdioma, cEditoria ):
        self.nCodLibro = cCodLibro
        self.nAutor = cAutor
        self.nNumPag = nNumPag
        self.nCategoria = cCategoria
        self.nAñoPublicacion = nAñoPublicacion
        self.nNomLibro = cNomLibro
        self.nEstado = cEstado
        self.nVitualFisico = cVitualFisico
        self.nIdioma = cIdioma
        self.nEditoria = cEditoria

    #Metodos 
    def getcCodLibro(self):     #Codigo de libro
        return self.cCodLibro
    
    def setcCodLibro(self, cCodLibro ):
        self.cCodLibro=cCodLibro
    
    def getcNomLibro (self):            #Nombre de libro 
        return self.cNomLibro
    
    def setcNomLibro (self, cNomLibro  ):
        self.cNomLibro = cNomLibro

    def getcAutor(self):            #Autor 
        return self.cAutor
    
    def setcAutor(self, cAutor ):
        self.cAutor=cAutor
    
    def getnNumPag(self):           #Numero de pagina
        return self.nNumPag
    
    def setnNumPag(self, nNumPag ):
        self.nNumPag=nNumPag
    
    def getcCategoria (self):           #Categoria 
        return self.cCategoria 
    
    def setcCategoria (self, cCategoria  ):
        self.cCategoria = cCategoria 
    
    def getnAñoPublicacion (self):          #Año publicacion
        return self.nAñoPublicacion
    
    def setnAñoPublicacion (self, nAñoPublicacion  ):
        self.nAñoPublicacion = nAñoPublicacion

    def getcEstado (self):            #Estado 
        return self.cEstado
    
    def setcEstado (self, cEstado  ):
        self.cEstado = cEstado
    
    def getcVitualFisico  (self):            #Virtual fisico
        return self.cVitualFisico 
    
    def setcVitualFisico  (self, cVitualFisico   ):
        self.cVitualFisico  = cVitualFisico 

    def getcIdioma  (self):            #Idioma del libro nEditoria
        return self.cIdioma 
    
    def setcIdioma  (self, cIdioma   ):
        self.cIdioma  = cIdioma

    def getcEditoria  (self):            #Editoria
        return self.cEditoria 
    
    def setcEditoria  (self, cEditoria   ):
        self.cEditoria  = cEditoria 

#Clase persona 

class Persona:
    cNumID = ''
    cNombreApellido = ''
    cCodTipoID = '' 
    dFechaNacimiento = ""
    cDireccion = ''
    cTelefono = ''
    cEmail = ''

    #Constructor

    def __init__(self, cNumID, cNombreApellido, cCodTipoID, dFechaNacimiento, cDireccion, cTelefono, cEmail ):
        self.cCodTipoID = cCodTipoID
        self.cNumID = cNumID
        self.cNombreApellido = cNombreApellido
        self.dFechaNacimiento = dFechaNacimiento
        self.cDireccion = cDireccion
        self.cTelefono = cTelefono
        self.cEmail = cEmail

    #Metodos 
    def getcCodTipoID(self):    #Codigo del tipo de identificación
        return self.cCodTipoID
    def setcNumID(self, cCodTipoID ):
        self.cCodTipoID = cCodTipoID

    def getcNumID(self):    #Numero de identificación
        return self.cNumID
    def setcNumID(self, cNumID ):
        self.cNumID = cNumID
    
    def getcNombreApellido(self):            #Nombre y apellido de la persona 
        return self.cNombreApellido
    def setcNomLibro (self, cNombreApellido ):
        self.cNombreApellido = cNombreApellido
    
    def getdFechaNacimiento(self):            #Nombre y apellido de la persona 
        return self.dFechaNacimiento
    def setdFechaNacimiento(self, dFechaNacimiento ):
        self.dFechaNacimiento = dFechaNacimiento
     
    def getcDireccion(self):            #Direccion de la casa 
        return self.cDireccion
    def setcDireccion(self, cDireccion ):
        self.cDireccion = cDireccion
    
    def getcTelefono(self):            #Telefono de la persona 
        return self.cTelefono
    def setcTelefono(self, cTelefono ):
        self.cTelefono = cTelefono
    
    def getcEmail(self):            #Telefono de la persona 
        return self.cEmail
    def setcEmail(self, cEmail ):
        self.cEmail = cEmail

#Clase Movimiento 

class Movimiento:
    cCodMovimiento = ''
    cCodLibro = ''
    dFechaPrestamo = ""
    dFechaEntrega = ""
    cNumID = ''
    nValorLibroPorPerdida = 0.0
    nValorMulta = 0.0

 #Constructor
    def __init__(self, cCodMovimiento, cCodLibro,dFechaPrestamo, dFechaEntrega, cNumID, nValorLibroPorPerdida, nValorMulta):
        self.cCodMovimiento = cCodMovimiento
        self.cCodLibro = cCodLibro
        self.dFechaPrestamo = dFechaPrestamo
        self.dFechaEntrega = dFechaEntrega
        self.cNumID = cNumID
        self.nValorLibroPorPerdida = nValorLibroPorPerdida
        self.nValorMulta = nValorMulta

 #metodos
    def getcCodMovimiento(self):            #Codigo de movimiento
        return self.cCodMovimiento
    def setcCodMovimiento(self, cCodMovimiento ):
        self.cCodMovimiento = cCodMovimiento
    
    def getcCodLibro(self):            #Codigo del libro
        return self.cCodLibro
    def setcCodLibro(self, cCodLibro ):
        self.cCodLibro = cCodLibro

    def getdFechaPrestamo(self):            #Fecha de prestamo
        return self.dFechaPrestamo
    def setdFechaPrestamo(self, dFechaPrestamo ):
        self.dFechaPrestamo = dFechaPrestamo
    
    def getdFechaEntrega(self):            #Fecha de entrega
        return self.dFechaEntrega
    def setdFechaEntrega(self, dFechaEntrega ):
        self.dFechaEntrega = dFechaEntrega

    def getcNumID(self):            #Numero de ID
        return self.cNumID
    def setcNumID(self, cNumID ):
        self.cNumID = cNumID
    
    def getnValorLibroPorPerdida(self):            #Valor por perdida del libro
        return self.nValorLibroPorPerdida
    def setnValorLibroPorPerdida(self, nValorLibroPorPerdida ):
        self.nValorLibroPorPerdida = nValorLibroPorPerdida

    def getnValorMulta(self):            #Valor por multa
        return self.nValorMulta
    def setnValorMulta(self, nValorMulta ):
        self.nValorMulta = nValorMulta

#Clase Cuenta ejercicio
class Cuenta:
    #Atributos
    cTitular = ''
    nCantidad = 0.0 

    #Constructor

    def __init__(self, cTitular, nCantidad):
        self.cTitular = cTitular
        self.nCantidad = nCantidad

    #metodos 

    def getcTitular(self):
        return self.cTitular
    def setcTitular(self, cTitular):
        self.cTitular = cTitular
    
    def getnCantidad(self):
        return self.nCantidad
    def setnCantidad(self, nCantidad):
        self.nCantidad = nCantidad

    def consignar(self,nCantidad):
        nSaldo = 0.0 
        nNuevoSaldo = 0.0
        if nCantidad >0:
            nSaldo = self.getnCantidad()  #Traigo la cantidad de dinero que tiene la cuenta 
            nNuevoSaldo = nSaldo + nCantidad #Sumo el valor que tiene la cuenta mas la nueva cantidad
            self.setnCantidad(nNuevoSaldo)

    def retirar(self,nCantidad):
        nSaldo = 0.0
        if nCantidad > 0:
            nSaldo = self.getnCantidad()
            if nCantidad < nSaldo:
                nNuevoSaldo = nSaldo - nCantidad 
                self.setnCantidad(nNuevoSaldo)