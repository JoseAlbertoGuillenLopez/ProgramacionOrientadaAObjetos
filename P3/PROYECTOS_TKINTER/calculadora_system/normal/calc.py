'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en alerta
'''

from tkinter import *
from tkinter import messagebox


# CONTROL APP O CONTROLLER
def suma(num1,num2):
    try:
        sum=float(num1+num2)
        resultado=messagebox.showinfo(title="SUMA",message=f"{num1}+{num2}={sum}")
    except:
        resultado=messagebox.showinfo(title="SUMA",message=f"Solo valores numericos")

def resta(num1,num2):
    try:
        sum=float(num1-num2)
        resultado=messagebox.showinfo(title="RESTA",message=f"{num1}-{num2}={sum}")
    except:
        resultado=messagebox.showinfo(title="RESTA",message=f"Solo valores numericos")

def division(num1,num2):
    try:
        sum=float(num1/num2)
        resultado=messagebox.showinfo(title="DIVISION",message=f"{num1}/{num2}={sum}")
    except ZeroDivisionError:
        resultado=messagebox.showinfo(title="DIVISION",message=f"0 no divisor")
    except:
        resultado=messagebox.showinfo(title="DIVISION",message=f"Solo valores numericos")
    

def multiplicacion(num1,num2):
    try:
        sum=float(num1*num2)
        resultado=messagebox.showinfo(title="MULTIPLICACION",message=f"{num1}*{num2}={sum}")
    except:
        resultado=messagebox.showinfo(title="MULTIPLICACION",message=f"Solo valores numericos")

#INTERFAZ O VIEW

ventana=Tk()

ventana.geometry("600x600")
ventana.resizable(False,False)
ventana.title("CALCULADORA")

op1=IntVar()
op2=IntVar()

caja1=Entry(ventana,textvariable=op1,width=5,justify="right")
caja1.focus()
caja1.pack(pady=10,anchor="center",side="top")

caja2=Entry(ventana,textvariable=op2,width=5,justify="right")
caja2.pack(pady=10,anchor="center",side="top")



btn1=Button(ventana,text="+",command=lambda:suma(op1.get(),op2.get()))
btn1.pack(pady=5)
btn2=Button(ventana,text="-",command=lambda:resta(op1.get(),op2.get()))
btn2.pack(pady=5)
btn3=Button(ventana,text="x",command=lambda:multiplicacion(op1.get(),op2.get()))
btn3.pack(pady=5)
btn4=Button(ventana,text="/",command=lambda:division(op1.get(),op2.get()))
btn4.pack(pady=5)

btn5=Button(ventana,text="SALIR",command=ventana.destroy)
btn5.pack(pady=5)


ventana.mainloop()