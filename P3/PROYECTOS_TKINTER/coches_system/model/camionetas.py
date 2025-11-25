from conexionBD import *


class Camionetas:
    @staticmethod
    #si es estatico el metodo se puede usar sin tener un objeto creado de esa clase y no se usa el self
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado):
        try:
            cursor.execute(
                "insert into camionetas values (NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute( 
                "select * from camionetas"
            )
            return cursor.fetchall()
        except:
            return False
        
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado,id):
        try:
            cursor.execute(
                "update camionetas set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,traccion=%s,cerrada=%s where id=%s",(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado,id)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from camionetas where id=%s",(id,)
            )
            conexion.commit()
            return True 
        except:
            return False

