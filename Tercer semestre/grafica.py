import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 

ventana = tk.Tk()
ventana.title("Gestión del inventario UNIMINUTO")
ventana.geometry("800x600")

tabControl = ttk.Notebook(ventana)
pestaña_crear = ttk.Frame(tabControl)
pestaña_actualizar = ttk.Frame(tabControl)
pestaña_consultar = ttk.Frame(tabControl)
pestaña_eliminar = ttk.Frame(tabControl)

tabControl.add(pestaña_crear, text="Crear")
tabControl.add(pestaña_actualizar, text="Actualizar")
tabControl.add(pestaña_consultar, text="Consultar")
tabControl.add(pestaña_eliminar, text="Eliminar")

tabControl.pack(expand=1, fill="both")

# Etiqueta para el nombre del lugar
etiqnombre = ttk.Label(pestaña_crear, text="ID del lugar:")
etiqnombre.pack()

# Entrada para el nombre del lugar
entrada_nombre = ttk.Entry(pestaña_crear)
entrada_nombre.pack()

# Etiqueta para el tipo de lugar
etiqtipo = ttk.Label(pestaña_crear, text="Tipo de lugar:")
etiqtipo.pack()

# Combo box para el tipo de lugar
combo_tipo = ttk.Combobox(pestaña_crear, values=["Aula de clases", "Laboratorio", "Sala de sistemas"])
combo_tipo.pack()

# Etiqueta para la capacidad del lugar
etiqcapacidad = ttk.Label(pestaña_crear, text="Capacidad del lugar:")
etiqcapacidad.pack()

# Entrada para la capacidad del lugar
entrada_capacidad = ttk.Entry(pestaña_actualizar)
entrada_capacidad.pack()

# Entrada para el nombre del lugar
entrada_nombre = ttk.Entry(pestaña_actualizar)
entrada_nombre.pack()

# Etiqueta para el tipo de lugar
etiqtipo = ttk.Label(pestaña_actualizar, text="Tipo de lugar:")
etiqtipo.pack()

# Combo box para el tipo de lugar
combo_tipo = ttk.Combobox(pestaña_actualizar, values=["Aula de clases", "Laboratorio", "Sala de sistemas"])
combo_tipo.pack()

# Etiqueta para la capacidad del lugar
etiqcapacidad = ttk.Label(pestaña_actualizar, text="Capacidad del lugar:")
etiqcapacidad.pack()

# Entrada para la capacidad del lugar
entrada_capacidad = ttk.Entry(pestaña_actualizar)
entrada_capacidad.pack()

def crear_lugar():
    # Obtener el nombre del lugar
    nombre = entrada_nombre.get()

    # Obtener el tipo de lugar
    tipo = combo_tipo.get()

    # Obtener la capacidad del lugar
    capacidad = int(entrada_capacidad.get())

    # Crear el lugar
    # ...

    # Mostrar un mensaje de confirmación
    messagebox.showinfo("Información", "Lugar creado exitosamente.")

def Salir ():       #Funcion para botón salir
    cSalir = messagebox.askquestion('Salir', '¿Deseas salir del programa?')
    if cSalir=='yes':
        ventana.destroy()

# Botón para crear el lugar
btncrear = ttk.Button(pestaña_crear, text="Crear", command=crear_lugar)
btnSalir = ttk.Button(pestaña_crear,text='Salir',command=Salir)
btncrear.pack()

ventana.mainloop()