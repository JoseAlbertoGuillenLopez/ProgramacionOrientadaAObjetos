"Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones"
"en Python para"

import tkinter as tk
#from tkinter import *

ventana=tk.Tk()
ventana.title("Mi primer App grafica en Tkinter con Python")
ventana.geometry("800x600")
ventana.resizable(False,True)# with en false y height en false para que no se haga mas grande
#permite redimencionar la ventana 


ventana.mainloop() #metodo que perimite tener la ventana abierta e interactuar con ella


