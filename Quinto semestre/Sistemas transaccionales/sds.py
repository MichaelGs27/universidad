from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from fs import Database

class MenuPrincipal:
    def __init__(self, root):
        self.Ventana = root
        self.Ventana.title("Menu Principal")
        self.Ventana.geometry("850x600")
        self.Ventana.config(bg="teal")

        self.db = Database()

        self.metodos_crud = {
            "Programa": "programa",
            "Periodo": "periodo",
            "Sede": "sede",
            "Momento": "momento",
            "Modalidad": "modalidad",
            "Genero": "genero",
            "Aula": "aula",
            "Curso": "curso",
            "Docente": "docente"
        }

        frame1 = LabelFrame(self.Ventana, text="Datos a ingresar", font=("calibri", 14))
        frame1.pack(fill="both", expand="yes", padx=20, pady=15)

        self.opciones = list(self.metodos_crud.keys())

        for idx, opcion in enumerate(self.opciones):
            Button(frame1, text=opcion, width=12, height=2, command=lambda opt=opcion: self.mostrar_submenu(opt)).grid(row=1, column=idx, padx=10, pady=10)

        Button(frame1, text="Salir", width=12, height=2, command=self.Ventana.destroy).grid(row=2, column=0, padx=10, pady=10)
        self.ventana_menu = None

    def mostrar_submenu(self, tipo):
        if self.ventana_menu:
            self.ventana_menu.destroy()

        self.ventana_menu = Toplevel(self.Ventana)
        self.ventana_menu.title(f"Menú - {tipo}")
        self.ventana_menu.geometry("300x300")
        self.ventana_menu.config(bg="lightgray")

        Label(self.ventana_menu, text=f"Gestionar {tipo}", font=("Arial", 12, "bold")).pack(pady=10)

        Button(self.ventana_menu, text="1. Crear", width=20, command=lambda: self.operacion_tipo("Crear", tipo)).pack(pady=5)
        Button(self.ventana_menu, text="2. Actualizar", width=20, command=lambda: self.operacion_tipo("Actualizar", tipo)).pack(pady=5)
        Button(self.ventana_menu, text="3. Consultar", width=20, command=lambda: self.operacion_tipo("Consultar", tipo)).pack(pady=5)
        Button(self.ventana_menu, text="4. Eliminar", width=20, command=lambda: self.operacion_tipo("Eliminar", tipo)).pack(pady=5)
        Button(self.ventana_menu, text="5. Cerrar", width=20, command=self.ventana_menu.destroy).pack(pady=10)

    def operacion_tipo(self, operacion, tipo):
        if not self.db.connection:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return

        tipo_metodo = self.metodos_crud.get(tipo, tipo.lower())
        metodo_consulta = f"consultar_{tipo_metodo}"

        if operacion == "Consultar":
            if hasattr(self.db, metodo_consulta):
                mensaje = getattr(self.db, metodo_consulta)()
                messagebox.showinfo(f"{tipo}s Registrados", mensaje)
            else:
                messagebox.showerror("Error", f"Método {metodo_consulta} no encontrado en la base de datos.")
            return

        ventana_op = Toplevel(self.ventana_menu)
        ventana_op.title(f"{operacion} {tipo}")
        ventana_op.geometry("350x400")
        ventana_op.config(bg="lightgray")

        Label(ventana_op, text=f"{operacion} {tipo}", font=("Arial", 12, "bold")).pack(pady=10)
        frame_form = Frame(ventana_op)
        frame_form.pack(pady=10)

        campos = {"Programa": ["ID", "Nombre"],
                  "Periodo": ["ID", "Nombre"],
                  "Sede": ["ID", "Nombre"],
                  "Momento": ["ID", "Nombre"],
                  "Modalidad": ["ID", "Nombre"],
                  "Genero": ["ID", "Nombre"],
                  "Aula": ["ID", "Nombre"],
                  "Curso": ["NRC", "Nombre", "Fecha Inicio", "Fecha Fin"],
                  "Docente": ["ID", "Nombre", "Apellido", "Correo"]}

        self.entries = {}
        for idx, campo in enumerate(campos[tipo]):
            Label(frame_form, text=f"{campo}: ", font=("Arial", 12)).grid(row=idx, column=0, padx=5, pady=5, sticky="e")
            entry = Entry(frame_form, width=25)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            self.entries[campo.lower()] = entry

        Button(ventana_op, text=operacion, width=16, font=("Arial", 12), command=lambda: self.ejecutar_operacion(operacion, tipo)).pack(pady=5)
        Button(ventana_op, text="Cerrar", width=16, font=("Arial", 12), command=ventana_op.destroy).pack(pady=5)

    def ejecutar_operacion(self, operacion, tipo):
        tipo_metodo = self.metodos_crud.get(tipo, tipo.lower())
        metodo = f"{operacion.lower()}_{tipo_metodo}"

        if not hasattr(self.db, metodo):
            messagebox.showerror("Error", f"Operación {operacion} no válida para {tipo}.")
            return

        try:
            if tipo == "Curso":
                if operacion == "Eliminar":
                    mensaje = getattr(self.db, metodo)(int(self.entries["nrc"].get()))
                elif operacion == "Crear":
                    mensaje = getattr(self.db, metodo)(int(self.entries["nrc"].get()), self.entries["nombre"].get(), self.entries["fecha inicio"].get(), self.entries["fecha fin"].get())
                else:
                    mensaje = getattr(self.db, metodo)(int(self.entries["nrc"].get()), self.entries["nombre"].get(), self.entries["fecha inicio"].get(), self.entries["fecha fin"].get())

            elif tipo == "Docente":
                if operacion == "Eliminar":
                    mensaje = getattr(self.db, metodo)(int(self.entries["id"].get()))
                elif operacion == "Crear":
                    mensaje = getattr(self.db, metodo)(int(self.entries["id"].get()), self.entries["nombre"].get(), self.entries["apellido"].get(), self.entries["correo"].get())
                else:
                    mensaje = getattr(self.db, metodo)(int(self.entries["id"].get()), self.entries["nombre"].get(), self.entries["apellido"].get(), self.entries["correo"].get())

            else:
                id_valor = int(self.entries["id"].get())
                if operacion == "Eliminar":
                    mensaje = getattr(self.db, metodo)(id_valor)
                else:
                    nombre = self.entries["nombre"].get()
                    mensaje = getattr(self.db, metodo)(id_valor, nombre)

            messagebox.showinfo("Resultado", mensaje)
        except Exception as e:
            messagebox.showerror("Error en operación", str(e))

if __name__ == "__main__":
    root = Tk()
    app = MenuPrincipal(root)
    root.mainloop()

