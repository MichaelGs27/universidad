import Pyro5.api
import mysql.connector
import signal
import sys

@Pyro5.api.expose   #Esta anotacion permite que la clase sea expuesta a traves de RMI 
class ServicioTipoID:
    def __init__ (self):
        #Establecer la conexion con la base de datos MySQL al iniciar el servicio 
        self.conn = mysql.connector.connect(
            host = "Localhost",     #Servidor
            port = "3306",          #Puerto
            user="root",            #Usuario de MySQL
            password = ""           #Contraseña 
        )

    def consultar_descripcion(Self, codigo):
        try:
            cursor = Self.conn.cursor()
            #Seleciona la base de datos para trabajar con ella
            cursor.execute("USE universidad")
            consulta ="SELECT cDescripcionTipoId FROM tipoid WHERE cTipoId = %s"
            cursor.execute(consulta,(codigo))
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                return resultado[0]
            else:
                return "Codigo no encontrado"
        except mysql.connector.Error as err:
            return f"Error desconocido: {str(err)}"
        except Exception as e:
            #Captura cualquier error de MySQL y lo convierte en un mensaje simple
            return f"Error desconocido: {str(e)}"
    def __del__ (self):
        #Este metodo especial se ejecuta al destruit 1 objeto y cierra la conexion
        self.conn.close()

def finalizar_servidor(Self):
    print("\n [INFO] servidor finalizado correctamente ")

#Capturar CTRL +C (Señal SIGINT )para un cierre limpio
signal.signal(signal.SIGINT, finalizar_servidor)

#Configura el servidor RMI
daemon = Pyro5.api.Daemon()
uri = daemon.register(ServicioTipoID)
print("Servidor TipoId corriendo. URI:", uri)
daemon.requestLoop()