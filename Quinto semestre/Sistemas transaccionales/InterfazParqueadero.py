import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# -------------------- Conexión --------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        database="Parqueadero"
    )

# -------------------- Funciones --------------------
def registrar_entrada():
    placa = entry_placa.get().upper()
    tipo = tipo_var.get()

    if not placa or not tipo:
        messagebox.showwarning("Campos Vacíos", "Debe ingresar placa y tipo.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verificar si el vehículo ya está registrado
        cursor.execute("SELECT idVehiculo FROM Vehiculo WHERE placa = %s", (placa,))
        vehiculo = cursor.fetchone()

        if not vehiculo:
            cursor.execute("INSERT INTO Vehiculo (placa, tipoVehiculo) VALUES (%s, %s)", (placa, tipo))
            conn.commit()
            id_vehiculo = cursor.lastrowid
        else:
            id_vehiculo = vehiculo[0]

        # Seleccionar un espacio libre según el tipo de vehículo
        cursor.execute("""
            SELECT idEspacio FROM Espacio
            WHERE tipoEspacio = %s AND disponible = TRUE
            LIMIT 1
        """, (tipo,))
        espacio = cursor.fetchone()

        if not espacio:
            messagebox.showwarning("Sin Espacios Disponibles", "No hay espacios disponibles para este tipo de vehículo.")
            return

        # Marcar el espacio como no disponible
        cursor.execute("UPDATE Espacio SET disponible = FALSE WHERE idEspacio = %s", (espacio[0],))
        conn.commit()

        # Insertar entrada en la tabla Registro con el id del espacio
        cursor.execute("""
            INSERT INTO Registro (idVehiculo, idEspacio, horaEntrada)
            VALUES (%s, %s, NOW())
        """, (id_vehiculo, espacio[0]))
        conn.commit()
        messagebox.showinfo("Éxito", "Entrada registrada.")
        entry_placa.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Error al registrar entrada: {e}")
    finally:
        conn.close()

def registrar_salida():
    placa = entry_placa.get().upper()
    if not placa:
        messagebox.showwarning("Campos Vacíos", "Debe ingresar la placa.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Obtener id del vehículo y tipo
        cursor.execute("SELECT idVehiculo, tipoVehiculo FROM Vehiculo WHERE placa = %s", (placa,))
        vehiculo = cursor.fetchone()
        if not vehiculo:
            messagebox.showwarning("No encontrado", "Vehículo no registrado.")
            return

        id_vehiculo, tipo = vehiculo

        # Buscar el último registro sin salida
        cursor.execute("""
            SELECT r.idRegistro, r.idEspacio FROM Registro r
            JOIN Espacio e ON r.idEspacio = e.idEspacio
            WHERE r.idVehiculo = %s AND r.horaSalida IS NULL
            ORDER BY r.horaEntrada DESC LIMIT 1
        """, (id_vehiculo,))
        registro = cursor.fetchone()

        if not registro:
            messagebox.showwarning("Sin registro", "No hay entrada activa para esta placa.")
            return

        id_registro, id_espacio = registro

        # Actualizar la hora de salida y el valor
        hora_salida = datetime.now()
        valor = 3500 if tipo == "Carro" else 2400

        cursor.execute("""
            UPDATE Registro 
            SET horaSalida = %s, valor = %s 
            WHERE idRegistro = %s
        """, (hora_salida, valor, id_registro))
        conn.commit()

        # Liberar el espacio
        cursor.execute("UPDATE Espacio SET disponible = TRUE WHERE idEspacio = %s", (id_espacio,))
        conn.commit()

        messagebox.showinfo("Salida Registrada", f"Salida registrada.\nTotal: ${valor}")
        entry_placa.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Error al registrar salida: {e}")
    finally:
        conn.close()

def ver_registros():
    for i in tabla.get_children():
        tabla.delete(i)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.placa, v.tipoVehiculo, e.codigoEspacio, r.horaEntrada, r.horaSalida, r.valor
            FROM Vehiculo v
            JOIN Registro r ON v.idVehiculo = r.idVehiculo
            JOIN Espacio e ON r.idEspacio = e.idEspacio
            ORDER BY r.horaEntrada DESC
        """)
        for row in cursor.fetchall():
            # Mostrar placa, tipo de vehículo, espacio (código del espacio), hora de entrada, hora de salida y valor
            tabla.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar registros: {e}")
    finally:
        conn.close()



# -------------------- Interfaz --------------------
root = tk.Tk()
root.title("Parqueadero - Registro")
root.geometry("500x500")
root.configure(bg="#2c3e50")

tk.Label(root, text="Gestión de Vehículos", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=5)

tk.Label(frame, text="Placa:", fg="white", bg="#2c3e50", font=("Arial", 12)).grid(row=0, column=0, sticky="e")
entry_placa = tk.Entry(frame, font=("Arial", 12))
entry_placa.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Tipo (carro/moto):", fg="white", bg="#2c3e50", font=("Arial", 12)).grid(row=1, column=0, sticky="e")
tipo_var = tk.StringVar()
tipo_menu = ttk.Combobox(frame, textvariable=tipo_var, values=["Carro", "Moto"], state="readonly")
tipo_menu.grid(row=1, column=1, padx=10, pady=5)

btn_entrada = tk.Button(root, text="Registrar Entrada", command=registrar_entrada, bg="#27ae60", fg="white", font=("Arial", 12, "bold"))
btn_entrada.pack(pady=5)

btn_salida = tk.Button(root, text="Registrar Salida", command=registrar_salida, bg="#e67e22", fg="white", font=("Arial", 12, "bold"))
btn_salida.pack(pady=5)

btn_ver = tk.Button(root, text="Ver Registros", command=ver_registros, bg="#3498db", fg="white", font=("Arial", 12, "bold"))
btn_ver.pack(pady=5)

tabla = ttk.Treeview(root, columns=("Placa", "Tipo", "Espacio", "Entrada", "Salida", "Valor"), show="headings")
for col in tabla["columns"]:
    tabla.heading(col, text=col)
tabla.pack(pady=10, fill="x", padx=10)

btn_salir = tk.Button(root, text="Salir", command=root.destroy, bg="#c0392b", fg="white", font=("Arial", 12, "bold"))
btn_salir.pack(pady=10)

root.mainloop()
