from tkinter import *
from tkinter import messagebox
from datetime import datetime
Ventana = Tk()  #Se crea el objeto 
Ventana.title("Información Personal ")
Ventana.resizable(1,1)
Ventana.geometry('450x250') #Cambia tamaño de la pantalla 
#Menu principal 
MenuPrincipal = Menu(Ventana)
#Archivo
MenArchivo = Menu(MenuPrincipal)
MenArchivo.add_command(label="Abrir Archivo")
MenArchivo.add_command(label="Abrir Carpeta")
MenArchivo.add_command(label="Importar")
MenArchivo.add_command(label="Exportar")
MenArchivo.add_command(label="Salir")
MenuPrincipal.add_cascade(label="Archivo",menu=MenArchivo)
Ventana.config(menu= MenuPrincipal)
#Editar
MenEditar = Menu(MenuPrincipal)
MenEditar = Menu(Ventana)
MenEditar.add_command(label="Cortar")
MenEditar.add_command(label="Pegar")
MenuPrincipal.add_cascade(label="Editar",menu=MenEditar)
Ventana.config(menu= MenuPrincipal)
#Formato
MenFormato = Menu(MenuPrincipal)
MenFormato = Menu(Ventana)
MenFormato.add_command(label="Formato APA")
MenuPrincipal.add_cascade(label="Formato",menu=MenFormato)
Ventana.config(menu= MenuPrincipal)
#Ayuda
MenAyuda = Menu(MenuPrincipal)
MenAyuda = Menu(Ventana)
MenAyuda.add_command(label="Help meeeee")
MenuPrincipal.add_cascade(label="Ayuda",menu=MenAyuda)
Ventana.config(menu= MenuPrincipal)
#Etiquetas
EtiqInfomacionPers = Label(Ventana , text = 'Información Personal', )
EtiqInfomacionPers.config(fg = 'black' ,font = ('Arial', 20), )
EtiqNombre = Label(Ventana , text = 'Nombre', )
EtiqNombre.config(fg = 'black' ,font = ('Arial', 20),)
EtiqApellido = Label(Ventana , text = 'Apellido')
EtiqApellido.config(fg = 'black',font = ('Arial',20),)
EtiqFechaNac = Label(Ventana , text = 'Fecha Nacimiento(DD/MM/AAAA)')
EtiqFechaNac.config(fg = 'black',font = ('Arial',20),)
EtiqGenero = Label(Ventana , text = 'Genero')
EtiqGenero.config(fg = 'black',font = ('Arial',20),)
EtiqFemenino = Label(Ventana , text = 'Femenino')
EtiqFemenino.config(fg = 'black',font = ('Arial',20),)
EtiqGustos = Label(Ventana , text = 'Gustos')
EtiqGustos.config(fg = 'black',font = ('Arial',20),)
EtiqComer = Label(Ventana , text = 'Comer')
EtiqComer.config(fg = 'black',font = ('Arial',20),)
EtiqCine = Label(Ventana , text = 'Cine')
EtiqCine.config(fg = 'black',font = ('Arial',20),)
EtiqVerTV = Label(Ventana , text = 'Ver TV')
EtiqVerTV.config(fg = 'black',font = ('Arial',20),)
EtiqCaminar = Label(Ventana , text = 'Caminar')
EtiqCaminar.config(fg = 'black',font = ('Arial',20),)
EtiqDeporte = Label(Ventana , text = 'Deporte')
EtiqDeporte.config(fg = 'black',font = ('Arial',20),)
EtiqSocial = Label(Ventana , text = 'Social')
EtiqSocial.config(fg = 'black',font = ('Arial',20),)
EtiqLugarVivi = Label(Ventana , text = 'Lugar Vivienda')
EtiqLugarVivi.config(fg = 'black',font = ('Arial',20),)
#Variables para leer la info que ingresa el usuario
txt1 = StringVar ()
txt2 = StringVar ()
txt3 =  StringVar ()
cGenero = StringVar()
cGenero.set(None)
cComer = IntVar()
cCine =IntVar()
cVerTV = IntVar()
cCaminar = IntVar()
cDeporte= IntVar()
cSocial = IntVar()
cVivienda = StringVar()
#Funciones
def EvaluarCo ():
    if cComer.get() ==0:
        Comer = (len(" "))
    else:
        Comer = ("Comer")
        return Comer
def EvaluarCi ():
    if cCine.get() ==0:
        Cine = (len(" "))
    else:
        Cine = ("Cine")
        return Cine
def EvaluarVerTV ():
    if cVerTV.get() ==0:
        VerTv = (len(" "))
    else:
        VerTv = ("VerTv")
        return VerTv
def EvaluarCa ():
    if cCaminar.get() ==0:
        Caminar = (len(" "))
    else:
        Caminar = ("Caminar")
        return Caminar
def EvaluarDe ():
    if cDeporte.get() ==0:
        Deporte = (len(" "))
    else:
        Deporte = ("Deporte")
        return Deporte
