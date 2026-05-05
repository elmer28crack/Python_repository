from  tkinter import *

ventana = Tk() #instancea la instancia de una ventana

ventana.geometry("800x500") # tamaño de la ventana (Ancho x alto)
ventana.title("Memo xd") # cambiar el titulo
ventana.config(background="") # cambiar el color al fondo papasito

texto = Label(ventana, text="Que lindo", font=("Arial",40))
texto.pack() #Mete el label por defecto papi
texto.place(x=0,y=0) #

ventana.mainloop() #Pone la ventana creada en la pantalla papi xd xd xd 