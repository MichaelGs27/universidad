# Programa que calcula el costo de envío de paquetes

while True:
    try:
        nPeso = float(input("Ingrese el peso del paquete en kilogramos: "))
        nDistancia = float(input("Ingrese la distancia a recorrer en kilómetros: "))
        if nPeso > 0 and nDistancia > 0:
            break
        else:
            print("Error: el peso y la distancia deben ser valores numéricos positivos.")
    except ValueError:
        print("Error: el peso y la distancia deben ser valores numéricos positivos.")

nCostobase = 10
nCostopeso = 5 * nPeso
nCostodistancia = 2 * (nDistancia // 100)

nCostototal = nCostobase + nCostopeso + nCostodistancia

if nPeso > 10:
    nDescuentopeso = nCostototal * 0.05
    nCostototal -= nDescuentopeso

if nDistancia > 1000:
    nDescuentodistancia = nCostototal * 0.1
    nCostototal -= nDescuentodistancia

print(f"El costo de envío es de ${nCostototal:.2f}")


