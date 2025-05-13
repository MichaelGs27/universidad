from tkinter import *
from tkinter import messagebox
Ventana = Tk()  #Se crea el objeto
Ventana.title("Calculadora Area y Perimetro")     #Titulo de la ventana 
Ventana.resizable(1,1)
Ventana.geometry('650x650') #Cambia tamaño de la pantalla 
#Etiquetas
EtiqAltura = Label(Ventana , text = 'Digite Altura', )
EtiqAltura.config(
    fg = 'white' ,
    font = ('Arial', 20),  
    bg = ('black')
)
EtiqBase = Label(Ventana , text ='Digite Base')
EtiqBase.config(
    fg = 'white',
    font = ('Arial',20),
    bg = ('black')
)
#EtiqResultado = Label(Ventana , text ='Resultado')
#EtiqResultado.config(
#    fg = 'white',
#    font = ('Arial',20),
#    bg = 'black'
#)
#Variables 
nNum1 = IntVar ()
nNum2 = IntVar ()
Resultado =  IntVar ()
#Funciones
def Area ():
    try:
        Resultado.set(nNum1.get() * nNum2.get())
        messagebox.showinfo('Resultado',f'El resultado del area es {(nNum1.get() * nNum2.get())}')
    except:
        return messagebox.showinfo('Información', 'No digite letras. Solo se puede digitar números.')

def Perimetro ():
    try:
        Resultado.set((nNum1.get()*2) + (nNum2.get()*2))
        messagebox.showinfo('Resultado',f'El resultado del perimetro es {((nNum1.get()*2) + (nNum2.get()*2))}')
    except:
        return messagebox.showinfo('Informacion', 'No digite letras. Solo se puede digitar números')

def Limpiar ():
    nNum1.set (0)
    nNum2.set (0)
    Resultado.set (0)
    messagebox.showinfo('Limpiar','Los valores se modificaron a 0.')
def Salir ():
    cSalir = messagebox.askquestion('Salir', '¿Deseas salir del programa?')
    if cSalir=='yes':
        Ventana.destroy()
#Cajas de texto y Botones 
txtAltura = Entry(Ventana,fg = 'black',font = 'CourierNew', textvariable= nNum1).grid(row=0,column= 1)
txtBase = Entry(Ventana,fg= 'black',font= 'CourierNew',textvariable= nNum2).grid(row=1,column= 1)
#txtResultado = Entry(Ventana,fg= 'black',font= 'CourierNew', state= 'disabled', textvariable= Resultado).grid(row=2,column= 1)
btnCalArea = Button(Ventana,text= 'Calcular Area',width=14,height=1,fg='black',command=Area).grid(row=4,column=1)
btnCalPeri = Button(Ventana,text='Calcular Perimetro',width=14,height=1,fg='black', command=Perimetro).grid(row=4,column=2)
btnLimpiar = Button(Ventana,text='Limpiar',width=10,height=1,fg='black', command=Limpiar).grid(row=5,column=1)
btnSalir = Button(Ventana,text='Salir',width=10,height=1,fg='black', command= Salir).grid(row=5,column=2)





EtiqAltura.grid(row=0,column=0)
EtiqBase.grid(row=1,column=0)
#EtiqResultado.grid(row=2,column=0)
Ventana.mainloop() #Se coloca el mainloop para que el codigo se pueda ejecutar 