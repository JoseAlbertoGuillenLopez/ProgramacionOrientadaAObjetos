from conexionBD import *
class Autos:

    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute(
                "insert into coches values (NULL,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas)
            )
            conexion.commit()
            return True
        except:
            return False 

    @staticmethod
    def consultar(): 
        try:
            cursor.execute(
                "select * from coches"
            )
            return cursor.fetchall()
        except:
            return False
        
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
        try:
            cursor.execute(
                "update coches set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",(marca,color,modelo,velocidad,caballaje,plazas,id)
            )
            conexion.commit()
            return True
        except:
            return False 
        

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from coches where id=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False

