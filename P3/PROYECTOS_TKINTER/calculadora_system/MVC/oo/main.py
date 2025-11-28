'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en alerta
4.- Programado con formato OO
5.- Considerar MVC
'''

from view import interfaz
from tkinter import *

class APP:
    def __init__(self,ventana):
        view=interfaz.vista(ventana)


if __name__ == "__main__":
    ventana=Tk()
    app=APP(ventana)
    ventana.mainloop()  
    
