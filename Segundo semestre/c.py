import tkinter as tk
def mostrar_informacion():
  if checkbutton.get() == 0:
    informacion = "No seleccionado"
  else:
    informacion = "Seleccionado"
  label.config(text=informacion)
root = tk.Tk()
checkbutton = tk.Checkbutton(root, text="¿Está seleccionado?")
checkbutton.pack()
label = tk.Label(root, text="")
label.pack()
boton = tk.Button(root, text="Mostrar información", command=mostrar_informacion)
boton.pack()
root.mainloop()
