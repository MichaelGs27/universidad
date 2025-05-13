#Programa para que el usuario adivine el número aleatorio que da el programa 
import random
nNumAleatorio = random.randint(1,100)
nIntentos = 0

while True:
    nIntentos += 1
    nNumUsuario= int (input("Adivina el número del 1 al 100: "))

    if nNumUsuario == nNumAleatorio:
        print(f"¡Felicidades! adivinaste el número en {nIntentos} intentos.")
        break
    elif nNumUsuario < nNumAleatorio:
        print("El número buscado es mayor.")
    else:
        print("El número buscado es menor.")

