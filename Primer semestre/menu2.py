# menu con ayuda
#Importar el módulo math para usar pi
import math 
#Definir una función para alidar que el usuario ingrese un número
def nValidarNumero (mensaje):
    while True:
        try:
            nNumero= float(input(mensaje))
            return nNumero
        except ValueError:
            print("Por favor ingresa un número valido.")
#Definir una función para mostrar el menú principal
def nMenu ():
    print("-----MENÚ-----")
    print("1. Calculadora")
    print("2. Convertir distancia")
    print("3. Convertir masa")
    print("4. Area y perimetro")
    print("5. Ingresar notas de un estudiante")
    print("6. Números primos de un número")
    print("7. Salir") 
#Definir una función para realizar las operaciones básicas de la calculadora
def nCalculadora ():
    print("---CALCULADORA---")
    print("a. Suma")
    print("b. Resta")
    print("c. Multiplicación")
    print("d. División")
    print("e. Volver al menu principal")
    nOpcion= input("Elige una opción: ")
    if nOpcion== "a":
        nNum1 = nValidarNumero ("Ingresa el primer número: ")
        nNum2 = nValidarNumero ("Ingresa el segundo número: ")
        nResultado = nNum1 + nNum2
        print(f"El resultado de la suma de {nNum1} y { nNum2} es: {nResultado}.")
        nCalculadora()
    elif nOpcion == "b":
        nNum1 = nValidarNumero ("Ingresa el primer número: ")
        nNum2 = nValidarNumero ("Ingresa el segundo número: ")
        nResultado = nNum1 - nNum2
        print(f"El resultado de la resta de {nNum1} y { nNum2} es: {nResultado}.")
        nCalculadora()
    elif nOpcion == "c":
        nNum1 = nValidarNumero ("Ingresa el primer número: ")
        nNum2 = nValidarNumero ("Ingresa el segundo número: ")
        nResultado = nNum1 * nNum2
        print(f"El resultado de la multiplicación de {nNum1} y { nNum2} es: {nResultado}.")
        nCalculadora()
    elif nOpcion == "d":
        nNum1 = nValidarNumero ("Ingresa el primer número: ")
        nNum2 = nValidarNumero ("Ingresa el segundo número: ")
        nResultado = nNum1 / nNum2
        if nNum2 == 0:
            print("No se puede dividir por 0.")
            nCalculadora()
        else:
            print(f"El resultado de la división de {nNum1} y { nNum2} es: {nResultado}.")
            nCalculadora()
    elif nOpcion == "e":
        nMenu()
    else:
        print("Opción invalida")
        nCalculadora()
#Definir una función para convertir distancias
def nConvertirDistancias ():
    print("---CONVERTIR DISTANCIAS---")
    print("a. De metros a centimetros")
    print("b. De centimetros a metros")
    print("c. De kilometros a metros")
    print("d. De metros a kilometros")
    print("e. Volver al menu principal")
    nOpcion= input("Elige uan opción: ")
    if nOpcion== "a":
        nMetros= nValidarNumero ("Ingresa la cantidad de metros")
        nCentimetros = nMetros * 100
        print(f"{nMetros} Metros equivalen a {nCentimetros} centimetros.")
        nConvertirDistancias()
    elif nOpcion == "b":
        nCentimetros = nValidarNumero ("Ingresa la cantidad de centimetros")
        nMetros = nCentimetros / 100
        print(f"{nCentimetros} centimetros equivalen a {nMetros} metros.")
        nConvertirDistancias()
    elif nOpcion == "c":
        nKilometros= nValidarNumero ("Ingresa la cantidad de kilometros")
        nMetros = nKilometros * 1000
        print(f"{nKilometros} Kilometros equivalen a {nMetros} metros.")
        nConvertirDistancias()
    elif nOpcion == "d":
        nMetros= nValidarNumero ("Ingresa la cantidad de metros")
        nKilometros = nMetros / 1000
        print(f"{nMetros} Metros equivalen a {nKilometros} kilometros.")
        nConvertirDistancias()
    elif nOpcion == "e":
        nMenu()
    else:
        print("Opción invalida")
        nConvertirDistancias()
#Definir una función para convertir las unidades de masa




2


