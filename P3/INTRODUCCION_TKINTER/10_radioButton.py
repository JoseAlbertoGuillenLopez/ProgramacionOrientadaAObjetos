from tkinter import *

def accion():
    lblmos.config(text=f"Opcion seleccionada: {opcion.get()} ")
    #get importante para sacar el valor

ventana=Tk()

ventana.title("RadioButton")
ventana.geometry("500x500")

#para seleccionar maximo 3 0 4 opciones pero solo una, minimo 2 rbtn


#value es lo que guarda el boton, puedo poner cualquer texto o numero es como el onvalue y offvalue de la chbx
#variable es la clase para que esten apagados o prendidos, tambien es para hacer el objeto una variable y en este caso 3 obj es una variable que toma el valor del seleccionado

opcion=StringVar()

opcion1=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="opcion 1")
opcion1.pack()


opcion2=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="opcion 2")
opcion2.pack()


opcion3=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="opcion 3")
opcion3.pack()


btnmost=Button(ventana,text="Mostrar selección",command=accion)
btnmost.pack()

lblmos=Label(ventana,text="")
lblmos.pack()

ventana.mainloop()