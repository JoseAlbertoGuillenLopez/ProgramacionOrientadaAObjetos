from tkinter import *

def mensaje(tipo):
    lbltx.config(text=f"{tipo}")


ventana=Tk()

ventana.title("Menu")
ventana.geometry("500x500")

menuBar=Menu(ventana)
ventana.config(menu=menuBar)
archivoMenu=Menu(menuBar,tearoff=1) #0 o 1 tearoff
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo Archivo"))
#funcion con parentesis si tengo parametros y con lambda
archivoMenu.add_command(label="Guardar Archivo",command=lambda: mensaje("Guardar Archivo")) 
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=ventana.quit) #destruye todo el programa


archivoEdicion=Menu(menuBar,tearoff=1) #0 o 1 tearoff
menuBar.add_cascade(label="Edicion", menu=archivoEdicion)
archivoEdicion.add_command(label="Copiar",command=lambda: mensaje("Copiar"))
#funcion con parentesis si tengo parametros y con lambda
archivoEdicion.add_command(label="Recortar",command=lambda: mensaje("Recortar")) 
archivoEdicion.add_separator()
archivoEdicion.add_command(label="Salir",command=ventana.destroy) #destruye la ventana activa u objetos separados
#si pongo el comando aqui es sin parentesis, si es arriba en funcion si va con parentesis quit()

lbltx=Label(ventana,text="")
lbltx.pack()

ventana.mainloop()