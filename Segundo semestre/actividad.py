import clasepersona         #Importo clase persona 
oPersona = clasepersona.Persona('',0,0)     #Creo el objeto 

cNombre = input("Escribe tu nombre completo: ")     
dFechaNacimiento = input("Escribe tu fecha de Nacimiento (DD/MM/AAAA): ")
nNumDocumento = input("Escribe tu número de documento: ")

oPersona.setcNombre(cNombre)
oPersona.setdFechaNacimiento(dFechaNacimiento)
oPersona.setnNumDocumento(nNumDocumento)

print("------------------------------------------------------")
print(oPersona.mostrar())
if oPersona.esMayorDeEdad == True:
    print(f"Según los datos del usuario {cNombre} esta persona es mayor de edad.")
else:
    print(f"Según los datos del usuario {cNombre} esta persona es menor de edad.")

