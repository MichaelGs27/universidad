import mysql.connector
from mysql.connector import Error


class Database:
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
        # PROGRAMA
        def crear_programa(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO programa (idPrograma, cNomPrograma) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Programa creado exitosamente."
            except Exception as e:
                return f"Error al crear en programa: {e}"

        def actualizar_programa(self, id, nombre):
            try:
                self.cursor.execute("UPDATE programa SET cNomPrograma=%s WHERE idPrograma=%s", (nombre, id))
                self.connection.commit()
                return "Programa actualizado correctamente."
            except Exception as e:
                return f"Error al actualizar programa: {e}"

        def consultar_programas(self):
            try:
                self.cursor.execute("SELECT * FROM programa")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar programas: {e}"

        def eliminar_programa(self, id):
            try:
                self.cursor.execute("DELETE FROM programa WHERE idPrograma=%s", (id,))
                self.connection.commit()
                return "Programa eliminado correctamente."
            except Exception as e:
                return f"Error al eliminar programa: {e}"

        # Periodo

        def crear_periodo(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO periodo (idPeriodo, cDescripcionPeriodo) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Periodo creado exitosamente."
            except Exception as e:
                return f"Error al crear en periodo: {e}"

        def actualizar_periodo(self, id, nombre):
            try:
                self.cursor.execute("UPDATE periodo SET cDescripcionPeriodo=%s WHERE idPeriodo=%s", (nombre, id))
                self.connection.commit()
                return "Periodo actualizado correctamente."
            except Exception as e:
                return f"Error al actualizar periodo: {e}"

        def consultar_periodos(self):
            try:
                self.cursor.execute("SELECT * FROM periodo")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar periodos: {e}"

        def eliminar_periodo(self, id):
            try:
                self.cursor.execute("DELETE FROM periodo WHERE idPeriodo=%s", (id,))
                self.connection.commit()
                return "Periodo eliminado correctamente."
            except Exception as e:
                return f"Error al eliminar periodo: {e}"

        # Sede

        def crear_sede(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO sede (idSede, cNomSede) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Sede creada exitosamente."
            except Exception as e:
                return f"Error al crear en sede: {e}"

        def actualizar_sede(self, id, nombre):
            try:
                self.cursor.execute("UPDATE sede SET cNomSede=%s WHERE idSede=%s", (nombre, id))
                self.connection.commit()
                return "Sede actualizada correctamente."
            except Exception as e:
                return f"Error al actualizar sede: {e}"

        def consultar_sedes(self):
            try:
                self.cursor.execute("SELECT * FROM sede")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar sedes: {e}"

        def eliminar_sede(self, id):
            try:
                self.cursor.execute("DELETE FROM sede WHERE idSede=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar sede: {e}"
        
        # Momento 

        def crear_Momento(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO sede (cIdMomento, cDescripcionMomento) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Sede creada exitosamente."
            except Exception as e:
                return f"Error al crear en sede: {e}"

        def actualizar_momento(self, id, nombre):
            try:
                self.cursor.execute("UPDATE sede SET cDescripcionMomento=%s WHERE cIdMomento=%s", (nombre, id))
                self.connection.commit()
                return "Sede actualizada correctamente."
            except Exception as e:
                return f"Error al actualizar momento: {e}"

        def consultar_momento(self):
            try:
                self.cursor.execute("SELECT * FROM momento")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar momento: {e}"

        def eliminar_momento(self, id):
            try:
                self.cursor.execute("DELETE FROM sede WHERE cIdMomento=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar momento: {e}"

        # Modalidad

        def crear_Modalidad(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO sede (cIdModalidad, cNomModalidad) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Sede creada exitosamente."
            except Exception as e:
                return f"Error al crear en modalidad: {e}"

        def actualizar_Modalidad(self, id, nombre):
            try:
                self.cursor.execute("UPDATE sede SET cNomModalidad=%s WHERE cIdModalidad=%s", (nombre, id))
                self.connection.commit()
                return "Sede actualizada correctamente."
            except Exception as e:
                return f"Error al actualizar modalidad: {e}"

        def consultar_modalidad(self):
            try:
                self.cursor.execute("SELECT * FROM modalidad")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar modalidad: {e}"

        def eliminar_Modalidad(self, id):
            try:
                self.cursor.execute("DELETE FROM sede WHERE cIdModalidad=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar modalidad: {e}"
            
        # Genero

        def crear_Genero(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO sede (cIdGenero, cNomGenero) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Sede creada exitosamente."
            except Exception as e:
                return f"Error al crear en genero: {e}"

        def actualizar_Genero(self, id, nombre):
            try:
                self.cursor.execute("UPDATE sede SET cNomGenero=%s WHERE cIdGenero=%s", (nombre, id))
                self.connection.commit()
                return "Sede actualizada correctamente."
            except Exception as e:
                return f"Error al actualizar genero: {e}"

        def consultar_Generos(self):
            try:
                self.cursor.execute("SELECT * FROM genero")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar generos: {e}"

        def eliminar_Genero(self, id):
            try:
                self.cursor.execute("DELETE FROM sede WHERE cIdGenero=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar genero: {e}"
            
        # Aula

        def crear_Aula(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO sede (cIdAula, cNomAula) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Sede creada exitosamente."
            except Exception as e:
                return f"Error al crear en sede: {e}"

        def actualizar_Aula(self, id, nombre):
            try:
                self.cursor.execute("UPDATE sede SET cNomAula=%s WHERE cIdAula=%s", (nombre, id))
                self.connection.commit()
                return "Sede actualizada correctamente."
            except Exception as e:
                return f"Error al actualizar sede: {e}"

        def consultar_Aulas(self):
            try:
                self.cursor.execute("SELECT * FROM aula")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar sedes: {e}"

        def eliminar_Aula(self, id):
            try:
                self.cursor.execute("DELETE FROM sede WHERE cIdAula=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar sede: {e}"
        
        # curso

        def crear_Curso(self, id, nombre):
            try:
                self.cursor.execute("INSERT INTO sede (cIdAula, cNomAula) VALUES (%s, %s)", (id, nombre))
                self.connection.commit()
                return "Sede creada exitosamente."
            except Exception as e:
                return f"Error al crear en sede: {e}"

        def actualizar_sede(self, id, nombre):
            try:
                self.cursor.execute("UPDATE sede SET cNomSede=%s WHERE idSede=%s", (nombre, id))
                self.connection.commit()
                return "Sede actualizada correctamente."
            except Exception as e:
                return f"Error al actualizar sede: {e}"

        def consultar_sedes(self):
            try:
                self.cursor.execute("SELECT * FROM sede")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar sedes: {e}"

        def eliminar_sede(self, id):
            try:
                self.cursor.execute("DELETE FROM sede WHERE idSede=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar sede: {e}"

        # ===== CURSO 
        def crear_curso(self, id_valor, nombre, fecha_inicio, fecha_fin):
            try:
                query = "INSERT INTO Curso (Nrc, cNomCurso, dFechaInicio, dFechaFin) VALUES (%s, %s, %s, %s)"
                self.cursor.execute(query, (id_valor, nombre, fecha_inicio, fecha_fin))
                self.connection.commit()
                return "Curso creado correctamente."
            except mysql.connector.Error as e:
                return f"Error al crear curso: {e}"

        def actualizar_curso(self, id_valor, nombre, fecha_inicio, fecha_fin):
            try:
                query = "UPDATE Curso SET cNomCurso = %s, dFechaInicio = %s, dFechaFin = %s WHERE Nrc = %s"
                self.cursor.execute(query, (nombre, fecha_inicio, fecha_fin, id_valor))
                self.connection.commit()
                return "Curso actualizado correctamente."
            except mysql.connector.Error as e:
                return f"Error al actualizar curso: {e}"

        def eliminar_curso(self, id_valor):
            try:
                self.cursor.execute("DELETE FROM sede WHERE Nrc=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar sede: {e}"

        def consultar_cursos(self):
            try:
                self.cursor.execute("SELECT * FROM curso")
                datos = self.cursor.fetchall()
                return "\n".join([f"{id}: {nombre}" for id, nombre in datos])
            except Exception as e:
                return f"Error al consultar sedes: {e}"

        # DOCENTE
        def crear_docente(self, id_docente, nombre1, nombre2, apellido1, apellido2, email_personal, email_inst, telefono, contrasena, id_genero):
            try:
                self.cursor.execute("""
                    INSERT INTO docente (cIdDocente, cNombre1, cNombre2, cApellido1, cApellido2, cEmailPersonal, cEmailInstitucional, cTelefono, cContraseña, cIdGenero)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (id_docente, nombre1, nombre2, apellido1, apellido2, email_personal, email_inst, telefono, contrasena, id_genero))
                self.connection.commit()
                return "Docente creado exitosamente."
            except Exception as e:
                return str(e)

        def actualizar_docente(self, id_docente, nombre1, nombre2, apellido1, apellido2, email_personal, email_inst, telefono, contrasena, id_genero):
            try:
                self.cursor.execute("""
                    UPDATE docente SET cNombre1=%s, cNombre2=%s, cApellido1=%s, cApellido2=%s, cEmailPersonal=%s,
                    cEmailInstitucional=%s, cTelefono=%s, cContraseña=%s, cIdGenero=%s WHERE cIdDocente=%s
                """, (nombre1, nombre2, apellido1, apellido2, email_personal, email_inst, telefono, contrasena, id_genero, id_docente))
                self.connection.commit()
                return "Docente actualizado correctamente."
            except Exception as e:
                return str(e)

        def consultar_docentes(self):
            try:
                self.cursor.execute("SELECT * FROM docente")
                docentes = self.cursor.fetchall()
                return "\n".join(str(d) for d in docentes)
            except Exception as e:
                return str(e)

        def eliminar_docente(self, id_docente):
            try:
                self.cursor.execute("DELETE FROM sede WHERE cIdDocente=%s", (id,))
                self.connection.commit()
                return "Sede eliminada correctamente."
            except Exception as e:
                return f"Error al eliminar sede: {e}"
    except Error as e:
        print("Error al conectarse al MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada en la base de datos.")
