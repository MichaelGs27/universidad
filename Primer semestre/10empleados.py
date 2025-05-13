#Empleados masculinos y femeninos
nEmpleado = 10
nNumHomb = 0
nNumMuje = 0
nSumaEdad = 0
nSumaSalario = 0

for nConta in range(nEmpleado):
    print(f"Ingrese información del empleado{nConta + 1}:")
    nEdad = int (input("Edad: "))
    nGenero = str(input("Genero (M o F): "))
    nSalario = float(input("Salario: "))

    nSumaEdad += nEdad
    nSumaSalario += nSalario

    if nGenero =="M":
        nNumHomb += 1
    elif nGenero== "F":
        nNumMuje += 1

nPromedioEdad = nSumaEdad / nEmpleado
nPromedioSalario = nSumaSalario / nEmpleado

print(f"Estaditicas de los empleados:")
print(f"Total empleados: {nEmpleado}")
print(f"Masculinos: {nNumHomb}")
print(f"Femeninos: {nNumMuje}")
print(f"Promedio edad: {nPromedioEdad}")
print(f"Promedio salario: {nPromedioSalario}")

    




