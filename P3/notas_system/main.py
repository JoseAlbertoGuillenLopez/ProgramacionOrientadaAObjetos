'''
1.- Implementar el MVC
2.- Paradigma POO
3.- App de escritorio

'''


from tkinter import *
from view import view1

class APP:
    def __init__(self,ventana):
        view=view1.View(ventana) 


if __name__=="__main__":
    ventana=Tk()
    app=APP(ventana)
    ventana.mainloop()   