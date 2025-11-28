'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en alerta 
'''

from tkinter import *
from tkinter import messagebox 
from model import operaciones
from view import interfaz

class funcionesc:

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="Estado",message=f"Accion realizada exitosamente")
        else:
            messagebox.showerror(title="Estado",message=f"Fallo al realizar la accion")

    @staticmethod
    def resultado(num1,num2,tit,simb):
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
        resultado=messagebox.askquestion(title=f"{tit}",message=f"{num1}{simb}{num2}={sum} \n¿Deseas guardar en la base de datos?")
        if resultado=="yes":
            respuesta=operaciones.Operaciones.insertar(num1,num2,simb,sum)
            funcionesc.respuesta_sql(respuesta)


    @staticmethod
    def eliminar(id):
        respuesta=operaciones.Operaciones.eliminar(id)
        funcionesc.respuesta_sql(respuesta)

    @staticmethod
    def mostrar(): 
        respuesta=operaciones.Operaciones.mostrar()
        if respuesta:
            cont=0
            res=""
            for i in respuesta:
                cont+=1
                res=res+f"Operacion: {cont:<5} ID: {i[0]:<5}  Fecha creacion: {i[1]}  \n  Operacion: {i[2]}{i[4]}{i[3]}={i[5]}\n\n" 
            return res 
        else:
            messagebox.showinfo(message="No hay registros en la BD")


    @staticmethod
    def checar_actualizacion(id,ventana):
            respuesta=operaciones.Operaciones.check(id)
            if respuesta:
                interfaz.vista.actuallizar_dag(respuesta[2],respuesta[3],respuesta[4],respuesta[5],id,ventana)
            else:
                messagebox.showwarning(title="Actualizar",message="No existe operacion con ese ID")


    @staticmethod
    def enviar_actualizacion(num1,num2,simb,res,id):
            respuesta=operaciones.Operaciones.actualizar(num1,num2,simb,res,id)
            funcionesc.respuesta_sql(respuesta)











    @staticmethod
    def check(id,ventana): 
        respuesta=operaciones.Operaciones.check(id)
        if respuesta:
            interfaz.vista.actualizar_screen2(ventana,respuesta)
        else:
            messagebox.showinfo(message=f"ID no encontrada")

        
        
        

# si quiero con decimales y validaciones:
# los hago string y luego a float y aqui valido valueerror
# en vez de usar num1.get() uso caja1.get() para que no cambie a int


