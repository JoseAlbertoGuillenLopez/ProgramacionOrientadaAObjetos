from tkinter import *

def mostrar():
    valor=lsbx.get(lsbx.curselection())
    lblmos.config(text=f"Seleccionaste: {valor} ")

ventana=Tk()

ventana.title("ListBox")
ventana.geometry("500x500")

#aqui no es necesaria la variable string, la creo arriba y uso cursorselection()

lsbx=Listbox(ventana,width=50,height=5,selectmode="single",)
lsbx.pack(pady=10)

opciones=["Azul","Rojo","Negro","Amarillo"]
for i in opciones:
    lsbx.insert(END,i)

btnmos=Button(ventana,text="Mostrar seleccion del usuario",command=mostrar)
btnmos.pack(pady=10)

lblmos=Label(ventana,text="")
lblmos.pack()


ventana.mainloop()