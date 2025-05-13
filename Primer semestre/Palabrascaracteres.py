# Programa que cuenta las palabras de una lista que tienen más de 5 caracteres utilizando una estructura repetitiva y condicional
nPalabras = input("Ingresa una lista de palabras separadas por comas: ").split(",")
nCantpalabras = 0

for nPalabra in nPalabras:
    if len(nPalabra) > 5:
        nCantpalabras += 1

if nCantpalabras == 0:
    print("No se encontraron palabras con más de 5 caracteres en la lista.")
elif nCantpalabras == 1:
    print("Se encontró 1 palabra con más de 5 caracteres en la lista.")
else:
    print(f"Se encontraron {nCantpalabras} palabras con más de 5 caracteres en la lista.")
