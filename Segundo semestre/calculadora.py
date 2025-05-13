"""
#Cargo la libreria
import libreria
#Entrada de datos para calculadora
nResultado=0.0
try: 
     nNum1 =float(input("Ingresa el primer número: "))
     nNum2 = float(input("Ingresa el segundo número: "))
     nOperacion = input("Dijite el tipo de operación: +,-,*,/: ")
except:
     print("Señor no se puede ingresar letras por favor reinicie el programa.")
else:    
    if nOperacion == "/":      
        if nNum2 == 0: 
            print("No se puede dividir por cero.")      #Sale un error al usuario que no se puede dividir por cero 
    if nOperacion == "+" or nOperacion == "-" or nOperacion == "*" or nOperacion == "/":
        nResultado = libreria.Calculadora(nNum1,nNum2,nOperacion)
        print(f"El resultado de la operación {nOperacion} es: {nResultado} ")
    else:
        print("La operacion que ingreso no es valida. ") 
"""
#Dos formas de importar una libreria 
from libreria import Calculadora
nResultado=0.0
try: 
     nNum1 =float(input("Ingresa el primer número: "))
     nNum2 = float(input("Ingresa el segundo número: "))
     nOperacion = input("Dijite el tipo de operación: +,-,*,/: ")
except:
     print("Señor no se puede ingresar letras por favor reinicie el programa.")
else:    
    if nOperacion == "/":      
        if nNum2 == 0: 
            print("No se puede dividir por cero.")      #Sale un error al usuario que no se puede dividir por cero 
    if nOperacion == "+" or nOperacion == "-" or nOperacion == "*" or nOperacion == "/":
        nResultado = Calculadora(nNum1,nNum2,nOperacion)
        print(f"El resultado de la operación {nOperacion} es: {nResultado} ")
    else:
        print("La operacion que ingreso no es valida. ") 