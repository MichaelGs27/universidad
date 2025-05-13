from tkinter import Tk, messagebox, Label, Button, Entry, Frame
from tarea2 import Usuario  # Importamos la interfaz del inventario

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x300")
        self.ventana.title("Login")
        self.intentos = 3  # Contador de intentos
        
        fondo = "#88FFB4"
        self.ventana.configure(bg=fondo)
        
        Label(self.ventana, text="Usuario", font=("Arial", 14), bg=fondo).pack(pady=10)
        self.entry_usuario = Entry(self.ventana, font=("Arial", 14))
        self.entry_usuario.pack()
        
        Label(self.ventana, text="Contraseña", font=("Arial", 14), bg=fondo).pack(pady=10)
        self.entry_contraseña = Entry(self.ventana, font=("Arial", 14), show="*")
        self.entry_contraseña.pack()
        
        Button(self.ventana, text="Ingresar", font=("Arial", 12), command=self.entrar).pack(pady=20)
        
        self.ventana.mainloop()
    
    def entrar(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        
        if usuario == "admin" and contraseña == "1234":
            messagebox.showinfo("Acceso correcto", "Bienvenido")
            self.ventana.destroy()  # Cierra la ventana de login
            root = Tk()
            root.geometry("850x600")  # Ajusta el tamaño de la ventana del inventario
            Usuario(root)  # Abre la interfaz de inventario
            root.mainloop()
        else:
            self.intentos -= 1
            if self.intentos > 0:
                messagebox.showerror("Error", f"Credenciales incorrectas. Intentos restantes: {self.intentos}")
            else:
                messagebox.showerror("Error", "Demasiados intentos fallidos. El programa se cerrará.")
                self.ventana.destroy()

if __name__ == "__main__":
    Login()
