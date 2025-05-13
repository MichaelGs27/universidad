import libreria_convertir   #Libreria para convertir moneda o masa kg-g/ lbs - kg
salir="Si"
nConversion = 0.0
while salir=="Si":      #Bluce para saber si salir del programa o no |  
    try: 
        print("----CONVERSOR-----")
        nOpcion = int(input("""1. Convertir Moneda (COP-USD):
                2. Convertit Moneda (COP-EUR)
                3. Convertit Masa (KG-G)
                4. Convertit Masa (Lb-Kg)
                Elige una opción (1-4): """))         #Opción para elegir el tipo de conversión
    except: 
        print("Elige una opcion correcta.")
    else:
        if nOpcion==1:
            nConversion = float (input("Ingresa la tasa de conversion de la moneda COP-USD (ej: 4000.00): "))
            nNum1 = float(input("Ingresa el valor que deseas convertir: "))
            nResultado = libreria_convertir.ConvertirO(nNum1, nOpcion,nConversion)       #Traemos la libreria para las conversiones
            print(f"El resultado de la conversion de moneda COP-USD: ${nResultado}")
        elif nOpcion==2:
            nConversion = float (input("Ingresa la tasa de conversion de la moneda COP-EUR (ej: 4000.00): "))
            nNum1 = float (input("Ingresa el valor que deseas convertir: "))
            nResultado = libreria_convertir.ConvertirO(nNum1, nOpcion,nConversion)       #Traemos la libreria para las conversiones
            print(f"El resultado de la conversion de moneda COP-EUR: €{nResultado}")
        elif nOpcion==3:
            nNum1 = float (input("Ingresa el valor que deseas convertir : "))
            nResultado = libreria_convertir.ConvertirO(nNum1,nOpcion, nConversion)       #Traemos la libreria para las conversiones
            print(f"El resultado de la conversion de masa Kg-Gr: {nResultado}")
        elif nOpcion==4:
            nNum1 = float (input("Ingresa el valor que deseas convertir : "))
            nResultado = libreria_convertir.ConvertirO(nNum1,nOpcion, nConversion)       #Traemos la libreria para las conversiones
            print(f"El resultado de la conversion de masa Lb-Kg: {nResultado}")
        salir = input("¿desea salir del programa? si o no: ")           #Pregunta para saber si seguir el programa o salirse 
