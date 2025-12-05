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





    @staticmethod
    def check_idcamionetas(ventana,tipo,id,accion):
        registro=camionetas.Camionetas.consultarid(id)
        if registro:
            if accion=="Actualizar":
                view1.View.cambiar_camionetas(ventana,tipo,registro)
            else:
                view1.View.borrar_camionetas(ventana,tipo,registro)
        else:
            messagebox.showwarning(title=f"{tipo}",message=f"No existe vehiculo con ese ID")

    def insertar_camionetas(ventana,tipo,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado):
        cerrado=cerrado.lower()
        if cerrado=="si":
            cerrado=1
        else:
            cerrado=0
        registro=camionetas.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado)
        Funciones.respuesta_sql(registro,tipo)

    def consultar_camionetas():
        registro=camionetas.Camionetas.consultar()
        if registro:
            numveh=0
            txt=""
            for i in registro:
                numveh+=1
                txt=txt+f"Num vehiculo: {numveh}  ID: {i[0]}  Marca:  {i[1]}\n  Color: {i[2]}  Modelo: {i[3]}  Velocidad: {i[4]}\n  Caballaje: {i[5]}  Plazas: {i[6]}   Traccion: {i[7]}\n   Cerrada: {i[8]}\n\n"
            return txt
        else:
            txt="No hay registros disponibles"
            return txt
        
    def cambiar_camionetas(ventana,tipo,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado,id):
        cerrado=cerrado.lower()
        if cerrado=="si":
            cerrado=1
        else:
            cerrado=0
        registro=camionetas.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado,id)
        Funciones.respuesta_sql(registro,tipo)

    def borrar_camionetas(ventana,tipo,id):
        registro=camionetas.Camionetas.eliminar(id)
        Funciones.respuesta_sql(registro,tipo)





    @staticmethod
    def check_idcamiones(ventana,tipo,id,accion):
        registro=camiones.Camiones.consultar_id(id)
        if registro:
            if accion=="Actualizar":
                view1.View.cambiar_camiones(ventana,tipo,registro)
            else:
                view1.View.borrar_camiones(ventana,tipo,registro)
        else:
            messagebox.showwarning(title=f"{tipo}",message=f"No existe vehiculo con ese ID")

    def insertar_camiones(ventana,tipo,marca,color,modelo,velocidad,caballaje,plazas,eje,capcarg):
        registro=camiones.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capcarg)
        Funciones.respuesta_sql(registro,tipo)

    def consultar_camiones():
        registro=camiones.Camiones.consultar()
        if registro:
            numveh=0
            txt=""
            for i in registro:
                numveh+=1
                txt=txt+f"Num vehiculo: {numveh}  ID: {i[0]}  Marca:  {i[1]}\n  Color: {i[2]}  Modelo: {i[3]}  Velocidad: {i[4]}\n  Caballaje: {i[5]}  Plazas: {i[6]}   Eje: {i[7]}\n   Capacidad carga: {i[8]}\n\n"
            return txt
        else:
            txt="No hay registros disponibles"
            return txt
        
    def cambiar_camiones(ventana,tipo,marca,color,modelo,velocidad,caballaje,plazas,eje,capcarg,id):
        registro=camiones.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capcarg,id)
        Funciones.respuesta_sql(registro,tipo)

    def borrar_camiones(ventana,tipo,id):
        registro=camiones.Camiones.eliminar(id)
        Funciones.respuesta_sql(registro,tipo)