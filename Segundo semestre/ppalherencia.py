#Cargar la libreria 
import LibreriaHerencia
#Creo el objeto
oTecnico = LibreriaHerencia.Tecnico('','')
try:
    nNumDocumento = input("Digite su número de documento: ")
    cNombreCompleto = input("Digite su nombre completo: ")
    nSueldo = input("Digite su sueldo: ")
    nFechaNacimiento = input("Digite su fecha de nacimiento (DD/MM/AAAA):")
    cLugarTrabajo = input("Escribe tu lugar de trabajo: ")
    cPaisVivienda = input("Escribe tu país de residencia: ")
except:
    print("Digite una opción valida.")
else:
    #Cambio los valores con el set
    oTecnico.setnNumDocumento(nNumDocumento)
    oTecnico.setcNombreComleto(cNombreCompleto)
    oTecnico.setdFechaNacimiento(nFechaNacimiento)
    oTecnico.setnSueldo(nSueldo)
    oTecnico.setcLugarTrabajo(cLugarTrabajo)
    oTecnico.setcPaisVivienda(cPaisVivienda)
    #Se muestra en pantalla los datos que ingreso el usuario
    print(f""" ---------Datos del usuario----------
        El número de documento es: {oTecnico.getnNumDocumento()}
        Su nombre es: {oTecnico.getcNombreComleto()}
        Su sueldo actualmente es: {oTecnico.getnSueldo()}
        Su fecha de nacimiento es: {oTecnico.getdFechaNacimiento()}
        Su lugar de trabajo es: {oTecnico.getcLugarTrabajo()}
        El país de su residencia es: {oTecnico.getcPaisVivienda()}""")



