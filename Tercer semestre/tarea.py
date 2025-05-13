from tkinter import *
from tkinter import messagebox
from datetime import datetime
Ventana = Tk()  #Se crea el objeto 
Ventana.title("UNIMINUTO ")
Ventana.resizable(1,1)
Ventana.geometry('450x250') #Cambia tamaño de la pantalla 
#Menu principal 
MenuPrincipal = Menu(Ventana)
#Etiquetas
EtiqInvUniminuto = Label(Ventana , text = 'Inventario Uniminuto', )
EtiqInvUniminuto.config(fg = 'black' ,font = ('Arial', 20), )
EtiqID = Label(Ventana , text = 'ID Sala:', )
EtiqID.config(fg = 'black' ,font = ('Arial', 20),)
EtiTipoLugar = Label(Ventana , text = 'Tipo de lugar:')
EtiTipoLugar.config(fg = 'black',font = ('Arial',20),)
EtiqCapacidadLugar = Label(Ventana , text = 'Capacidad del lugar:')
EtiqCapacidadLugar.config(fg = 'black',font = ('Arial',20),)
#Variables para leer la info que ingresa el usuario
txt1 = StringVar ()
txt2 =  StringVar ()
cLugar = StringVar()
Lugares = []
def CrearLugar():
    # Obtener la información del lugar
    
    id = txt1.get()
    tipo = cLugar.get()
    capacidad = txt2.get()

    # Agregar el lugar a la lista
    Lugares.append((id, tipo, capacidad))

    # Mostrar un mensaje de confirmación
    messagebox.showinfo("Información", "Lugar creado exitosamente")

def ActualizarLugar():
    # Obtener la información del lugar
    id = txt1.get()
    tipo = cLugar.get()
    capacidad = txt2.get()

    # Buscar el lugar en la lista
    indice = buscar_lugar(id)

    # Si el lugar no existe, mostrar un mensaje de error
    if indice is None:
        messagebox.showerror("Error", "El lugar no existe.")
        return

    # Actualizar la información del lugar en la lista
    Lugares[indice] = (id, tipo, capacidad)

    # Mostrar un mensaje de confirmación
    messagebox.showinfo("Información", "Lugar actualizado exitosamente")

def buscar_lugar(id):
    for indice, lugar in enumerate(Lugares):
        if lugar[0] == id:
            return indice
    return None

def EliminarLugar():
    # Obtener el ID del lugar
    id = txt1.get()

    # Buscar el lugar en la lista
    indice = buscar_lugar(id)

    # Si el lugar no existe, mostrar un mensaje de error
    if indice is None:
        messagebox.showerror("Error", "El lugar no existe.")
        return

    # Eliminar el lugar de la lista
    del Lugares[indice]

    # Mostrar un mensaje de confirmación
    messagebox.showinfo("Información", "Lugar eliminado exitosamente")


def Salir ():       #Funcion para botón salir
    cSalir = messagebox.askquestion('Salir', '¿Deseas salir del programa?')
    if cSalir=='yes':
        Ventana.destroy()

#Cajas de texto
txtID = Entry(Ventana,fg = 'black',font = 'CourierNew',textvariable= txt1).grid(row=1,column= 1)
txtCapacidad = Entry(Ventana,fg= 'black',font= 'CourierNew',textvariable= txt2).grid(row=1,column= 5)
#list
ListVi = OptionMenu(Ventana,cLugar, "Aula de clases","Laboratorio","Sala de sistemas").grid(row=1,column= 3)
#Botones
btnCrear = Button(Ventana,text= 'Crear',width=15,height=2,fg='black',command=CrearLugar).grid(row=8,column=0)
btnEliminar = Button(Ventana,text='Eliminar',width=15,height=2,fg='black', command=EliminarLugar).grid(row=8,column=1)
btnActualizar = Button(Ventana,text='Actualizar',width=15,height=2,fg='black', command=ActualizarLugar).grid(row=8,column=2)
btnConsultar = Button(Ventana,text='Consultar',width=15,height=2,fg='black', command = buscar_lugar).grid(row=8,column=3)
btnSalir = Button(Ventana,text='Salir',width=15,height=2,fg='black', command=Salir).grid(row=8,column=4)


EtiqInvUniminuto.grid(row=0,column=0)
EtiqID.grid(row=1,column=0)
EtiTipoLugar.grid(row=1,column=2)
EtiqCapacidadLugar.grid(row=1,column=4)



Ventana.mainloop() #Se coloca el mainloop para que el codigo se pueda ejecutar