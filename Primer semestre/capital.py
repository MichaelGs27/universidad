# programa que simula el capital obtenido en la inversión cada año que dura la inversión.
nCantidad = float(input("¿Cantidad a invertir? "))
nInteres = float(input("¿Interés porcentual anual? "))
nAños = int(input("¿Años?"))
for nConta in range(nAños):
    nCantidad *= 1 + nInteres / 100 
    print(f"Capital tras {nConta + 1} años: {(round(nCantidad, 2))}")
          
