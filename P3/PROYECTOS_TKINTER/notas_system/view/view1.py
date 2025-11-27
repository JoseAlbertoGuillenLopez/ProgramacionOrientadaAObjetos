# en un inicio todo sin estatico y todas las funciones con self y tambien se mandan a llamar con self
# metodo normal puede llamar a estatico pero esatico no llama al normal

from tkinter import *
from tkinter import messagebox
from controller import controlador1

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.geometry("500x500")
        ventana.title(".:: Notas System ::.")
        ventana.resizable(0,0)
        self.menu_principal(ventana)

    @staticmethod
    def borrar_pantalla(ventana):
        for i in ventana.winfo_children():
            i.destroy()
    
    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=".:: Menú Principal ::.")
        lbltit.pack(pady=10)

        btnreg=Button(ventana,text="1.- Registro",command=lambda:View.registro(ventana))
        btnreg.pack(pady=5)
        btnlog=Button(ventana,text="2.- Login",command=lambda:View.login(ventana)) ### botones con lambda para pasar ventana y se llaman con self
        btnlog.pack(pady=5)
        btnsal=Button(ventana,text="3.- Salir",command=ventana.quit)
        btnsal.pack(pady=5)

    @staticmethod
    def registro(ventana):
        View.borrar_pantalla(ventana) 
        
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

        btnreg=Button(ventana,text="Registrar",command=lambda:{controlador1.Controlador.regusuario(txtnom.get(),txtap.get(),txtmail.get(),txtpass.get(),ventana),View.login(ventana)})
        btnreg.pack(pady=5) ### {} en lambda para 2 acciones
        btnvolv=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btnvolv.pack(pady=5)
    
    @staticmethod
    def login(ventana):
        View.borrar_pantalla(ventana)
        
        lbltit=Label(ventana,text=".:: Inicio de Sesión ::.")
        lbltit.pack(pady=10)

        lblmail=Label(ventana,text="Ingresa tu email").pack(pady=5)
        txtmail=Entry(ventana)
        txtmail.focus()
        txtmail.pack(pady=5)

        lblpass=Label(ventana,text="Ingresa tu Contraseña").pack(pady=5)
        txtpass=Entry(ventana,show="*")
        txtpass.pack(pady=5)

        btnent=Button(ventana,text="Entrar",command=lambda:controlador1.Controlador.login(txtmail.get(),txtpass.get(),ventana)) 
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btnvolv.pack(pady=5)


    @staticmethod
    def menunotas(ventana,user,nom,ap):

        global id_user,nom_user,ap_user
        id_user=user
        nom_user=nom
        ap_user=ap


        View.borrar_pantalla(ventana)
        
        lbltit=Label(ventana,text=f".:: Bienvenido {nom_user} {ap_user}, has iniciado sesion ::.")
        lbltit.pack(pady=10)

        btncr=Button(ventana,text="1.- Crear",command=lambda:View.crear_notas(ventana)) ### abre otro
        btncr.pack(pady=5)
        btnmos=Button(ventana,text="2.- Mostrar",command=lambda:View.mostrar_notas(ventana))
        btnmos.pack(pady=5)
        btnact=Button(ventana,text="3.- Cambiar",command=lambda:View.modificar_notas(ventana))
        btnact.pack(pady=5)
        btneli=Button(ventana,text="4.- Eliminar",command=lambda:View.eliminar_notas(ventana))
        btneli.pack(pady=5)
        btnvolv=Button(ventana,text="5.- Regresar",command=lambda:View.login(ventana))
        btnvolv.pack(pady=5)

    @staticmethod
    def crear_notas(ventana):
        View.borrar_pantalla(ventana)

        lbltit=Label(ventana,text=f"{nom_user} {ap_user}, Vamos a cambiar una Nota ::.::.")
        lbltit.pack(pady=10)

        lbltitulo=Label(ventana,text="Titulo").pack(pady=5)
        txttit=Entry(ventana)
        txttit.focus()
        txttit.pack(pady=5)

        lbldesc=Label(ventana,text="Descripcion").pack(pady=5)
        txtdesc=Entry(ventana)
        txtdesc.pack(pady=5)

        btnent=Button(ventana,text="Crear",command=lambda:controlador1.Controlador.crearnota(id_user,txttit.get(),txttit.get())) ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:View.menunotas(ventana,id_user,nom_user,ap_user))
        btnvolv.pack(pady=5)

    @staticmethod
    def mostrar_notas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: {nom_user} {ap_user}, tus notas son: ::.")
        lbltit.pack(pady=10)
        registros=controlador1.Controlador.mostrarnota(id_user)
        filas=""
        numnota=1
        if registros:
            for i in registros:
                filas=filas+f"Nota: {numnota} \n ID: {i[0]}.- Título: {i[2]}       Fecha Creación: {i[4]}\nDescripción: {i[3]}\n\n "
                numnota=numnota+1

        lblnotas=Label(ventana,text=f"{filas}")
        lblnotas.pack(pady=5)
        
        btnvolv=Button(ventana,text="Volver",command=lambda:View.menunotas(ventana,id_user,nom_user,ap_user))
        btnvolv.pack(pady=5)

    @staticmethod
    def modificar_notas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: {nom_user} {ap_user}, Vamos a cambiar una Nota ::.")
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

        btnent=Button(ventana,text="Guardar",command=lambda:controlador1.Controlador.actualizarnota(txtid.get(),txttit.get(),txtdesc.get())) ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:View.menunotas(ventana,id_user,nom_user,ap_user))
        btnvolv.pack(pady=5)

    @staticmethod
    def eliminar_notas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f" {nom_user} {ap_user}, Vamos a eliminar una Nota ::.")
        lbltit.pack(pady=10)

        lblid=Label(ventana,text="ID de la nota a cambiar:").pack(pady=5)
        txtid=Entry(ventana)
        txtid.focus()
        txtid.pack(pady=5)


        btnent=Button(ventana,text="Eliminar",command=lambda:controlador1.Controlador.eliminarnota(txtid.get())) ### este se va al controlador
        btnent.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:View.menunotas(ventana,id_user,nom_user,ap_user))
        btnvolv.pack(pady=5)







#reg no validado por {} de lambda
#falta validar entry vacio
#rowcount



#globales se pueden poner hasta arriba pero con vacias y abajo les pongo valor, depues de decalarlas las puedo usar para abajo del programa
# def menunotas(self,ventana,datusuario): 
# todas estas funciones tienen respuesta como parametro y en el menunotas tambien debo de pasar ese argumento para los commands