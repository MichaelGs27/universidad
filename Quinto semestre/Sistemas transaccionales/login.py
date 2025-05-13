from tkinter import Tk, messagebox, Label, Button, Entry, Frame, mainloop
from Clasesdb import Database
from menuppal import MenuPrincipal

class Login:
    def __init__(self):
        self.db = Database()
        if not self.db.connection:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return

        self.ventana = Tk()
        self.ventana.geometry("400x700")
        self.ventana.title("Login")
        self.intentos = 3
        fondo = "#88FFB4"
        
        self.frame_superior = Frame(self.ventana, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)
        
        self.frame_inferior = Frame(self.ventana, bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)
        
        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)
        
        self.titulo = Label(self.frame_superior, text="Login", font=("Calisto MT", 36, "bold"), bg=fondo)
        self.titulo.pack(side="top", pady=20)
        
        self.Label_usuario = Label(self.frame_inferior, text="Usuario: ", font=("Arial", 18), bg=fondo, fg="black")
        self.Label_usuario.grid(row=0, column=0, padx=10, sticky="e")
        
        self.Label_contraseña = Label(self.frame_inferior, text="Contraseña: ", font=("Arial", 18), bg=fondo, fg="black")
        self.Label_contraseña.grid(row=1, column=0, padx=10, sticky="e")
        
        self.entry_usuario = Entry(self.frame_inferior, bd=0, width=14, font=("Arial", 18))
        self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")
        
        self.entry_contraseña = Entry(self.frame_inferior, bd=0, width=14, font=("Arial", 18), show="*")
        self.entry_contraseña.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")
        
        self.boton_ingresar = Button(self.frame_inferior, text="Ingresar", width=16, font=("Arial", 12), command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=15)
        
        self.boton_crear_usuario = Button(self.frame_inferior, text="Crear Usuario", width=16, font=("Arial", 12), command=self.crear_usuario)
        self.boton_crear_usuario.grid(row=3, column=0, columnspan=2, pady=15)
        
        mainloop()
    #Metodo que recibe los valores ingresados y manda a crear el usuario
    def crear_usuario(self):
        cNombre = self.entry_usuario.get()
        cContraseña = self.entry_contraseña.get()
        mensaje = self.db.crear_usuario(cNombre, cContraseña)
        messagebox.showinfo("Resultado", mensaje)
    #Metodo que recibe los datos para verificar si el usuario esta en la base de datos
    def entrar(self):  
        cNombre = self.entry_usuario.get()
        cContraseña = self.entry_contraseña.get()
        if self.db.verificar_usuario(cNombre, cContraseña):
            messagebox.showinfo("Acceso correcto", "Bienvenido")
            self.ventana.destroy()
            root = Tk()
            app = MenuPrincipal(root)
            root.mainloop()
        else:
            self.intentos -= 1
            if self.intentos > 0:
                messagebox.showerror("Error", f"Usuario o Contraseña incorrectos. Intentos restantes: {self.intentos}.")
            else:
                messagebox.showerror("Error", "Has agotado tus intentos. Cerrando programa.")
                self.ventana.destroy()
                self.db.cerrar_conexion()

Login()
