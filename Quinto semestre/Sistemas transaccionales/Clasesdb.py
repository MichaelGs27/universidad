# Archivo: database.py
import mysql.connector
from mysql.connector import Error
#Se crea la base de datos 
class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="dbLogin"
            )
            self.cursor = self.connection.cursor()
            print("Conexión a la base de datos exitosa")
        except Error as e:
            print(f"Error en la conexión a la base de datos: {e}")
            self.connection = None
    #Se crea el metodo para crear el usuario
    def crear_usuario(self, cNombre, cContraseña):
        if not cNombre or not cContraseña:
            return "Error: Usuario y Contraseña requeridos."
        
        try:
            self.cursor.execute(f"INSERT INTO Usuario (cNomUsuario, cContraseña) VALUES ('{cNombre}', '{cContraseña}')")
            self.connection.commit()
            return "Usuario registrado exitosamente."
        except Error as e:
            return f"Error al registrar usuario: {e}"
    #Se crea el metodo para verificar el usuario
    def verificar_usuario(self, cNombre, cContraseña):
        self.cursor.execute(f"SELECT * FROM Usuario WHERE cNomUsuario = '{cNombre}' AND cContraseña = '{cContraseña}'")
        return self.cursor.fetchone() is not None
    #Insertar programa
    def InsertarPrograma(self, cIdPrograma, CNomPrograma):
        if not cIdPrograma or not CNomPrograma:
            return "Error: ID y Nombre del programa requeridos."
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
                cursor.execute("USE universidad")

                #Se crea la transaccion
                connection.start_transaction()

                IcInsert = f"INSERT INTO universidad.programa(cIdPrograma, cNomPrograma) VALUES ('{cIdPrograma}', '{CNomPrograma}')"
                cursor.execute(IcInsert)

                #confirmar los cambios
                connection.commit()
                return "programa registrado exitosamente."
        except Error as e:
            connection.rollback()
            return f"Error al registrar usuario: {e}"
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexión cerrada en la base de datos.")
    #Se crea el metodo actualizar programa
    def ActualizarPrograma(self, cIdPrograma, CNomProgramaNuevo ):
        if not cIdPrograma or not CNomProgramaNuevo:
            return "Error: ID y Nombre del programa requeridos."
        IcSelect = "SELECT * from universidad.cIdPrograma ORDER BY cIdPrograma"
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
                cursor.execute("USE universidad")
                cursor.execute(IcSelect)

                #Se obtienen los registros de la consulta 
                cId = cursor.fetchall()
                print("Total registros: ", cursor.rowcount)
                print("Registros: ")
                for row in cId:
                    print(row)
                #Se crea la transaccion
                    connection.start_transaction()
                    IcUpdate = f"""UPDATE programa
                                SET 
                                    cNomPrograma = '{CNomProgramaNuevo}'
                                WHERE 
                                    cIdPrograma = '{cIdPrograma}'
                                    """
                    cursor.execute(IcUpdate)
                    #confirmar los cambios
                    connection.commit()
                    return "programa actualizado exitosamente."
        except Error as e:
            connection.rollback()
            return "Error al registrar usuario: No existe en la base de datos "
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()   
                print("Conexión cerrada en la base de datos.")
    #se crea el metodo eliminar programa
    def EliminarPrograma(self, cIdPrograma):
        if not cIdPrograma:
            return "Error: ID y Nombre del programa requeridos."
        IcSelect = "SELECT * from universidad.cIdPrograma ORDER BY cIdPrograma"
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
                cursor.execute("USE universidad")
                cursor.execute(IcSelect)

                #Se obtienen los registros de la consulta 
                cId = cursor.fetchall()
                print("Total registros: ", cursor.rowcount)
                print("Registros: ")
                for row in cId:
                    print(row)
                #Se crea la transaccion
                connection.start_transaction()
                cEliminar = f"DELETE FROM universidad.programa WHERE cIdPrograma = '{cIdPrograma}'"
                cursor.execute(cEliminar)
                #confirmar los cambios
                connection.commit()
                return "programa eliminado exitosamente."
        except Error as e:
            connection.rollback()
            return f"Error al eliminar el programa. {e}"
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexión cerrada en la base de datos.")
    #Se crea el metodo consultar programa 
    def ConsultarPrograma(self):
        try:
    # Conexión a la base de datos correcta
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="",  
                database="universidad"  
            )

            cursor = connection.cursor()
            # Consulta la tabla "programas"
            cursor.execute("SELECT * FROM programa")
            programas = cursor.fetchall()

            # Construcción del mensaje
            resultado = "Programas registrados:\n"
            for programa in programas:
                resultado += f"ID: {programa[0]}, Nombre: {programa[1]}\n"
            
            return(resultado)  #Muestra la consulta

        except mysql.connector.Error as error:
            return(f"Error al consultar programas: {error}")

        finally:
            if 'coconnection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
    #Cierra la conexion con la base de datos 
    def cerrar_coconnection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Conexión cerrada.")