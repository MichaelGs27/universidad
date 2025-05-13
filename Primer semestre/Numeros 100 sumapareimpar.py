#Suma de los números pares e impares de 1 a 100
nContador = 0
nSumaPar = 0
nSumaImpar = 0
for nContador in range(0,101):
    if nContador % 2== 0:
        nSumaPar = nSumaPar + nContador
    else:
        if nContador %2==1:
           nSumaImpar = nSumaImpar + nContador
print(f"La suma de los números pares es:{nSumaPar}")
print(f"La suma de los números impares es: {nSumaImpar}")

def nCalcularDiasVacaciones(self):
                    #Calcular los días de vacaciones que le corresponden al empleado.
            nDiasVacaciones = 0
            i = 0
            for i in range(1, self.nAntiguedad):
                nDiasVacaciones = nDiasVacaciones + i
            if nDiasVacaciones > 1825:
                nDiasVacaciones = 20
            return nDiasVacaciones
