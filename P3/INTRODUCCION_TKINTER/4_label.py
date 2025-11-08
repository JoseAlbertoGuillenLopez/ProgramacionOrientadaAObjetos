import tkinter as tk

ventana=tk.Tk()

ventana.title("LABEL")
ventana.geometry("800x600")

etiqueta1=tk.Label(ventana,text="Nombre de la persona").pack()


marco1=tk.Frame(ventana,background="red",height=100,width=200)
marco1.pack_propagate(False)#para que se metan dentro
marco1.pack()


etiqueta2=tk.Label(marco1,text="Soy otra etiqueta",background="teal").pack(pady=10)




ventana.mainloop()