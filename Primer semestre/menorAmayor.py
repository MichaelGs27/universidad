# Programa que ordena tres números enteros de menor a mayor utilizando condicionales
nNUm1 = int (input("Ingrese el primer número: "))
nNUm2 = int(input("Ingrese el segundo número: "))
nNum3 = int(input("Ingrese el tercer número: "))

if nNUm1 <= nNUm2 and nNUm1 <= nNum3:
    if nNUm2<=nNum3:
        print(F"Los números ordenados de mayor a menor son: {nNUm1}, {nNUm2}, {nNum3}.")
    else:
        print(f"Los números ordenados de menor a mayor son: {nNUm1}, {nNum3}, {nNUm2}")
elif nNUm2<=nNUm1 and nNUm2<=nNum3:
    if nNUm1<=nNum3:
        print(f"Los números ordenados de mayor a menor son: {nNUm2}, {nNUm1} {nNum3}")  
    else:
         print(f"Los números ordenados de menor a mayor son: {nNUm2}, {nNum3}, {nNUm1}")
else:
    if nNum3<=nNUm1:
         print(f"Los números ordenados de menor a mayor son: {nNum3}, {nNUm1}, {nNUm2}")
    else:
         print(f"Los números ordenados de menor a mayor son: {nNum3}, {nNUm2}, {nNUm1}")

