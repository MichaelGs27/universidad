#se importa la clase 
import animalclass
#Se crean los objetos 
oAnimal1 = animalclass.Perro("","")
oAnimal2 = animalclass.Pescado(0,0)
oAnimal3 = animalclass.Leon(0,"")

Salir = "Si"
while Salir == "Si":
    try:
        cOpcion = int(input("""--------BIENVENIDO
                        Elige una opción
                        1. Perro
                        2. Pescado
                        3. León
                        4. Salir:  """))
    except:
        print("Digite una opción valida.")
    else:
        if cOpcion==1:
            cHabitat = input("Digite el habitat del perro: ")
            cColor = input("Digite el color del perro: ")
            nPeso = input("Digite el peso del perro: ")
            cRazaPerro = input("Digite la raza del perro: ")
            cConcentradoPerro = input("Digite el tipo de concentrado del perro: ")
            #Cambiamos el valor 
            oAnimal1.setcHabitat(cHabitat)
            oAnimal1.setcColor(cColor)
            oAnimal1.setnPeso(nPeso)
            oAnimal1.setcTipoPerro(cRazaPerro)
            oAnimal1.setcTipoConcentrado(cConcentradoPerro)
            #Imprimimos el resultado 
            print(oAnimal1.hablar())
        elif cOpcion==2:
            cHabitat = input("Digite el habitat del pescado: ")
            cColor = input("Digite el color del pescado: ")
            nPeso = input("Digite el peso del pescado: ")
            cTamaño = input("Ingrese el tamaño del pesacado: ")
            nVelocidad = input("Ingrese la velocidad del pescado: ")
            #Cambiamos el valor 
            oAnimal2.setcHabitat(cHabitat)
            oAnimal2.setcColor(cColor)
            oAnimal2.setnPeso(nPeso)
            oAnimal2.setnTamaño(cTamaño)
            oAnimal2.setnVelocidad(nVelocidad)
            #Imprimimos en pantalla 
            print(oAnimal2.hablar())
        elif cOpcion==3:
            cHabitat = input("Digite el habitat del león: ")
            cColor = input("Digite el color del león: ")
            nPeso = input("Digite el peso del león: ")
            nEdad = input("Digite la edad del león: ")
            cGenero = input("Digite el genero del león: ")
            #Cambiamos el valor 
            oAnimal3.setcHabitat(cHabitat)
            oAnimal3.setcColor(cColor)
            oAnimal3.setnPeso(nPeso)
            oAnimal3.setnEdad(nEdad)
            oAnimal3.setcGenero(cGenero)
            print(oAnimal3.hablar())
        elif cOpcion== 4:
            Salir = "Desea salir del programa(Si/No): "
            print("Vuelva pronto.")
        






        
