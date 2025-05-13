# Programa que calcula la media de los números pares de una lista utilizando condiciones y estructuras repetitivas
nContador = 0
nSumaPar = 0
nCantidadPar = 0
nMediaPares = 0
nNum = int(input("Digite un número para sacarle que numeros pares hay dentro del numero mencionado: "))
for nContador in range(nNum):
    if int(nContador) % 2== 0:
        nSumaPar += int(nContador)
        nCantidadPar += 1
if nCantidadPar > 1:
        nMediaPares = nSumaPar / nCantidadPar
        print (f"La media de los numeros pares es: {nMediaPares}")
else:
        print("No se encontraron pares en la lista")
        