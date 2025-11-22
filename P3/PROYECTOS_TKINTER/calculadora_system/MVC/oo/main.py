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



#bd esta en enteross

#1
class APP:
    def __init__(self,ventana):
        view=interfaz.vista(ventana)

#2  
    '''@staticmethod
    def main(ventana):
        view=interfaz.vista.main(ventana)'''
        

if __name__ == "__main__":
    ventana=Tk()
    app=APP(ventana)
    ventana.mainloop() 
    

'''if __name__ == "__main__":
    ventana=Tk()
    APP.main(ventana)
    ventana.mainloop()'''