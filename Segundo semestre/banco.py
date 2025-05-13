#Cargo libreria
import clases
Salir = "No"

    #Creo el objeto con base a la clase cuenta 
oCuenta = clases.Cuenta('',0.0)
cNombreTitular = input("Digite el nombre del titular de la cuenta: ")
while Salir=="No":
    try:
        cOpcion = input("""Operación a realizar 
                    1. Consignar
                    2. Retirar
                    3. Salir: """)
    except:
        print("Digite uan opción valida ")

    #Verifico que el usuario haya ingresado el nombre del titular de la cuenta
    if cNombreTitular=='':
        print("El titular no puede estar vacio, por favor verifica. ")
    else:
        if cOpcion == '1':
            nValorIngresar = float(input("Digite el valor a consignar a la cuenta: "))
            oCuenta.consignar(nValorIngresar)
            print("El valor consignado es",nValorIngresar, "El saldo de la cuenta es: ", oCuenta.getnCantidad())
        
        elif cOpcion == '2':
            nValorRetirar = float(input("Digite el valor a retirar de la cuenta cuenta: "))
            if nValorRetirar > 0:
                oCuenta.retirar(nValorRetirar)
                print("El valor retirado es",nValorRetirar, "El saldo de la cuenta es: ", oCuenta.getnCantidad())
            else:
                print("Para poder retirar ingrese un valor positivo.")
    Salir =  input("¿Desea salir del programa?: ")
print(f"El nombre del titular de la cuenta es: {cNombreTitular} Y su saldo es: ",oCuenta.getnCantidad() )