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
        cursor.execute("CREATE DATABASE IF NOT EXISTS Parqueadero")
        print("Base de datos 'Parqueadero' creada exitosamente o ya existe.")

        # Seleccionar la base de datos
        cursor.execute("USE Parqueadero")

        # Crear tabla Vehiculo
        create_table_vehiculo = """
        CREATE TABLE IF NOT EXISTS Vehiculo (
            idVehiculo INT AUTO_INCREMENT,
            placa VARCHAR(10) UNIQUE,
            tipoVehiculo ENUM('Carro', 'Moto'),
            PRIMARY KEY (idVehiculo)
        )
        """
        cursor.execute(create_table_vehiculo)
        print("Tabla Vehiculo creada exitosamente o ya existe.")
        # Crear tabla Espacio
        create_table_espacio = """
        CREATE TABLE IF NOT EXISTS Espacio (
            idEspacio INT AUTO_INCREMENT PRIMARY KEY,
            codigoEspacio VARCHAR(10) UNIQUE, 
            tipoVehiculo ENUM('Carro', 'Moto'),
            disponible BOOLEAN DEFAULT TRUE
        )
        """
        cursor.execute(create_table_espacio)
        print("Tabla Espacio creada exitosamente o ya existe.")

        # Crear tabla Registro
        create_table_registro = """
        CREATE TABLE IF NOT EXISTS Registro (
            idRegistro INT AUTO_INCREMENT,
            idVehiculo INT,
            idEspacio INT,
            horaEntrada DATETIME,
            horaSalida DATETIME,
            valor DECIMAL(10,2),
            PRIMARY KEY (idRegistro),
            FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo),
            FOREIGN KEY (idEspacio) REFERENCES Espacio(idEspacio)
        )
        """
        cursor.execute(create_table_registro)
        print("Tabla Registro creada exitosamente o ya existe.")

        # Confirmar los cambios
        connection.commit()

except Error as e:
    print("Error al conectarse a MySQL:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada en la base de datos.")
