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

        # Insertar los registros 
        insert_queries = [
            #Tipos de identificacion
            "INSERT INTO usuario (cIdUsuario, cNomUsuario, cContraseña ) VALUES ('1', 'Michael0', 'Michael.10');",
            "INSERT INTO usuario (cIdUsuario, cNomUsuario, cContraseña) VALUES ('2', 'Oscar', 'Oscar0');",
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
        cursor.execute("SELECT * FROM usuario;")
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