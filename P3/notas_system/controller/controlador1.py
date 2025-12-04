from tkinter import messagebox
from view import view1
from model import usuario,nota

    #view=view1.View(ventana)
    #view.menu_principal(ventana)
    # view1.View.menu_principal(ventana) 

class Controlador:
    
    @staticmethod
    def respuesta_sql(respuesta): 
        if respuesta:
            messagebox.showinfo(title="Notas",message=f"...¡Accion realizada con exito!...")
            
        else:
            messagebox.showerror(title="Notas",message=f"...¡No fue posible realizar la accion, intente de nuevo!...")

    @staticmethod
    def regusuario(nombre,apellidos,email,passw,ventana): 
        respuesta=usuario.Usuario.registrar(nombre,apellidos,email,passw)
        if respuesta:
            messagebox.showinfo(title="Usuarios",message=f"{nombre} {apellidos} registrado correctamente con el mail {email}")
        else:
            messagebox.showerror(message="** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...",title="Usuarios")


    @staticmethod
    def login(mail,passw,ventana):
        datusuario=usuario.Usuario.iniciar_sesion(mail,passw)
        if datusuario:
            messagebox.showinfo(title="Usuarios",message=f"{datusuario[1]} {datusuario[2]} , iniciaste sesion correctamente ::.")
            view1.View.menunotas(ventana,datusuario[0],datusuario[1],datusuario[2])
        else:
            messagebox.showerror(message="** Email y/o contraseña incorrectas... vuelve a inteterlo ...",title="Usuarios")



    @staticmethod
    def crearnota(usuario_id,titulo,desc):
        respuesta=nota.Nota.crear(usuario_id,titulo,desc)
        Controlador.respuesta_sql(respuesta)
        

    @staticmethod
    def mostrarnota(usuario_id):
        respuesta=nota.Nota.mostrar(usuario_id)
        if respuesta:
            return respuesta
        else:
            respuesta=""
            messagebox.showwarning(message="No hay registros para mostrar",title="Notas")
            return respuesta


    @staticmethod
    def actualizarnota(id,tit,desc):
        respuesta=nota.Nota.actualizar(id,tit,desc)
        Controlador.respuesta_sql(respuesta)
        

    @staticmethod
    def eliminarnota(id):
        respuesta=nota.Nota.eliminar(id) 
        Controlador.respuesta_sql(respuesta)
        