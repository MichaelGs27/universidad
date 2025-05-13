import datetime
class cliente:
    #Atributos
    nNumCliente = 0
    cNombre = ''
    nCantidad = 0.0

    #Constructor

    def __init__(self, nNumCliente, cNombre, nCantidad):
        self.nNumCliente = nNumCliente
        self.cNombre = cNombre
        self.nCantidad = nCantidad

    def getnNumCliente(self):
        return self.nNumCliente
    def setnNumCliente(self, nNumCliente):
        self.nNumCliente = nNumCliente
    
    def getcNombre(self):
        return self.cNombre
    def setcNombre(self, cNombre):
        self.cNombre = cNombre

    def getnCantidad(self):
        return self.nCantidad
    def setnCantidad(self, nCantidad):
        self.nCantidad = nCantidad

    def consignar(self, nCantidad):
        nSaldo = 0.0
        nNuevoSaldo = 0.0
        if nCantidad > 0:
            nSaldo = self.getnCantidad()
            nNuevoSaldo = nSaldo + nCantidad
            self.setnCantidad(nNuevoSaldo)

    def retirar(self, nCantidad):
        nSaldo = 0.0
        if nCantidad > 0:
            nSaldo = self.getnCantidad()
            if nCantidad < nSaldo:
                nNuevoSaldo = nSaldo - nCantidad
                self.setnCantidad(nNuevoSaldo)

def cCliente():
    oCuenta = cliente(0, '', 0.0)
    cNombreCuenta = input("Digite el nombre del titular de la cuenta: ")
    while Salir == "No":
        try:
            cOpcion = input("""Operación a realizar
                            1. Consignar
                            2. Retirar
                            3. Salir: """)
        except:
            print("Digite uan opción valida ")

        #Verifico que el usuario haya ingresado el nombre del titular de la cuenta
        if cNombreCuenta == '':
            print("El titular no puede estar vacio, por favor verifica. ")
        else:
            if cOpcion == '1':
                nNumCliente = int(input("Digite su número de cliente: "))
                nValorIngresar = float(input("Digite el valor a consignar a la cuenta: "))
                oCuenta.consignar(nValorIngresar)
                print("El valor consignado es", nValorIngresar, "El saldo de la cuenta es: ", oCuenta.getnCantidad())

            elif cOpcion == '2':
                nNumCliente = int(input("Digite su número de cliente: "))
                nValorRetirar = float(input("Digite el valor a retirar de la cuenta cuenta: "))
                if nValorRetirar > 0:
                    oCuenta.retirar(nValorRetirar)
                    print("El valor retirado es", nValorRetirar, "El saldo de la cuenta es: ", oCuenta.getnCantidad())
                else:
                    print("Para poder retirar ingrese un valor positivo.")
        Salir = input("¿Desea salir del programa?: ")
    print(f"""El nombre de la cuenta es: {cNombreCuenta} Y su número de cliente es: {nNumCliente}
            actualmente este es su saldo : """, oCuenta.getnCantidad())
import datetime

class empleado:
    #Atributos
    nNumIdentificacion = 0
    cNombreEm = ''
    cPuesto = ''
    dFechaIngreso = 0
    nAntiguedad = 0

    #Constructor

    def __init__(self, nNumIdentificacion, cNombreEm, cPuesto, dFechaIngreso):
        self.nNumIdentificacion = nNumIdentificacion
        self.cNombreEm = cNombreEm
        self.cPuesto = cPuesto
        self.dFechaIngreso = dFechaIngreso
        self.nAntiguedad = self.nCalcularAntiguedad()

    def getnNumIdentificacion(self):
        return self.nNumIdentificacion
    def setnNumIdentificacion(self, nNumIdentificacion):
        self.nNumIdentificacion = nNumIdentificacion

    def getcNombreEm(self):
        return self.cNombreEm
    def setcNombreEm(self, cNombreEm):
        self.cNombreEm = cNombreEm

    def getcPuesto(self):
        return self.cPuesto
    def setcPuesto(self, cPuesto):
        self.cPuesto = cPuesto

    def getdFechaIngreso(self):
        return self.dFechaIngreso
    def setdFechaIngreso(self, dFechaIngreso):
        self.dFechaIngreso = dFechaIngreso

    def getnAntiguedad(self):
        return self.nAntiguedad
    def setnAntiguedad(self, nAntiguedad):
        self.nAntiguedad = nAntiguedad

    def nCalcularAntiguedad(self):
        #Calcula la antigüedad del empleado en años.
        cHoy = datetime.now()
        diferencia = cHoy - self.dFechaIngreso
        return diferencia.days / 365.25

    def nCalcularDiasVacaciones(self):
        #Calcular los días de vacaciones que le corresponden al empleado.
        nDiasVacaciones = 5
        for i in range(1, self.nAntiguedad):
            nDiasVacaciones += 2
        if nDiasVacaciones > 20:
            nDiasVacaciones = 20
        return nDiasVacaciones

    def __str__(self):
        #Devuelve una representación del empleado.
        return f"""ID: {self.nNumIdentificacion} 
            Nombre: {self.cNombreEm}
            Puesto: {self.cPuesto} 
            Antigüedad: {self.nAntiguedad}
            Días de vacaciones: {self.nCalcularDiasVacaciones()}"""


identificacion = input("Ingrese la identificación del empleado: ")
while not identificacion.isdigit():
    identificacion = input("Ingrese la identificación del empleado: ")
nombre = input("Ingrese el nombre del empleado: ")
puesto = input("Ingrese el puesto del empleado: ")
fecha_ingreso = input("Ingrese la fecha de ingreso del empleado (YYYY-MM-DD): ")
cEmpleado = empleado(identificacion, nombre, puesto, fecha_ingreso)
print(cEmpleado)
