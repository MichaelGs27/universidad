#La funciones calculara devuelve el resultado de una operacion 
#Recibe como parametros:
#nNum1 = float 
#nNum2 = float
#nOpcion = signo +,-,*,/
"""def Calculadora(nNum1, nNum2,nOperacion,):
    nResultado=0.0
    if nOperacion=="+":
        nResultado = nNum1+nNum2
    elif nOperacion=="-":
        nResultado = nNum1-nNum2
    elif nOperacion=="*":
        nResultado = nNum1*nNum2
    elif nOperacion=="/":
        nResultado = nNum1/nNum2
    return nResultado """


#Cargo la libreria clases
import libreriadeclases

#Creo en el objeto de la clase tipo identificación, para referenciar que es un objeto lo escribo "oTipo"
oTipoId = libreriadeclases.TipoId("Cc","Cedula de ciudadania")

cTipoId = input("Ingrese el tipo de identificación:  ")
cNombreTipo = input("Ingrese el nombre del tipo de identificación: ")

oTipoId.setnCodTipoId(cTipoId)
oTipoId.setnNombreTipoId(cNombreTipo)

print(f'El tipo de documento ingresado es: ', oTipoId.getnCodTipoId(), oTipoId.getnNombreTipoId())

