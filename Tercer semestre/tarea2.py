#Interfaz grafica Inventario Uniminuto
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

M1 = []
#Se crea la clase 
class Usuario:
    def __init__(self, root):
        # Configuración inicial de la interfaz gráfica
        self.Ventana = root
        self.Ventana.title("Inventario Uniminuto")
        self.Ventana.geometry("850x600")
        self.Ventana.config(bg="teal")

        # Crear dos marcos (frames) para organizar la interfaz
        frame1 = LabelFrame(self.Ventana, text="Datos a ingresar", font=("calibri", 14))
        frame2 = LabelFrame(self.Ventana, text="Información ", font=("calibri", 14))

        # Empaquetar los marcos en la ventana principal
        frame1.pack(fill="both", expand="yes", padx=20, pady=15)
        frame2.pack(fill="both", expand="yes", padx=20, pady=15)

        # Variables de control para los datos ingresados por el usuario
        ID = IntVar()
        Nombre = StringVar()
        TipoLugar = StringVar()
        Capacidad = StringVar()

        # Método para limpiar los campos de entrada
        def Limpiar():
            self.entID.delete(0, END)
            self.entNombre.delete(0, END)
            self.entTipoLugar.delete(0, END)
            self.entCapacidad.delete(0, END)
            messagebox.showinfo('Limpiar', 'Se limpiaron los espacios.')

        # Método para agregar un nuevo lugar
        def Agregar():
            AUX = [ID.get(), Nombre.get(), TipoLugar.get(), Capacidad.get()]
            if AUX == "":
                messagebox.showerror('Error', "Digite valores.")
            else:
                # Verificar si la información ya existe en M1
                if not any(item[:3] == AUX[:3] for item in M1):
                    M1.append(AUX)
                    print(M1)
                    # Limpiar el Treeview antes de actualizarlo
                    for i in self.trv.get_children():
                        self.trv.delete(i)

                    # Actualizar el Treeview con los datos de M1
                    for row in M1:
                        self.trv.insert("", "end", values=row)
                else:
                    messagebox.showwarning('Advertencia', 'La información ya existe. No se puede agregar.')
                    

        # Método para eliminar un lugar por su ID
        def Eliminar():
            IDeliminar = ID.get()
            
            if IDeliminar == "":
                messagebox.showerror('Error', "Digite el ID que deseas eliminar.")
            else:
                # Buscar el índice del elemento en M1 que tiene el ID proporcionado
                EliminarFra = next((index for index, item in enumerate(M1) if item[0] == IDeliminar), None)

                if EliminarFra is not None:
                    # Eliminar el elemento de M1
                    M1.pop(EliminarFra)

                    # Limpiar el Treeview antes de actualizarlo
                    for i in self.trv.get_children():
                        self.trv.delete(i)

                    # Actualizar el Treeview con los datos de M1
                    for row in M1:
                        self.trv.insert("", "end", values=row)

                    messagebox.showinfo('Información', 'Se ha eliminado correctamente.')
                else:
                    messagebox.showwarning('Advertencia', f'No se encontró un elemento con el ID {IDeliminar}.')

        # Método para consultar la información de un lugar por su ID
        def Consultar():
            IdBuscar = ID.get()
            encontrado = False
            #Busca en la lista el ID proporcionado para mostrar la información
            for fila in M1:
                if fila[0] == IdBuscar:
                    messagebox.showinfo('Información', f'ID: {fila[0]}\nNombre: {fila[1]}\nTipo: {fila[2]}\nCapacidad: {fila[3]}')
                    print(M1)
                    encontrado = True
                    break    
            if not encontrado:
                messagebox.showwarning('Advertencia', f'No se encontró un elemento con el ID {IdBuscar}.')
                print(IdBuscar)

        # Método para actualizar la información de un lugar por su ID
        def Actualizar():
            IdActualizar = ID.get()
            encontrado = False
            #Busca en la lista el ID prorcionado para poder actualizar 
            for i, fila in enumerate(M1):
                if fila[0] == IdActualizar:
                    encontrado = True

                    if self.entNombre.get() and self.entTipoLugar.get() and self.entCapacidad.get():
                        # Actualizar la información en el Treeview
                        M1[i][1] = self.entNombre.get()
                        M1[i][2] = self.entTipoLugar.get()
                        M1[i][3] = self.entCapacidad.get()

                        # Limpiar el Treeview antes de actualizarlo
                        for item in self.trv.get_children():
                            self.trv.delete(item)

                        # Actualizar el Treeview con los datos de M1
                        for row in M1:
                            self.trv.insert("", "end", values=row)

                        messagebox.showinfo('Información', 'Se ha actualizado correctamente.')
                        print(M1)
                    else:
                        messagebox.showwarning('Advertencia', 'Ingrese nuevos valores para actualizar.')

                    break

            if not encontrado:
                messagebox.showwarning('Advertencia', f'No se encontró un elemento con el ID {IdActualizar}.')
                

        # Método para salir del programa
        def Salir():
            cSalir = messagebox.askquestion('Salir', '¿Deseas salir del programa?')
            if cSalir == 'yes':
                self.Ventana.destroy()

        # Crear etiquetas y campos de entrada en el frame1
        lbl1 = Label(frame1, text="ID", width=20)
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        self.entID = Entry(frame1, textvariable=ID)
        self.entID.grid(row=0, column=1, padx=5, pady=3)

        lbl2 = Label(frame1, text="Nombre del lugar", width=20)
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        self.entNombre = Entry(frame1, textvariable=Nombre)
        self.entNombre.grid(row=1, column=1, padx=5, pady=3)

        lbl3 = Label(frame1, text="Tipo del lugar", width=20)
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        self.entTipoLugar = Entry(frame1, textvariable=TipoLugar)
        self.entTipoLugar.grid(row=2, column=1, padx=5, pady=3)

        lbl4 = Label(frame1, text="Capacidad del lugar", width=20)
        lbl4.grid(row=3, column=0, padx=5, pady=3)
        self.entCapacidad = Entry(frame1, textvariable=Capacidad)
        self.entCapacidad.grid(row=3, column=1, padx=5, pady=3)

        # Crear botones en el frame1 con funciones asociadas
        btn1 = Button(frame1, text="Agregar", width=12, height=2, command=Agregar)
        btn1.grid(row=5, column=0, padx=10, pady=10)
        btn2 = Button(frame1, text="Eliminar", width=12, height=2, command=Eliminar)
        btn2.grid(row=5, column=1, padx=10, pady=10)
        btn3 = Button(frame1, text="Actualizar", width=12, height=2, command=Actualizar)
        btn3.grid(row=5, column=2, padx=10, pady=10)
        btn4 = Button(frame1, text="Consultar", width=12, height=2, command=Consultar)
        btn4.grid(row=5, column=3, padx=10, pady=10)
        btn5 = Button(frame1, text="Limpiar", width=12, height=2, command=Limpiar)
        btn5.grid(row=5, column=4, padx=10, pady=10)
        btn6 = Button(frame1, text="Salir", width=12, height=2, command=Salir)
        btn6.grid(row=5, column=5, padx=10, pady=10)

        # Crear un Treeview en el frame2 para mostrar la información
        self.trv = ttk.Treeview(frame2, columns=(1, 2, 3, 4), show="headings", height="15")
        self.trv.pack()

        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="Nombre del lugar")
        self.trv.heading(3, text="Tipo del lugar")
        self.trv.heading(4, text="Capacidad del lugar")

# Inicializar la aplicación si se ejecuta como script principal
if __name__ == "__main__":
    root = Tk()
    Usuario = Usuario(root)
    root.mainloop()
