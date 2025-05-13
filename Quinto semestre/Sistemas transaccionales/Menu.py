import mysql.connector
from mysql.connector import Error
#Menu
Menu = 0
Salir  = "Si" or "si"
while Menu == 0:
    try:
        nOpcion = int(input ("""-----MENU-------
                        0. Salir
                        1. Programa
                        2. Periodo
                        3. Sede
                        4. Momento
                        5. Modalidad
                        6. Genero
                        7. Aula:  """))
    except:
        print("Valores invalidos.")
    else:
        if nOpcion == 1:
            nOpcion1 = input("""--------------MENU PROGRAMA-----------------
                            1. Crear programa
                            2. Actualizar programa
                            3. Consultar programa
                            4. Eliminar programa
                            5. Regresar: """)
            #Opcion insertar 
            if nOpcion1 == "1": 
                cIdPrograma = input("Digite el ID del programa: ")
                CNomPrograma = input("Digite el nombre del programa: ")
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
                except Error as e:
                    print ("Error al realizar insercción del registro sobre la base de datos.", e)
                    connection.rollback()
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("Conexión cerrada en la base de datos.")
            #Opcion Actualizar 
            elif nOpcion1 == "2":
                cIdPrograma1 = int(input("Digite el ID para actualizar: "))
                cNomProgramaNuevo = input("Digite el nombre que quiere cambiar: ")
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

                        IcUpdate = f"""UPDATE programa
                                    SET 
                                        cNomPrograma = "{cNomProgramaNuevo}"
                                    WHERE 
                                        cIdPrograma = "{cIdPrograma1}"
                                        """
                        cursor.execute(IcUpdate)

                        #confirmar los cambios
                        connection.commit()
                except Error as e:
                    print ("Error al realizar insercción del registro sobre la base de datos.", e)
                    connection.rollback()
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("Conexión cerrada en la base de datos.")

                 
        elif nOpcion == 2:
            nOpcion1 = input("""--------------MENU PERIODO-----------------
                            1. Crear periodo
                            2. Actualizar periodo
                            3. Consultar periodo
                            4. Eliminar periodo
                            5. Regresar: """)
        elif nOpcion == 3:
            nOpcion1 = input("""--------------MENU SEDE-----------------
                            1. Crear sede
                            2. Actualizar sede
                            3. Consultar sede
                            4. Eliminar sede
                            5. Regresar: """)
        elif nOpcion == 4:
            nOpcion1 = input("""--------------MENU MOMENTO-----------------
                            1. Crear momento
                            2. Actualizar momento
                            3. Consultar momento
                            4. Eliminar momento
                            5. Regresar: """)
        elif nOpcion == 5:
            nOpcion1 = input("""--------------MENU MODALIDAD-----------------
                            1. Crear modalidad
                            2. Actualizar modalidad
                            3. Consultar modalidad
                            4. Eliminar modalidad
                            5. Regresar: """)
        elif nOpcion == 6:
            nOpcion1 = input("""--------------MENU GENERO-----------------
                            1. Crear genero
                            2. Actualizar genero
                            3. Consultar genero
                            4. Eliminar genero
                            5. Regresar: """)
        elif nOpcion == 7:
            nOpcion1 = input("""--------------MENU AULA-----------------
                            1. Crear aula
                            2. Actualizar aula
                            3. Consultar aula
                            4. Eliminar aula
                            5. Regresar: """)
        elif nOpcion == 0:
                Salir = str(input("¿Deseas salir de programa?(Si/No): "))
                if Salir == 'Si' or 'si':
                        print("Hasta luego...")   
                        break                
                else:
                    print("Sigues en el programa...")
        else:
                print("Opcion invalida, intente de nuevo")