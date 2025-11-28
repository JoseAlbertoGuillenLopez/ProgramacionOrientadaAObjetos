from tkinter import *
from tkinter import ttk
from controller import funciones
from model import coches,camiones,camionetas

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.geometry("1200x400")
        ventana.title("Gestion de Coches")
        self.menu_principal(ventana)

    def borrar_pantalla(self,ventana):
        for i in ventana.winfo_children():
            i.destroy()
