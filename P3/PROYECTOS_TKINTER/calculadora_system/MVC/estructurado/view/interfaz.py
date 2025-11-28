'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en alerta
'''

from tkinter import *
from tkinter import messagebox
from controller import funciones


    #cadauna interfaz es una funcion
def interfaz():
    #INTERFAZ O VIEW

    ventana=Tk()

    ventana.geometry("600x600")
    ventana.resizable(False,False)
    ventana.title("CALCULADORA")

    op1=StringVar()
    op2=StringVar()

    caja1=Entry(ventana,textvariable=op1,width=5,justify="right")
    caja1.focus()
    caja1.pack(pady=10,anchor="center",side="top")

    caja2=Entry(ventana,textvariable=op2,width=5,justify="right")
    caja2.pack(pady=10,anchor="center",side="top")



    btn1=Button(ventana,text="+",command=lambda:funciones.resultado(op1.get(),op2.get(),"SUMA","+"))
    btn1.pack(pady=5)
    btn2=Button(ventana,text="-",command=lambda:funciones.resultado(op1.get(),op2.get(),"RESTA","-"))
    btn2.pack(pady=5)
    btn3=Button(ventana,text="x",command=lambda:funciones.resultado(op1.get(),op2.get(),"MULTIPLICACION","*"))
    btn3.pack(pady=5)
    btn4=Button(ventana,text="/",command=lambda:funciones.resultado(op1.get(),op2.get(),"DIVISION","/"))
    btn4.pack(pady=5)

    btn5=Button(ventana,text="SALIR",command=ventana.destroy)
    btn5.pack(pady=5)


    ventana.mainloop()