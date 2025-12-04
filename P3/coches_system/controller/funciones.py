from model import coches,camiones,camionetas
from tkinter import messagebox
from view import view1


class Funciones:
    @staticmethod
    def respuesta_sql(respuesta,tipo): 
        if respuesta:
            messagebox.showinfo(title=f"{tipo}",message=f"...¡Accion realizada con exito!...")
            
        else:
            messagebox.showerror(title=f"{tipo}",message=f"...¡No fue posible realizar la accion, intente de nuevo!...")



    @staticmethod
    def check_id(ventana,tipo,id,accion):
        registro=coches.Autos.consultarid(id)
        if registro:
            if accion=="Actualizar":
                view1.View.cambiar_autos(ventana,tipo,registro)
            else:
                view1.View.borrar_autos(ventana,tipo,registro)
        else:
            messagebox.showwarning(title=f"{tipo}",message=f"No existe vehiculo con ese ID")

    def insertar_autos(ventana,tipo,marca,color,modelo,velocidad,caballaje,plazas):
        registro=coches.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        Funciones.respuesta_sql(registro,tipo)

    def consultar_autos():
        registro=coches.Autos.consultar()
        if registro:
            numveh=0
            txt=""
            for i in registro:
                numveh+=1
                txt=txt+f"Num vehiculo: {numveh}  ID: {i[0]}  Marca:  {i[1]}\n  Color: {i[2]}  Modelo: {i[3]}  Velocidad: {i[4]}\n  Caballaje: {i[5]}  Plazas: {i[6]}\n\n"
            return txt
        else:
            txt="No hay registros disponibles"
            return txt
        
    def cambiar_autos(ventana,tipo,marca,color,modelo,velocidad,caballaje,plazas,id):
        registro=coches.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        Funciones.respuesta_sql(registro,tipo)

    def borrar_autos(ventana,tipo,id):
        registro=coches.Autos.eliminar(id)
        Funciones.respuesta_sql(registro,tipo)
