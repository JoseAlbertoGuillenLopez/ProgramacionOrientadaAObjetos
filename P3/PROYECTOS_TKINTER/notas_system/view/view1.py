# en un inicio todo sin estatico y todas las funciones con self y tambien se mandan a llamar con self
# metodo normal puede llamar a estatico pero esatico no llama al normal

from tkinter import *
from tkinter import messagebox
from controller import funciones

class View:
    def __init__(self,ventana):
        self.ventana=ventana ### no es necesario
        ventana.geometry("500x500")
        ventana.title("Gestión de Notas")
        #View.menu_pricipal(ventana)
        self.menu_principal(ventana)

    
    def borrar_pantalla(self,ventana):
        for i in ventana.winfo_children():
            i.destroy()
    
    def menu_principal(self,ventana):
        self.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=".:: Menú Principal ::.")
        lbltit.pack(pady=10)

        btnreg=Button(ventana,text="1.- Registro",command=lambda:self.registro(ventana))
        btnreg.pack(pady=5)
        btnlog=Button(ventana,text="2.- Login",command=lambda:self.login(ventana)) ### botones con lambda para pasar ventana y se llaman con self
        btnlog.pack(pady=5)
        btnsal=Button(ventana,text="3.- Salir",command=ventana.quit)
        btnsal.pack(pady=5)

    def registro(self,ventana):
        self.borrar_pantalla(ventana) 
        
        lbltit=Label(ventana,text=".:: Registro en el Sistema ::.")
        lbltit.pack(pady=10)

        lblnom=Label(ventana,text="¿Cual es tu nombre?").pack(pady=5)
        txtnom=Entry(ventana)
        txtnom.focus()
        txtnom.pack(pady=5)

        lblap=Label(ventana,text="¿Cuales son tus apellidos?").pack(pady=5)
        txtap=Entry(ventana)
        txtap.pack(pady=5)

        lblmail=Label(ventana,text="Ingresa tu email").pack(pady=5)
        txtmail=Entry(ventana)
        txtmail.pack(pady=5)

        lblpass=Label(ventana,text="Ingresa tu Contraseña").pack(pady=5)
        txtpass=Entry(ventana,show="*")
        txtpass.pack(pady=5)

        btnreg=Button(ventana,text="Registrar",command=lambda:"") ### este se va al controlador
        btnreg.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:self.menu_principal(ventana))
        btnvolv.pack(pady=5)
    
    def login(self,ventana):
        self.borrar_pantalla(ventana)
        
        lbltit=Label(ventana,text=".:: Inicio de Sesión ::.")
        lbltit.pack(pady=10)

        lblmail=Label(ventana,text="Ingresa tu email").pack(pady=5)
        txtmail=Entry(ventana)
        txtmail.focus()
        txtmail.pack(pady=5)

        lblpass=Label(ventana,text="Ingresa tu Contraseña").pack(pady=5)
        txtpass=Entry(ventana,show="*")
        txtpass.pack(pady=5)

        btnent=Button(ventana,text="Entrar",command=lambda:self.menunotas(ventana)) ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:self.menu_principal(ventana))
        btnvolv.pack(pady=5)



    def menunotas(self,ventana):  #falta el usuario
        self.borrar_pantalla(ventana)
        
        lbltit=Label(ventana,text=f".:: Bienvenido {'nombre'}, has iniciado sesion ::.")
        lbltit.pack(pady=10)

        btncr=Button(ventana,text="1.- Crear",command=lambda:self.crear_notas(ventana)) ### abre otro
        btncr.pack(pady=5)
        btnmos=Button(ventana,text="2.- Mostrar",command=lambda:self.mostrar_notas(ventana))
        btnmos.pack(pady=5)
        btnact=Button(ventana,text="3.- Cambiar",command=lambda:self.modificar_notas(ventana))
        btnact.pack(pady=5)
        btneli=Button(ventana,text="4.- Eliminar",command=lambda:self.eliminar_notas(ventana))
        btneli.pack(pady=5)
        btnvolv=Button(ventana,text="5.- Regresar",command=lambda:self.login(ventana))
        btnvolv.pack(pady=5)

    def crear_notas(self,ventana):
        self.borrar_pantalla(ventana)

        lbltit=Label(ventana,text=".:: Crear nota ::.")
        lbltit.pack(pady=10)

        lbltitulo=Label(ventana,text="Titulo").pack(pady=5)
        txttit=Entry(ventana)
        txttit.focus()
        txttit.pack(pady=5)

        lbldesc=Label(ventana,text="Descripcion").pack(pady=5)
        txtdesc=Entry(ventana)
        txtdesc.pack(pady=5)

        btnent=Button(ventana,text="Crear",command=lambda:"") ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:self.menunotas(ventana))
        btnvolv.pack(pady=5)

    def mostrar_notas(self,ventana):
        self.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f"{'nombre'}, tus notas son: ")
        lbltit.pack(pady=10)

        filas=""
        registros=[("1","100","nota 1","descripcion","2025-22-34")]
        numnota=1
        if registros:
            for i in registros:
                filas=filas+f"Nota: {numnota} \n ID: {i[0]}.- Título: {i[2]}       Fecha creación: {i[4]}\nDescripción: {i[3]} "
                numnota=numnota+1

        else:
            messagebox.showinfo(message="No hay notas para ese usuario")
        

        lblnotas=Label(ventana,text=f"{filas}")
        lblnotas.pack(pady=5)
        
        btnvolv=Button(ventana,text="Volver",command=lambda:self.menunotas(ventana))
        btnvolv.pack(pady=5)

    def modificar_notas(self,ventana):
        self.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f"Nombre, Vamos a cambiar una Nota ::.")
        lbltit.pack(pady=10)

        lblid=Label(ventana,text="ID de la nota a cambiar:").pack(pady=5)
        txtid=Entry(ventana)
        txtid.focus()
        txtid.pack(pady=5)

        lbltitulo=Label(ventana,text="Nuevo Título:").pack(pady=5)
        txttit=Entry(ventana)
        txttit.pack(pady=5)

        lbldesc=Label(ventana,text="Nueva Descripcion").pack(pady=5)
        txtdesc=Entry(ventana)
        txtdesc.pack(pady=5)

        btnent=Button(ventana,text="Guardar",command=lambda:"") ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:self.menunotas(ventana))
        btnvolv.pack(pady=5)

    def eliminar_notas(self,ventana):
        self.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f"Nombre, Vamos a eliminar una Nota ::.")
        lbltit.pack(pady=10)

        lblid=Label(ventana,text="ID de la nota a cambiar:").pack(pady=5)
        txtid=Entry(ventana)
        txtid.focus()
        txtid.pack(pady=5)


        btnent=Button(ventana,text="Eliminar",command=lambda:"") ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:self.menunotas(ventana))
        btnvolv.pack(pady=5)

# def menunotas(self,ventana,respuesta): 
# todas estas funciones tienen respuesta como parametro y en el menunotas tambien debo de pasar ese argumento para los commands