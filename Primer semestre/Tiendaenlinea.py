#Programa que simula una tienda en linea
nCamisetas = 20
nPantalones = 35
nZapatos = 50

nCantidadCamisetas = int(input("¿Cuántas camisetas deseas llevar?"))
nCantidadPantalones = int(input("¿Cuántos pantalones deseas llevar?"))
nCantidadZapatos = int(input("¿Cuántos zapataos deseas llevar?"))

if nCantidadCamisetas <0 or nCantidadPantalones <0 or nCantidadZapatos<0:
    print("La cantidad ingresada es invalida.")
else:
    nTotal = (nCamisetas * nCantidadCamisetas) + (nPantalones * nCantidadPantalones) + (nZapatos * nCantidadZapatos)

if nTotal > 200:
    nTotal *= 0.20
elif nTotal > 100:
    nTotal *= 0.10
    
print (f"El costo total de su compra es $ {nTotal} dolares.")

    

