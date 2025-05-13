from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Clasesdb import Database

class MenuPrincipal:
    def __init__(self, root):
        # Configuración inicial de la interfaz gráfica
        self.Ventana = root
        self.Ventana.title("Menu Principal")
        self.Ventana.geometry("850x600")
        self.Ventana.config(bg="teal")
        # Crear dos marcos (frames) para organizar la interfaz
        frame1 = LabelFrame(self.Ventana, text="Datos a ingresar", font=("calibri", 14))
        # Empaquetar los marcos en la ventana principal
        frame1.pack(fill="both", expand="yes", padx=20, pady=15)
        # Crear botones en el frame1 con funciones asociadas
        btn1 = Button(frame1, text="Programa", width=12, height=2, command=self.menuPrograma)
        btn1.grid(row=1, column=0, padx=10, pady=10)
        btn2 = Button(frame1, text="Periodo", width=12, height=2, command= self.menuPrograma)
        btn2.grid(row=1, column=1, padx=10, pady=10)
        btn3 = Button(frame1, text="Sede", width=12, height=2, command= self.menuPrograma)
        btn3.grid(row=1, column=2, padx=10, pady=10)
        btn4 = Button(frame1, text="Momento", width=12, height=2, command= self.menuPrograma)
        btn4.grid(row=1, column=3, padx=10, pady=10)
        btn5 = Button(frame1, text="Modalidad", width=12, height=2, command= self.menuPrograma)
        btn5.grid(row=1, column=4, padx=10, pady=10)
        btn6 = Button(frame1, text="Genero", width=12, height=2, command= self.menuPrograma)
        btn6.grid(row=1, column=5, padx=10, pady=10)
        btn7 = Button(frame1, text="Aula", width=12, height=2, command= self.menuPrograma)
        btn7.grid(row=1, column=6, padx=10, pady=10)
        btn8 = Button(frame1, text="Salir", width=12, height=2, command= self.Ventana.destroy)
        btn8.grid(row=2, column=0, padx=10, pady=10)

    def menuPrograma(self):
        #Abre un mini menú emergente con opcione
        ventana_menu = Toplevel(self.Ventana)
        ventana_menu.title("Menú")
        ventana_menu.geometry("300x300")
        ventana_menu.config(bg="lightgray")

        Label(ventana_menu, text="Seleccione una opción:", font=("Arial", 12, "bold")).pack(pady=10)

        Button(ventana_menu, text="1. Crear", width=20, command= self.CrearPrograma).pack(pady=5)
        Button(ventana_menu, text="2. Actualizar", width=20, command=self.ActualizarPrograma).pack(pady=5)
        Button(ventana_menu, text="3. Consultar", width=20, command=self.ConsultarPrograma).pack(pady=5)
        Button(ventana_menu, text="4. Eliminar", width=20, command=self.EliminarPrograma).pack(pady=5)
        Button(ventana_menu, text="5. Regresar", width=20, command=ventana_menu.destroy).pack(pady=10)
    #Crear programa
    def CrearPrograma(self):
        self.db = Database()
        if not self.db.connection:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return
        # Se abre otro submenú
        ventana_menu = Toplevel(self.Ventana)
        ventana_menu.title("Crear Programa")
        ventana_menu.geometry("300x300")
        ventana_menu.config(bg="lightgray")
        Label(ventana_menu, text="Seleccionaste crear programa", font=("Arial", 12, "bold")).pack(pady=10)
        #Crear un Frame dentro de ventana_menu para usar grid()
        frame_form = Frame(ventana_menu)
        frame_form.pack(pady=10)
        # ID del programa
        Label(frame_form, text="ID: ", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_ID = Entry(frame_form, width=20)
        self.entry_ID.grid(row=0, column=1, padx=5, pady=5)
        # Nombre del programa
        Label(frame_form, text="Nombre del Programa: ", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_NomPrograma = Entry(frame_form, width=20)
        self.entry_NomPrograma.grid(row=1, column=1, padx=5, pady=5)
        # Botón Crear
        Button(ventana_menu, text="Crear", width=16, font=("Arial", 12), command=self.crear_Programa).pack(pady=5)
        # Botón Salir
        Button(ventana_menu, text="Cerrar", width=16, font=("Arial", 12), command=ventana_menu.destroy).pack(pady=5)

    def crear_Programa(self):
        cIdPrograma = self.entry_ID.get()
        cNomPrograma = self.entry_NomPrograma.get()
        mensaje = self.db.InsertarPrograma(cIdPrograma, cNomPrograma)
        messagebox.showinfo("Resultado", mensaje)
    
    def ConsultarPrograma(self):
        self.db = Database()
        if not self.db.connection:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return
        mensaje = self.db.ConsultarPrograma()
        messagebox.showinfo("Programas Registrados", mensaje)


    #Actualizar programa
    def ActualizarPrograma(self):
        self.db = Database()
        if not self.db.connection:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return
        # Se abre otro submenú
        ventana_menu = Toplevel(self.Ventana)
        ventana_menu.title("Actualizar Programa")
        ventana_menu.geometry("500x500")
        ventana_menu.config(bg="lightgray")
        Label(ventana_menu, text="Seleccionaste actualizar programa", font=("Arial", 12, "bold")).pack(pady=10)
        #Crear un Frame dentro de ventana_menu para usar grid()
        frame_form = Frame(ventana_menu)
        frame_form.pack(pady=10)
        # ID del programa
        Label(frame_form, text="""Digite el Id 
                            que va a actualizar: """, font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_ID = Entry(frame_form, width=20)
        self.entry_ID.grid(row=0, column=1, padx=5, pady=5)
        # Nombre del programa
        Label(frame_form, text="""Digite el nuevo 
                            nombre del programa:""", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_NomProgramaNuevo = Entry(frame_form, width=20)
        self.entry_NomProgramaNuevo.grid(row=1, column=1, padx=5, pady=5)
        # Botón Crear
        Button(ventana_menu, text="Crear", width=16, font=("Arial", 12), command=self.actualizar_programa).pack(pady=5)
        # Botón Salir
        Button(ventana_menu, text="Cerrar", width=16, font=("Arial", 12), command=ventana_menu.destroy).pack(pady=5)

    def actualizar_programa(self):
        cIdPrograma = self.entry_ID.get()
        cNomProgramaNuevo = self.entry_NomProgramaNuevo.get()
        mensaje = self.db.ActualizarPrograma(cIdPrograma, cNomProgramaNuevo)
        messagebox.showinfo("Resultado", mensaje)

    def EliminarPrograma(self):
        self.db = Database()
        if not self.db.connection:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return
        # Se abre otro submenú
        ventana_menu = Toplevel(self.Ventana)
        ventana_menu.title("Eliminar Programa")
        ventana_menu.geometry("500x500")
        ventana_menu.config(bg="lightgray")
        Label(ventana_menu, text="Seleccionaste actualizar programa", font=("Arial", 12, "bold")).pack(pady=10)
        #Crear un Frame dentro de ventana_menu para usar grid()
        frame_form = Frame(ventana_menu)
        frame_form.pack(pady=10)
        # ID del programa
        Label(frame_form, text="""Digite el Id 
                            que va a eliminar: """, font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_ID = Entry(frame_form, width=20)
        self.entry_ID.grid(row=0, column=1, padx=5, pady=5)
        # Botón Eliminar
        Button(ventana_menu, text="Eliminar", width=16, font=("Arial", 12), command=self.Eliminar_programa).pack(pady=5)
        # Botón Salir
        Button(ventana_menu, text="Cerrar", width=16, font=("Arial", 12), command=ventana_menu.destroy).pack(pady=5)

    def Eliminar_programa(self):
        cIdPrograma = self.entry_ID.get()
        mensaje = self.db.EliminarPrograma(cIdPrograma)
        messagebox.showinfo("Resultado", mensaje)

# Crear la ventana raíz y ejecutar la aplicación
if __name__ == "__main__":
    root = Tk()
    app = MenuPrincipal(root)
    root.mainloop()

