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
        cursor.execute("CREATE DATABASE IF NOT EXISTS Universidad")
        print("Base de datos creada exitosamente o ya existe.")
        
        # Seleccionar la base de datos
        cursor.execute("USE Universidad")
        # Crear tabla Genero
        create_table_genero = """ 
        CREATE TABLE IF NOT EXISTS Genero(
            cIdGenero INT AUTO_INCREMENT,
            cNomGenero VARCHAR(45) NOT NULL,
            PRIMARY KEY (cIdGenero)
        )
        """
        cursor.execute(create_table_genero)
        print("Tabla Genero creada exitosamente o ya existe.")

        # Crear tabla usuario
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

        # Crear tabla Modalidad
        create_table_modalidad = """ 
        CREATE TABLE IF NOT EXISTS Modalidad(
            cIdModalidad INT AUTO_INCREMENT,
            cNomModalidad VARCHAR(45) NOT NULL,
            PRIMARY KEY (cIdModalidad)
        )
        """
        cursor.execute(create_table_modalidad)
        print("Tabla Modalidad creada exitosamente o ya existe.")
        # Crear tabla Aula
        create_table_aula = """ 
        CREATE TABLE IF NOT EXISTS Aula(
            cIdAula INT AUTO_INCREMENT,
            cNomAula VARCHAR(100) NOT NULL,
            PRIMARY KEY (cIdAula)
        )
        """
        cursor.execute(create_table_aula)
        print("Tabla Aula creada exitosamente o ya existe.")
        # Crear tabla Programa
        create_table_programa = """ 
        CREATE TABLE IF NOT EXISTS Programa (
            cIdPrograma INT AUTO_INCREMENT,
            cNomPrograma VARCHAR(100) NOT NULL,
            PRIMARY KEY (cIdPrograma)
        )
        """
        cursor.execute(create_table_programa)
        print("Tabla Programa creada exitosamente o ya existe.")
        # Crear tabla Periodo
        create_table_periodo = """ 
        CREATE TABLE IF NOT EXISTS Periodo(
            cIdPeriodo INT NOT NULL,
            cDescripcionPeriodo VARCHAR(100) NOT NULL,
            PRIMARY KEY (cIdPeriodo)
        )
        """
        cursor.execute(create_table_periodo)
        print("Tabla Periodo creada exitosamente o ya existe.")
        # Crear tabla Sede
        create_table_sede = """ 
        CREATE TABLE IF NOT EXISTS Sede(
            cIdSede INT AUTO_INCREMENT,
            cNomSede VARCHAR(100) NOT NULL,
            PRIMARY KEY (cIdSede)
        )
        """
        cursor.execute(create_table_sede)
        print("Tabla Sede creada exitosamente o ya existe.")
        # Crear tabla Momento
        create_table_momento = """ 
        CREATE TABLE IF NOT EXISTS Momento(
            cIdMomento INT AUTO_INCREMENT,
            cDescripcionMomento VARCHAR(100) NOT NULL,
            PRIMARY KEY (cIdMomento)
        )
        """
        cursor.execute(create_table_momento)
        print("Tabla Momento creada exitosamente o ya existe.")
        # Crear tabla Docente con llave foránea a Genero
        create_table_docente = """ 
        CREATE TABLE IF NOT EXISTS Docente(
            cIdDocente INT AUTO_INCREMENT,
            cNombre1 VARCHAR(100) NOT NULL,
            cNombre2 VARCHAR(100),
            cApellido1 VARCHAR(100) NOT NULL,
            cApellido2 VARCHAR(100),
            cEmailPersonal VARCHAR(100) NOT NULL,
            cEmailInstitucional VARCHAR(100) NOT NULL,
            cTelefono VARCHAR(15) NOT NULL,
            cContraseña VARCHAR(100) NOT NULL,
            cIdGenero INT,
            PRIMARY KEY (cIdDocente),
            FOREIGN KEY (cIdGenero) REFERENCES Genero(cIdGenero)
        )
        """
        cursor.execute(create_table_docente)
        print("Tabla Docente creada exitosamente o ya existe.")
        # Crear tabla Curso
        create_table_curso = """ 
        CREATE TABLE IF NOT EXISTS Curso(
            Nrc INT AUTO_INCREMENT,
            cNomCurso VARCHAR(100) NOT NULL,
            dFechaInicio DATE NOT NULL,
            dFechaFin DATE NOT NULL,
            PRIMARY KEY (Nrc)
        )
        """
        cursor.execute(create_table_curso)
        print("Tabla Curso creada exitosamente o ya existe.")

        # Confirmar los cambios
        connection.commit()

except Error as e:
    print("Error al conectarse al MySQL:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada en la base de datos.")
