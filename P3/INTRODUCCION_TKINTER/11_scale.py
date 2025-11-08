from tkinter import *

def mostrar():
    lblmos.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

ventana=Tk()

ventana.title("Scale")
ventana.geometry("500x500")

valor=IntVar()

scl=Scale(ventana,from_=0, to=100, orient=HORIZONTAL, variable=valor,length=200)
scl.pack()

btnmos=Button(ventana,text="Mostrar valor",command=mostrar)
btnmos.pack(pady=10)

lblmos=Label(ventana,text="")
lblmos.pack()

ventana.mainloop()