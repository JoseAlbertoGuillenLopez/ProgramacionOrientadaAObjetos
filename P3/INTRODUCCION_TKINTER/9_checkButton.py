from tkinter import *

def accion():
    #get toma valores de los values pero tiene que ser con variables
    if opcion.get()==1:
        lbltx.config(text="Notificaciones activadas")
    else:
        lbltx.config(text="Notificaciones desactivadas")

ventana=Tk()

ventana.title("CheckButton")
ventana.geometry("500x500")


#crea variable para poder usar de otra forma el widget
opcion=IntVar()
chkbtn=Checkbutton(ventana,text="¿Deseas recibir notificaciones?",variable=opcion,onvalue=1,offvalue=0)
chkbtn.pack(pady=10)

btnconf=Button(ventana,text="Confirmar",command=accion)
btnconf.pack()

lbltx=Label(ventana,text="")
lbltx.pack()

ventana.mainloop()