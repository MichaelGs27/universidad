import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="universidad"
        )
        return connection
    except Error as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None

def insertar_tipo_sede(codigo, descripcion):
    connection = crear_conexion()
    if not connection:
        print("No se pudo establecer conexion")
        return
    try:
        cursor = connection.cursor()
        #Se crea la transaccion
        connection.start_transaction()
        cursor.execute("USE universidad")

        IcInsert = f"INSERT INTO sede(cIdSede, cNomSede)VALUES(%s, %s)"
        cursor.execute(IcInsert,(codigo,descripcion))

        #confirmar los cambios
        connection.commit()
        print ("programa registrado exitosamente.")
    except Error as e:
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close() #Se cierra el cursor
            connection.close() #Se cierra la conexion 
            print("Conexión cerrada en la base de datos.")
            
def actualizar_tipo_sede(codigo, descripcion):
    connection = crear_conexion()
    if not connection:
        print("No se pudo establecer conexion")
        return
    try:

        cursor = connection.cursor()
        cursor.execute("USE universidad")

        #Se crea la transaccion
        connection.start_transaction()

        IcUpdate = f"""UPDATE sede
                    SET 
                        cNomSede = "%s"
                    WHERE 
                        cIdSede = "%s"
                        """
        cursor.execute(IcUpdate,(codigo,descripcion))

        #confirmar los cambios
        connection.commit()
        print ("programa registrado exitosamente.")
    except Error as e:
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada en la base de datos.")
    