#Este programa es para promediar la nota de sus estudiamtes
"""
nConta = 0
nSumaNotas = 0
nEstudiantes = int(input("Escribe la cantidad total de estudiantes: "))
for nConta in range(1,nEstudiantes + 1):
    nNota= float(input(f"Escribir la nota del estudiante {nConta} :"))
    nSumaNotas = nSumaNotas + nNota 

nPromedio = nSumaNotas / nEstudiantes
print(f"El promedio de notas del curso es: {nPromedio}")

"""
num = int(input("Ingrese un número: "))

# Verificamos si cada número desde 1 hasta el número ingresado es primo
for i in range(1, num+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, "es primo")