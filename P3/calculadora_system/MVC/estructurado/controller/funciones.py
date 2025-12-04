'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en alerta
'''

from tkinter import *
from tkinter import messagebox


# CONTROL APP O CONTROLLER

def resultado(num1,num2,tit,simb):
    
    try:
        num1=float(num1)
        num2=float(num2)
        if simb=="+":
            sum=num1+num2
            tit="suma"
        elif simb=="-":
            sum=num1-num2
            tit="resta"
        elif simb=="*":
            sum=num1*num2
            tit="multiplicacion"
        elif simb=="/":
            sum=num1/num2
            tit="division"
        messagebox.showinfo(title=f"{tit}",message=f"{num1}{simb}{num2}={sum}")
    except ZeroDivisionError:
        messagebox.showinfo(message=f"0 no divisor")
    except ValueError:
        messagebox.showinfo(message=f"SOLO VALORES NUMERICOS")



