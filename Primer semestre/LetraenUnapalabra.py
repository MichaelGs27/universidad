#Programa para saber cuantas veces hay una letra en una frase
nFrase = input("Ingresa una frase en minuscula: ")
nLetra = input("Ingresa una letra en minuscula: ")
nCantidad = 0

for caracter in nFrase:
    if caracter == nLetra:
        nCantidad += 1

print(f"La letra '{nLetra}', aparece '{nCantidad}' de veces en la frase '{nFrase}'")     
