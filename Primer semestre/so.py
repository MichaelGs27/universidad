import shutil

# Lista para almacenar los nombres de los archivos comprimidos
archivos_comprimidos = []

def comprimir_archivo(nombre_archivo, tamaño_archivo_mb):
    """
    Simula la compresión de un archivo si su tamaño es mayor a 500 MB,
    evita duplicidad y registra los archivos comprimidos.
    """
    # Verificar si el archivo ya fue comprimido
    archivo_comprimido = f"{nombre_archivo}.zip"
    if archivo_comprimido in archivos_comprimidos:
        print(f"El archivo comprimido '{archivo_comprimido}' ya está registrado.")
        return

    # Verificar si el archivo supera los 500 MB
    if tamaño_archivo_mb > 500:
        # Simular la compresión
        archivos_comprimidos.append(archivo_comprimido)
        print(f"El archivo '{nombre_archivo}' ha sido comprimido exitosamente como '{archivo_comprimido}'.")
    else:
        print(f"El archivo '{nombre_archivo}' no necesita ser comprimido (tamaño: {tamaño_archivo_mb} MB).")

# Solicitar al usuario la información de los archivos
while True:
    # Solicitar el nombre del archivo
    nombre_archivo = input("Ingresa el nombre del archivo (o escribe 'salir' para terminar): ")
    if nombre_archivo.lower() == 'salir':
        break

    # Solicitar el tamaño del archivo en MB
    try:
        tamaño_archivo_mb = float(input(f"Ingresa el tamaño de '{nombre_archivo}' en MB: "))
    except ValueError:
        print("Por favor, ingresa un número válido para el tamaño.")
        continue

    # Procesar el archivo
    comprimir_archivo(nombre_archivo, tamaño_archivo_mb)

# Mostrar los archivos comprimidos generados
print("\nArchivos comprimidos generados:")
for archivo in archivos_comprimidos:
    print(f"- {archivo}")

