from model import coches,camiones,camionetas
from tkinter import messagebox
from view import view1

class Funciones:

    @staticmethod
    def regcoche(marca,color,modelo,velocidad,caballaje,plazas,ventana):
        if marca and color:
            respuesta=coches.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
            if respuesta:
                messagebox.showinfo(message="Registro agregado")
                obj=view1.View(ventana)
                obj.menu_coches(ventana)
            else:
                messagebox.showerror(message="Error al insertar")
        else:
            messagebox.showwarning(message="Rellena todos los campos")

    @staticmethod
    def actcoche(marca,color,modelo,velocidad,caballaje,plazas,id,ventana):
        if marca and color:
            respuesta=coches.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
            if respuesta:
                messagebox.showinfo(message="Registro actualizado")
                obj=view1.View(ventana)
                obj.menu_coches(ventana)
            else:
                messagebox.showerror(message="Error al actualizar")
        else:
            messagebox.showwarning(message="Selecciona un registro")

    @staticmethod
    def elicoche(id,ventana):
        if id:
            respuesta=coches.Autos.eliminar(id)
            if respuesta:
                messagebox.showinfo(message="Registro eliminado")
                obj=view1.View(ventana)
                obj.menu_coches(ventana)
            else:
                messagebox.showerror(message="Error al eliminar")
        else:
            messagebox.showwarning(message="Selecciona un registro")






    @staticmethod
    def regcamioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,ventana):
        if marca and color and traccion and cerrada:
            cerrada=cerrada.lower()
            if cerrada=="si":
                cerrada=1
            respuesta=camionetas.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            if respuesta:
                messagebox.showinfo(message="Registro agregado")
                obj=view1.View(ventana)
                obj.menu_camionetas(ventana)
            else:
                messagebox.showerror(message="Error al insertar")
        else:
            messagebox.showwarning(message="Rellena todos los campos")

    @staticmethod
    def actcamioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id,ventana):
        if marca and color and traccion and cerrada:
            cerrada=cerrada.lower()
            if cerrada=="si":
                cerrada=1
            respuesta=camionetas.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
            if respuesta:
                messagebox.showinfo(message="Registro actualizado")
                obj=view1.View(ventana)
                obj.menu_camionetas(ventana)
            else:
                messagebox.showerror(message="Error al actualizar")
        else:
            messagebox.showwarning(message="Selecciona un registro")

    @staticmethod
    def elicamioneta(id,ventana):
        if id:
            respuesta=camionetas.Camionetas.eliminar(id)
            if respuesta:
                messagebox.showinfo(message="Registro eliminado")
                obj=view1.View(ventana)
                obj.menu_camionetas(ventana)
            else:
                messagebox.showerror(message="Error al eliminar")
        else:
            messagebox.showwarning(message="Selecciona un registro")




    @staticmethod
    def regcamion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,ventana):
        if marca and color:
            respuesta=camiones.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad)
            if respuesta:
                messagebox.showinfo(message="Registro agregado")
                obj=view1.View(ventana)
                obj.menu_camiones(ventana)
            else:
                messagebox.showerror(message="Error al insertar")
        else:
            messagebox.showwarning(message="Rellena todos los campos")

    @staticmethod
    def actcamion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id,ventana):
        if marca and color:
            respuesta=camiones.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id)
            if respuesta:
                messagebox.showinfo(message="Registro actualizado")
                obj=view1.View(ventana)
                obj.menu_camiones(ventana)
            else:
                messagebox.showerror(message="Error al actualizar")
        else:
            messagebox.showwarning(message="Selecciona un registro")

    @staticmethod
    def elicamion(id,ventana):
        if id:
            respuesta=camiones.Camiones.eliminar(id)
            if respuesta:
                messagebox.showinfo(message="Registro eliminado")
                obj=view1.View(ventana)
                obj.menu_camiones(ventana)
            else:
                messagebox.showerror(message="Error al eliminar")
        else:
            messagebox.showwarning(message="Selecciona un registro")