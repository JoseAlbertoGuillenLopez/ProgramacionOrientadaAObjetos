from conexionBD import *

class Operaciones:
    
    @staticmethod
    def insertar(numero1,numero2,signo,resultado):
        try:
            cursor.execute(
                "insert into operaciones values (NULL,NOW(),%s,%s,%s,%s)",(numero1,numero2,signo,resultado)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrar():
        try:
            cursor.execute(
                "select * from operaciones"
            )
            return cursor.fetchall()
        except:
            return False
    
    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        try:
            cursor.execute(
                "update operaciones set fecha=NOW(), n1=%s, n2=%s, signo=%s, resultado=%s where id=%s",(numero1,numero2,signo,resultado,id)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from operaciones where id=%s",(id,)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def check(id):
        try:
            cursor.execute(
                "select * from operaciones where id=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False
        
    