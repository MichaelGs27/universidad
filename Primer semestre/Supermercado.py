#Supermercado venta del producto
nProducto = int(input("Digite cuantas unidades desea llevar"))
nPrecio = int(input("Digite el precio por unidad"))
nDocenas = nProducto / 12


if nDocenas>=3: 
   nDescuento= 0.15
else:
    if nDocenas<3:
        nDescuento = 0.10
nPrecioSinDescuento = nProducto * nPrecio
nMontoDescuento= nPrecioSinDescuento * nDescuento
nPrecioConDescuento= nPrecioSinDescuento - nMontoDescuento


if nDocenas>=3:
    nUnidadesOb= (nDocenas + 1) 
else:
    nUnidadesOb = 0
           
          
print(f"Monto de la compra:{nPrecioSinDescuento}")
print(f"Monto del descuento: {nMontoDescuento}")
print(f"Monto a pagar: {nPrecioConDescuento}")
print(f"Unidades de obsequio: {nUnidadesOb}")


