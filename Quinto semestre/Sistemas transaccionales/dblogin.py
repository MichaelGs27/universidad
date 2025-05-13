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
        # Crear la base de datos (si no existe)
        cursor.execute("CREATE DATABASE IF NOT EXISTS dbLogin")
        print("Base de datos creada exitosamente o ya existe.")
        # Seleccionar la base de datos
        cursor.execute("USE dbLogin")

        # Crear tabla Genero
        create_table_usuario = """ 
        CREATE TABLE IF NOT EXISTS Usuario(
            cIdUsuario INT AUTO_INCREMENT,
            cNomUsuario VARCHAR(45) NOT NULL,
            cContraseña Varchar(200) NOT NULL,
            PRIMARY KEY (cIdUsuario)
        )
        """
        cursor.execute(create_table_usuario)
        print("Tabla usuario creada exitosamente o ya existe.")
except Error as e:
    print("Error al conectarse al MySQL:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada en la base de datos.")