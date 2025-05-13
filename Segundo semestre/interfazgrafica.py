from tkinter import *
Ventana = Tk()  #Se crea el objeto
Ventana.title("Mi primera Ventana")     #Titulo de la ventana 
Ventana.resizable(1,1)      #Tamaño (vertical - horizontal)
Ventana.geometry('240x240') #Cambia tamaño de la pantalla 
EtiqNombre = Label(Ventana , text = 'Nombre', )
EtiqNombre.config(
    fg = 'white' ,
    font = ('LucidaHandwriting', 20),  
    bg = 'black'
)
EtiqApellido = Label(Ventana , text ='Apellido')
EtiqApellido.config(
    fg = 'white',
    font = ('LucidaHandwriting',20),
    bg = ('black')
)
txtNombre = Text(Ventana,width=10,height=1,fg = 'pink',font = 'CourierNew').grid(row=1,column= 1)
txtApellido = Text(Ventana,width=10,height=1,fg='pink',font= 'CourierNew').grid(row=0,column= 1)
btnAceptar = Button(Ventana,text = 'Aceptar',width=6,height=2, fg= 'red').grid(row=4,column=2)
btnCancelar = Button(Ventana,text = 'Cancelar',width=6,height=2, fg= 'blue').grid(row=4,column=3)
btnSalir = Button(Ventana,text = 'Salir',width=6,height=2,fg= 'green').grid(row=4,column=4)




EtiqNombre.grid(row=1,column=0)
EtiqApellido.grid(row=0,column=0)
Ventana.mainloop() #Se coloca el mainloop para que el codigo se pueda ejecutar 