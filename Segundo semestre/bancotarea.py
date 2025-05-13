#Importamos la libreria datetime para las fecha
from datetime import datetime, timedelta
class cliente:
    #Atributos
    nNumCliente = 0
    cNombre = ''
    nCantidad = 0.0 

    #Constructor

    def __init__(self,nNumCliente, cNombre, nCantidad):
        self.nNumCliente = nNumCliente
        self.cNombre = cNombre
        self.nCantidad = nCantidad

    def getnNumCliente(self):       #Número del cliente
        return self.nNumCliente
    def setnNumCliente(self, nNumCliente):
        self.nNumCliente = nNumCliente
    
    def getcNombre(self):           #Nombre del Cliente 
        return self.cNombre
    def setcNombre(self, cNombre):
        self.cNombre = cNombre

    def getnCantidad(self):         #La Cantidad o monto en la cuenta
        return self.nCantidad
    def setnCantidad(self, nCantidad):
        self.nCantidad = nCantidad

    def consignar(self,nCantidad):
        nSaldo = 0.0 
        nNuevoSaldo = 0.0
        if nCantidad >0:
            nSaldo = self.getnCantidad()  #Traigo la cantidad de dinero que tiene la cuenta 
            nNuevoSaldo = nSaldo + nCantidad #Sumo el valor que tiene la cuenta mas la nueva cantidad
            self.setnCantidad(nNuevoSaldo)

    def retirar(self,nCantidad):
        nSaldo = 0.0
        if nCantidad > 0:
            nSaldo = self.getnCantidad()
            if nCantidad < nSaldo:
                nNuevoSaldo = nSaldo - nCantidad  #Operación para el nuevo saldo de la cuenta 
                self.setnCantidad(nNuevoSaldo)
Salir = "Si"
    #Creo el objeto con base a la clase cuenta 
print("------BIENVENIDO-------")
try:
        cOpcion = input(""" Bienvenido al banco
                    1. Cliente (1)
                    2. Empleado (2): """)
except:
        print("Digite una opción valida ")
        #Elige la opción 1 que es cliente
if cOpcion == "1":
    oCuenta = cliente('',0,0.0)
    cNombreCuenta = input("Digite el nombre del titular de la cuenta: ")
    while Salir=="Si":
        try:
            #Menu para la primera opcion que es cliente
            cOpcion = input("""Operación a realizar 
                        1. Consignar
                        2. Retirar: """)
        except:
            print("Digite uan opción valida ")

        #Verifico que el usuario haya ingresado el nombre del titular de la cuenta
        if cNombreCuenta=='':
            print("El titular no puede estar vacio, por favor verifica. ")
        else:
            #Elige la opción 1 que es consignar 
            if cOpcion == '1':          
                nNumCliente = int(input("Digite su número de cliente: "))
                nValorIngresar = float(input("Digite el valor a consignar a la cuenta: "))
                oCuenta.consignar(nValorIngresar)
                print("El valor consignado es",nValorIngresar, "El saldo de la cuenta es: ", oCuenta.getnCantidad())
            #Elige la opción 2 que es retirar  
            elif cOpcion == '2':
                nNumCliente = int(input("Digite su número de cliente: "))
                nValorRetirar = float(input("Digite el valor a retirar de la cuenta cuenta: "))
                if nValorRetirar > 0:
                    oCuenta.retirar(nValorRetirar)
                    print("El valor retirado es",nValorRetirar, "El saldo de la cuenta es: ", oCuenta.getnCantidad())
                else:
                    print("Para poder retirar ingrese un valor positivo.")
        Salir =  input("¿Desea salir del programa?: ")
        #Termina el prgrama y muestra este mensaje 
    print(f"""El nombre de la cuenta es: {cNombreCuenta} Y su número de cliente es: {nNumCliente} 
        actualmente este es su saldo : """,oCuenta.getnCantidad())
    #Elige la opcion 2 que es empleado
elif cOpcion == "2":
    #Creo la clase empleado
    class empleado:
        #Atributos
        nNumIdentificacion = 0
        cNombreEm = ''
        cPuesto = ''                                                                                    
        dFechaIngreso = 0
        nAntiguedad = 0
        nSueldo = 0.0
        #Constructor
        def __init__(self,nNumIdentificacion , cNombreEm, cPuesto, dFechaIngreso, nAntiguedad, nSueldo):
            self.nNumIdentificacion = nNumIdentificacion
            self.cNombreEm = cNombreEm
            self.cPuesto = cPuesto
            self.dFechaIngreso = dFechaIngreso
            self.nAntiguedad = nAntiguedad
            self.nSueldo = nSueldo

        def getnNumIdentificacion(self):        #Número de Identificación
            return self.nNumIdentificacion
        def setnNumIdentificacion(self, nNumIdentificacion):
            self.nNumIdentificacion = nNumIdentificacion

        def getcNombreEm(self):             #Nombre del Empleado
            return self.cNombreEm
        def setcNombreEm(self, cNombreEm):
            self.cNombreEm = cNombreEm

        def getcPuesto(self):               #Puesto que ocupa el empleado
            return self.cPuesto
        def setcPuesto(self, cPuesto):
            self.cPuesto = cPuesto

        def getdFechaIngreso(self):             #Fecha de Ingreso al banco 
            return self.dFechaIngreso
        def setdFechaIngreso(self, dFechaIngreso):
            self.dFechaIngreso = dFechaIngreso

        def getnAntiguedad(self):              #Antigüedad en el banco
            return self.nAntiguedad
        def setnAntiguedad(self, nAntiguedad):
            self.nAntiguedad = nAntiguedad

        def getnSueldo(self):       #Sueldo del empleado
            return self.nSueldo
        def setnSueldo(self, nSueldo):
            self.nSueldo = nSueldo

        def nCalcularAntiguedad(self):
                #Calcula la antigüedad del empleado en años.
                nAntiguedad = (dFechaActual - dFechaIngreso).days
                return nAntiguedad

        def nCalcularDiasVacaciones(self):
        # Calcula los días de vacaciones que le corresponden al empleado.
            nDiasVacaciones = 5
            nContador = 1
            for nContador in range(1, self.nAntiguedad):
                if nDiasVacaciones > 1825:
                    nDiasVacaciones = nDiasVacaciones + 2
            return nDiasVacaciones
        
        def nCalcularSueldo(self):
        #Calcula el sueldo del empleado.
            if cPuesto == "cajero":
                nSueldo = 1000000
            elif cPuesto == "supervisor":
                nSueldo = 1500000    
            else:
                nSueldo = 2000000
            return nSueldo
    #Le pido los datos al empleado 
    oEmpleado = empleado (0,'','',0,0,0.0)
    nNumIdentificacion = input("Ingrese la identificación del empleado: ")
    nNombre = input("Ingrese el nombre del empleado: ")
    cPuesto = input("Ingrese el puesto del empleado (cajero - supervisor - recepcionista): ")
    dFechaIngreso = datetime.strptime(input("Ingrese la fecha de ingreso al banco (DD-MM-AAAA): "),"%d-%m-%Y")
    dFechaActual = datetime.strptime(input("Ingrese la fecha actual (DD-MM-AAAA): "),"%d-%m-%Y")
    #Imprimo en pantalla los datos del empleado
    print(f"""ID:{nNumIdentificacion} 
                Nombre: {nNombre}
                Puesto: {cPuesto} 
                Antigüedad: {oEmpleado.nCalcularAntiguedad()} dias de antigüedad
                Días de vacaciones: {oEmpleado.nCalcularDiasVacaciones()}
                Sueldo : ${oEmpleado.nCalcularSueldo()}""")
                
