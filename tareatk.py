import tkinter as tk 
ventana = tk.Tk()
ventana.title('Ahora tenemos 4 botones!')
ventana.geometry('400x200')

boton1= tk.Button(ventana, text="Boton 1")
boton2= tk.Button(ventana, text="Boton 2")
boton3= tk.Button(ventana, text="Boton 3")
boton4= tk.Button(ventana, text="Boton 4")
boton5= tk.Button(ventana, text="Salir", command=ventana.destroy)

boton1.pack(side="top")
boton2.pack(side="left")
boton3.pack(side="right")
boton4.pack(side="bottom")
boton5.place(x=100, y=100)

ventana.mainloop()