import mysql.connector
from mysql.connector import Error

try:
    # Establecer conexión con el servidor
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password=""
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Seleccionar la base de datos
        cursor.execute("USE Parqueadero")

        # Iniciar la transacción
        cursor.execute("START TRANSACTION;")

        # Insertar los registros (Espacios para Motos y Carros)
        insert_queries = [
            # Espacios para Motos
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M1', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M2', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M3', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M4', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M5', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M6', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M7', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M8', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M9', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M10', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M11', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M12', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M13', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M14', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M15', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M16', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M17', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M18', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M19', 'Moto', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('M20', 'Moto', TRUE);",
            #Espacio para carros
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C1', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C2', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C3', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C4', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C5', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C6', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C7', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C8', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C9', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C10', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C11', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C12', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C13', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C14', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C15', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C16', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C17', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C18', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C19', 'Carro', TRUE);",
            "INSERT INTO espacio (codigoEspacio, tipoVehiculo, disponible) VALUES ('C20', 'Carro', TRUE);"
            
        ]

        for query in insert_queries:
            cursor.execute(query)

        # Confirmar los cambios
        connection.commit()
        print("Registros insertados exitosamente.")

        # Verificar cuántas filas fueron afectadas
        cursor.execute("SELECT ROW_COUNT();")
        rows_affected = cursor.fetchone()
        print(f"Número de filas insertadas: {rows_affected[0]}")

        # Si deseas ver los registros insertados, puedes hacer un SELECT:
        cursor.execute("SELECT * FROM espacio;")
        result = cursor.fetchall()
        for row in result:
            print(row)

except Error as e:
    print("Error al conectarse a MySQL:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada en la base de datos.")
