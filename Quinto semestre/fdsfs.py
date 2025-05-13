import tkinter as tk
from tkinter import messagebox
from datetime import datetime 

# --- Datos simulados ---
usuarios = {
    "admin": {"password": "123", "rol": "admin"},
    "trabajador": {"password": "trabajador123", "rol": "trabajador"},
}

# --- Funciones ---
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        rol = usuarios[usuario]["rol"]
        ventana_login.destroy()
        if rol == "admin":
            mostrar_panel_admin()
        elif rol == "trabajador":
            mostrar_panel_trabajador()
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

def mostrar_panel_admin():
    admin = tk.Tk()
    admin.title("Administrador - Parqueadero")
    admin.geometry("500x300")
    admin.configure(bg="#2c3e50")

    tk.Label(admin, text="Panel del Administrador", font=("Arial", 18, "bold"), fg="white", bg="#2c3e50").pack(pady=20)
    tk.Label(admin, text="Aquí se mostrarán los registros del parqueadero.", font=("Arial", 12), fg="white", bg="#2c3e50").pack(pady=10)
    
    tk.Button(admin, text="Salir", command=admin.destroy, bg="#e74c3c", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    admin.mainloop()

def mostrar_panel_trabajador():
    trabajador = tk.Tk()
    trabajador.title("Registro Vehículos - Parqueadero")
    trabajador.geometry("400x400")
    trabajador.configure(bg="#34495e")

    tk.Label(trabajador, text="Registrar Vehículo", font=("Arial", 16, "bold"), fg="white", bg="#34495e").pack(pady=20)

    frame = tk.Frame(trabajador, bg="#34495e")
    frame.pack()

    tk.Label(frame, text="Placa:", font=("Arial", 12), fg="white", bg="#34495e").grid(row=0, column=0, pady=5, sticky="e")
    entry_placa = tk.Entry(frame, font=("Arial", 12))
    entry_placa.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Tipo (carro/moto):", font=("Arial", 12), fg="white", bg="#34495e").grid(row=1, column=0, pady=5, sticky="e")
    entry_tipo = tk.Entry(frame, font=("Arial", 12))
    entry_tipo.grid(row=1, column=1, pady=5)

    def registrar_vehiculo():
        placa = entry_placa.get()
        tipo = entry_tipo.get().lower()
        tarifa = 3500 if tipo == "carro" else 2400 if tipo == "moto" else None
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # <-- Formato de fecha y hora

        if tarifa:
            messagebox.showinfo("Registrado", f"Placa: {placa}\nTipo: {tipo}\nTarifa: ${tarifa}\nFecha y hora: {fecha_hora}")
        else:
            messagebox.showerror("Error", "Tipo de vehículo no válido")

    tk.Button(trabajador, text="Registrar", command=registrar_vehiculo, bg="#27ae60", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
    tk.Button(trabajador, text="Salir", command=trabajador.destroy, bg="#c0392b", fg="white", font=("Arial", 12, "bold")).pack()

    trabajador.mainloop()

# --- Interfaz de login ---
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión - Parqueadero")
ventana_login.geometry("400x300")
ventana_login.configure(bg="#1abc9c")

tk.Label(ventana_login, text="Iniciar Sesión", font=("Arial", 18, "bold"), bg="#1abc9c", fg="white").pack(pady=20)

frame_login = tk.Frame(ventana_login, bg="#1abc9c")
frame_login.pack()

tk.Label(frame_login, text="Usuario:", font=("Arial", 12), bg="#1abc9c", fg="white").grid(row=0, column=0, pady=5, sticky="e")
entry_usuario = tk.Entry(frame_login, font=("Arial", 12))
entry_usuario.grid(row=0, column=1, pady=5)

tk.Label(frame_login, text="Contraseña:", font=("Arial", 12), bg="#1abc9c", fg="white").grid(row=1, column=0, pady=5, sticky="e")
entry_contraseña = tk.Entry(frame_login, show="*", font=("Arial", 12))
entry_contraseña.grid(row=1, column=1, pady=5)

tk.Button(ventana_login, text="Entrar", command=verificar_login, bg="#2980b9", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

ventana_login.mainloop()
