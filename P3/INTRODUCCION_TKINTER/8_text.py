from tkinter import *

def mostrar():
    mostrarContenido=txtarea.get("1.0",END).strip()
    lblocu.config(text=f"mensaje: {mostrarContenido}")
    #no puedo usar get por saltos de linea
    #get con 0 y con "1.0"

ventana=Tk()

ventana.geometry("800x600")
ventana.title("Text")

lbl_tit=Label(ventana,text="Escriba su comentario:")
lbl_tit.pack()
txtarea=Text(ventana,width=30,height=10)
txtarea.pack()
btnmos=Button(ventana,text="Mostrar comentario",command=mostrar)
btnmos.pack()

lblocu=Label(ventana,text="")
lblocu.pack()




ventana.mainloop()