def EvaluarSo ():
    if cSocial.get() ==0:
        Social = (len(" "))
    else:
        Social = ("Social")
        return Social

def Mostrarinfo ():
    if txt1.get() =="":
            messagebox.showerror("Error","Por favor ingrese el nombre.")
    elif txt2.get()=="":
            messagebox.showerror("Error","Por favor ingrese el apellido.")
    elif txt3.get()=="":
        messagebox.showerror("Error","Por favor ingrese la edad. ")
    elif cGenero.get()==None:
        messagebox.showerror("Error","Por favor ingrese el genero. ")
    fechanac = datetime.strptime(txt3.get(),'%d/%m/%Y')
    fechaact = datetime.now()
    edad = fechaact.year - fechanac.year 
    messagebox.showinfo("Info", f"""Señor usuario {txt1.get()} {txt2.get()} de edad: {edad}
De genero: {cGenero.get()}
Su gustos son los siguientes: {EvaluarCo()}, {EvaluarCi()}, {EvaluarVerTV()}, {EvaluarCa()}, {EvaluarDe()}, {EvaluarSo()}
Su lugar de vivienda es: {cVivienda.get()}""")
def Limpiar ():     #Funcion para limpiar las  cajas de texto
    txt1.set (" ")
    txt2.set (" ")
    txt3.set (" ")
    cGenero.set(0)
    cComer.set(0)
    cCine.set(0)
    cVerTV.set(0)
    cCaminar.set(0)
    cDeporte.set(0)
    cSocial.set(0)
    cVivienda.set("")
    messagebox.showinfo('Limpiar','Se limpiaron los espacios.')
def Salir ():       #Funcion para botón salir
    cSalir = messagebox.askquestion('Salir', '¿Deseas salir del programa?')
    if cSalir=='yes':
        Ventana.destroy()
#Cajas de texto
txtNombre = Entry(Ventana,fg = 'black',font = 'CourierNew',textvariable= txt1).grid(row=1,column= 1)
txtApellido = Entry(Ventana,fg = 'black',font = 'CourierNew',textvariable= txt2).grid(row=1,column= 3)
txtFechaNac = Entry(Ventana,fg= 'black',font= 'CourierNew',textvariable= txt3).grid(row=1,column= 5)
#Radio button
RadMasculino = Radiobutton(Ventana,text="Masculino",fg = 'black',font = ('Arial',20),variable=cGenero, value="Masculino").grid(row=3,column= 0)
RadFemenino = Radiobutton(Ventana,text="Femenino",fg = 'black',font = ('Arial',20),variable=cGenero, value= "Femenino").grid(row=4,column= 0)
chekComer = Checkbutton(Ventana,text="Comer",fg = 'black',font = ('Arial',20),variable=cComer ,onvalue=1,offvalue=0,).grid(row=3,column= 2)
chekCine = Checkbutton(Ventana,text="Cine",fg = 'black',font = ('Arial',20),variable=cCine,onvalue=1,offvalue=0).grid(row=4,column= 2)
chekVerTV = Checkbutton(Ventana,text="Ver TV",fg = 'black',font = ('Arial',20),variable=cVerTV,onvalue=1,offvalue=0).grid(row=5,column= 2)
chekCaminar = Checkbutton(Ventana,text="Caminar",fg = 'black',font = ('Arial',20),variable=cCaminar,onvalue=1,offvalue=0).grid(row=3,column= 4)
chekDeporte = Checkbutton(Ventana,text="Deporte",fg = 'black',font = ('Arial',20),variable=cDeporte,onvalue=1,offvalue=0).grid(row=4,column= 4)
chekSocial = Checkbutton(Ventana,text="Social",fg = 'black',font = ('Arial',20),variable=cSocial,onvalue=1,offvalue=0).grid(row=5,column= 4)
ListVi = OptionMenu(Ventana,cVivienda, "Ibagué","Bogotá","Medellin","Cali","Bucaramanga","Barranquilla").grid(row=3,column= 5)
btnMostrarinfo = Button(Ventana,text= 'Mostrar Info',width=15,height=2,fg='black',command=Mostrarinfo).grid(row=8,column=0)
btnLimpiar = Button(Ventana,text='Limpiar',width=15,height=2,fg='black',command=Limpiar).grid(row=8,column=1)
btnSalir = Button(Ventana,text='Salir',width=15,height=2,fg='black',command=Salir).grid(row=8,column=2)
#Ubicación de las etiquetas 
EtiqInfomacionPers.grid(row=0,column=0)
EtiqNombre.grid(row=1,column=0)
EtiqApellido.grid(row=1,column=2)
EtiqFechaNac.grid(row=1,column=4)
EtiqGenero.grid(row=2,column=0)
EtiqGustos.grid(row=2,column=3)
EtiqLugarVivi.grid(row=2,column=5)
Ventana.mainloop() #Se coloca el mainloop para que el codigo se pueda ejecutar