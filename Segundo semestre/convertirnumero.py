import libreria_convertir  #Libreria para convertir masa
salir="si"
while salir=="si":      #Bluce para saber si salir del programa o no |  
    try: 
        nNum1 =float(input("Ingresa el primer número: "))       #Ingresar el número a convertir
        print("1. Convertir Masa (gramos a kilogramos):")
        print("2. Convertir distancia (Millas a kilometros):")
        nOpcion = float(input("Elige una opción (1-2): "))          #Opción para elegir el tipo de conversión
    except:
        print("Señor debe elegir una de esas opciones. Por favor reinicie el programa.")        #devuelve al inicio si no escribe un número entre 1 y 2
    else:
        if nOpcion==1:
            nResultado = libreria_convertir.Convertir(nNum1,nOpcion,)       #Traemos la libreria para las conversiones
            print(f"El resultado de la conversion de masa es {nResultado}")
        elif nOpcion==2:
            nResultado = libreria_convertir.Convertir(nNum1, nOpcion)
            print(f"El resultado de la conversion de la velocidad es {nResultado}")
        salir = input("¿desea salir del programa? si o no: ")           #Pregunta para saber si seguir el programa o salirse 



