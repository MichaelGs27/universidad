#Programa diseñado por MIchael Gutierrez 
#Menú
nMenu = 0
nCalculadora= 0
while nMenu ==0:
    
        print("-----MENÚ-----")
        print("1. Calculadora")
        print("2. Convertir distancia")
        print("3. Convertir masa")
        print("4. Area y perimetro")
        print("5. Ingresar notas de un estudiante")
        print("6. Números primos de un número")
        print("7. Salir")
        nOpcion1 = input("Elige una opción: ")
        
        if nOpcion1 == "1":
                        #Calculadora
                        print("----CALCULADORA----")
                        print("1. Suma")
                        print("2. Resta")
                        print("3. Multiplicacion")
                        print("4. Division")
                        print("5. Volver al menú")
                        nOpcion = int(input("Selecciona una opción (1-5): "))
                        if nOpcion == 1:
                                nNum1 = int(input("Escribe el primer número: "))
                                nNum2 = int(input("Digite el segundo número: "))
                                print(f"El resultado de la suma es: {nNum1 + nNum2}") #Operacion y resultado de la suma
                        elif nOpcion == 2:
                                nNum1 = int(input("Escribe el primer número: "))
                                nNum2 = int(input("Digite el segundo número: "))
                                print(f"El resultado de la resta es: {nNum1 - nNum2}") #Operacion y resultado de la resta
                        elif nOpcion == 3:
                                nNum1 = int(input("Escribe el primer número: "))
                                nNum2 = int(input("Digite el segundo número: "))
                                print(f"El resultado de la multiplicacion es: {nNum1 * nNum2}") #Operacion y resultado de la multiplicacion
                        elif nOpcion == 4:
                                nNum1 = int(input("Escribe el primer número: "))
                                nNum2 = int(input("Digite el segundo número: "))
                                if nNum2 <1:
                                        print("No se puede dividir por cero.")
                                print(f"El resultado de la divion es: {nNum1 / nNum2}") #Operacion y resultado de la division                              
                        elif nOpcion== 5:
                                print("Hasta Luego")           
        elif nOpcion1 == "2":
                print("-----CONVERTIR DISTANCIA-----") #Convertir las distancias
                print("Selecciona una opción:")
                print("1. Convertir Kilometros a metros")
                print("2. Convertir metros a kilometros")
                print("3. Convertir kilometros a millas")
                print("4. Convertir millas a kilometros")
                print("5. Volver al menú")
                nOpcion = int(input("Selecciona una opción (1-5): "))
                if nOpcion == 1:
                        nKm= float(input("Introduce la distancia en kilometros: ")) 
                        nMetros = nKm*1000              #Operacion para convertir kilometros a metros 
                        print(f"{round(nKm, 2)} kilometros son {nMetros} metros.")
                elif nOpcion ==2:
                        nMe = float(input("Ingresa los metros que deseas pasar a kilometros: "))
                        nKilom = nMe / 1000             #Operacion para convertir metros a kilometros 
                        print(f"{round(nMe,2)} metros son {nKilom} kilometros. ")
                elif nOpcion==3:
                        nKilom = float(input("Ingresa los kilometros que deseas pasar a millas: "))
                        nMi = nKilom / 1.609             #Operacion para convertir kilometros a millas
                        print(f"{round(nKilom,2)} kilometros son {nMi} millas.")
                elif nOpcion ==4:
                        nMi = float(input("Ingresa las millas que quieres pasar a kilometros: "))
                        nMi= nMi/1000                   #Operacion para convertir millas a kilometros 
                        print(f"{round(nMi,2)} millas son {nMi} kilometros. ")
                elif nOpcion==5:
                        print("Hasta Luego")            
        elif nOpcion1 == "3":
                print("-----CONVERTIR MASA-----")     #Convertidor de masa
                print("Selecciona una opción:")
                print("1. Convertir Kilogramos a libras")
                print("2. Convertir libras a kilogramos")
                print("3. convertir libras a gramos")
                print("4. Convertir gramos a libras")
                print("5. Volver al menú")
                nOpcion = int(input("Selecciona una opción (1-5): "))
                if nOpcion == 1:
                        nKilogra = float(input("Ingrese los kilogramos que desea pasar a libras: "))
                        nLibra = nKilogra * 2.205               #Operacion para convertir Kilogramos a libras
                        print(f"{nKilogra} kilogramos son {round(nLibra,2)} Libras.")
                elif nOpcion ==2:
                        nLibra = float(input("Digite las libras que desea pasar a kilogramos: "))
                        nKilogra = nLibra / 2.205                #Operacion para convertir libras a kilogramos 
                        print(f"{nLibra} Libras son {round(nKilogra,2)} kilogramos.")
                elif nOpcion==3:
                        nLibra = float(input("Ingrese las libras que deseas pasar a gramos: "))
                        nGramos = nLibra * 453.592              #Operacion para convertir libras a gramos
                        print(f"{nGramos} Gramos son {round(nLibra,2)} Libras.")
                elif nOpcion ==4:
                        nGramos = float(input("Digete los gramos que deseas pasar a libras: "))
                        nLibra = nGramos / 453.592              #Operacion para convertir gramos a libras 
                        print(f"{nLibra} Libras son {round(nGramos,2)} gramos")
                elif nOpcion==5:
                        print("Hasta Luego") 
        elif nOpcion1 == "4":
                print("-----AREA Y PERIMETRO DE UNA CIRCUNFERENCIA-----")     #Area y perimetro
                nRadio =  float(input("Digite el radio: "))
                print (f"El area es : {3.14159265 * nRadio * nRadio}")     #Operacion y resultado del area
                print (f"Y el perimetro es :{6.28318531 * nRadio}")        #Operacion y resultado del perimetro
                nSalida = input("¿Deseas salir? (si/no)")
                if nSalida == "si":
                        print("Volviendo al menu principal...")
        elif nOpcion1 == "5":
                print("-----INGRESAR NOTAS DE LA MATERIA-----")         #Promedio de notas 
                nConta = 0
                nNota=0
                nSumaNotas = 0
                nNotas = int(input("Escribe cuantas notas son: "))      
                for nConta in range(0,nNotas):        
                        nNota= float(input(f"Escribir la nota  {nConta}: "))    
                        nSumaNotas = nSumaNotas + nNota                 #Sumas de notas 
                nPromedio = nSumaNotas / nNotas                 #Promedio de notas
                print(f"El promedio de notas es: {nPromedio}")          #Salida del promedio
        elif nOpcion1 == "6":
                print("-----NÚMEROS PRIMOS DE UN NÚMERO-----")          #Numeros primos
                nNum = int(input("Ingrese un número: "))
                for nConta in range(1, nNum+1):                 #Primer for para ir hasta x numero que se ingrese
                        if nConta > 1:
                                for nConti in range(2, nConta):         #Segundo for para saber cuales son primos 
                                        if (nConta % nConti) == 0:
                                             break
                                else:
                                    print(nConta, "es primo")           #Salida con los numeros que son primos 
                nOpcion = ("¿Deseas salir del programa?(si/no)" )
                if nOpcion == "si":
                       print("Hasta Luego")
                else:
                       print("Sigue en el programa")
        elif nOpcion1 == "7":
                nRespuesta = str(input("¿Deseas salir de programa?(Si/No): "))
                if nRespuesta != "S":
                        print("Sigues en el programa")               
                else:
                        break  
        else:
                print("Opcion invalida, intente de nuevo")

