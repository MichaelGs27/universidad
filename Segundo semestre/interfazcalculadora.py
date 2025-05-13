#Importamos "tkinter" para crear la ventana, "messagebox" para mensajes por ventana y "math" para operaciones matemáticas.
from tkinter import *
from tkinter import messagebox
import math
Ventana = Tk()  #Se crea el objeto
Ventana.title("Calculadora ")     #Titulo de la ventana 
Ventana.resizable(1,1)
Ventana.geometry('650x650') #Cambia tamaño de la pantalla 
#Etiquetas
EtiqX = Label(Ventana , text = 'X', )
EtiqX.config(
    fg = 'black' ,
    font = ('Arial', 20),  
)
EtiqY = Label(Ventana , text = 'Y')
EtiqY.config(
    fg = 'black',
    font = ('Arial',20),
)
EtiqResultado = Label(Ventana , text = 'Resultado')
EtiqResultado.config(
    fg = 'black',
    font = ('Arial',20),
)
#Variables para que aparezca en 0 la calculadora
nNum1 = IntVar ()
nNum2 = IntVar ()
Resultado =  IntVar ()
#Funciones
def Suma ():        #Función de la suma
    try:
        Resultado.set(nNum1.get() + nNum2.get())
        messagebox.showinfo('Resultado',f'El resultado de la suma es: {(nNum1.get() + nNum2.get())}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def Resta ():       #Función de la resta
    try:
        Resultado.set(nNum1.get() - nNum2.get())
        messagebox.showinfo('Resultado',f'El resultado de la resta es: {(nNum1.get() - nNum2.get())}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def Multiplicacion ():      #Función de la multiplicación
    try:
        Resultado.set(nNum1.get() * nNum2.get())
        messagebox.showinfo('Resultado',f'El resultado de la Multiplicación es: {(nNum1.get() * nNum2.get())}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def Division ():    #Función de la división
    try:
        if nNum1.get()!=0:  #Número diferente a 0
            Resultado.set(nNum1.get() / nNum2.get())
            messagebox.showinfo('Resultado',f'El resultado de la División es: {(nNum1.get() / nNum2.get())}')
        else:
             messagebox.showerror('Error','No se puede dividir por 0.')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def RaizX ():    #Función de la Raiz de X
    try:
        if nNum1.get()<=0:
            messagebox.showerror('Error','Ingrese un número positivo.')
        else:
            Resultado.set(math.sqrt(nNum1.get()))
            messagebox.showinfo('Resultado',f'El resultado de la raiz de X es: {(math.sqrt(nNum1.get()))}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def RaizY ():    #Función de la Raiz de Y
    try:
        if nNum1.get()<=0:
            messagebox.showerror('Error','Ingrese un número positivo.')
        else:
            Resultado.set(math.sqrt(nNum2.get()))
            messagebox.showinfo('Resultado',f'El resultado de la raiz de X es: {(math.sqrt(nNum2.get()))}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def XalaY ():    #Función de X a la Y
    try:
            Resultado.set(pow(nNum1.get(),nNum2.get()))
            messagebox.showinfo('Resultado',f'El resultado de X a la Y es: {(pow(nNum1.get(),nNum2.get()))}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def YalaX ():    #Función de Y a la X
    try:
            Resultado.set(pow(nNum2.get(),nNum1.get()))
            messagebox.showinfo('Resultado',f'El resultado de Y a la X es: {(pow(nNum2.get(),nNum1.get()))}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def XmodY ():    #Función de X mod Y
    try:
            Resultado.set(nNum1.get()%nNum2.get())
            messagebox.showinfo('Resultado',f'El resultado de X mod Y es: {(nNum1.get()%nNum2.get())}')
    except:
        return messagebox.showerror('Error', 'No digite letras. Solo se puede digitar números.')
def Limpiar ():     #Funcion para limpiar las  cajas de texto
    nNum1.set (0)
    nNum2.set (0)
    Resultado.set (0)
    messagebox.showinfo('Limpiar','Los valores se modificaron a 0.')
def Salir ():       #Funcion para botón salir
    cSalir = messagebox.askquestion('Salir', '¿Deseas salir del programa?')
    if cSalir=='yes':
        Ventana.destroy()
#Cajas de texto
txtX = Entry(Ventana,fg = 'black',font = 'CourierNew', textvariable= nNum1).grid(row=1,column= 0)
txtX = Entry(Ventana,fg = 'black',font = 'CourierNew', textvariable= nNum2).grid(row=1,column= 1)
txtResultado = Entry(Ventana,fg= 'black',font= 'CourierNew', state= 'disabled', textvariable= Resultado).grid(row=1,column= 2)
# Botones 
btnSuma = Button(Ventana,text= '+',width=8,height=2,fg='black',command= Suma).grid(row=3,column=0)
btnResta = Button(Ventana,text= '-',width=8,height=2,fg='black',command= Resta).grid(row=3,column=1)
btnMultiplicacion = Button(Ventana,text= '*',width=8,height=2,fg='black',command=Multiplicacion).grid(row=3,column=2)
btnDivision = Button(Ventana,text= '/',width=8,height=2,fg='black', command= Division).grid(row=4,column=0)
btnRaizX = Button(Ventana,text= 'Raiz X',width=8,height=2,fg='black',command= RaizX).grid(row=4,column=1)
btnRaizY = Button(Ventana,text= 'Raiz Y',width=8,height=2,fg='black',command= RaizY).grid(row=4,column=2)
btnXalaY = Button(Ventana,text= 'X a la Y',width=8,height=2,fg='black',command= XalaY).grid(row=5,column=0)
btnYalaX = Button(Ventana,text= 'Y a la X',width=8,height=2,fg='black',command=YalaX).grid(row=5,column=1)
btnXmodY = Button(Ventana,text= 'X mod Y',width=8,height=2,fg='black',command=XmodY).grid(row=5,column=2)
btnLimpiar = Button(Ventana,text='Limpiar',width=8,height=2,fg='black', command=Limpiar).grid(row=6,column=1)
btnSalir = Button(Ventana,text='Salir',width=8,height=2,fg='black', command=Salir).grid(row=6,column=2)

#Ubicación de las etiquetas 
EtiqX.grid(row=0,column=0)
EtiqY.grid(row=0,column=1)
EtiqResultado.grid(row=0,column=2)

Ventana.mainloop() #Se coloca el mainloop para que el codigo se pueda ejecutar