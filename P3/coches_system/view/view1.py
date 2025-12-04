from tkinter import *
from controller import funciones
from model import coches,camiones,camionetas

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.geometry("500x650")
        ventana.title("Gestion de Coches") 
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

        btnau=Button(ventana,text="1.- Autos",command=lambda:View.menu_acciones(ventana,"Autos"))
        btnau.pack(pady=5)
        btncami=Button(ventana,text="2.- Camionetas",command=lambda:View.menu_acciones(ventana,"Camionetas")) 
        btncami.pack(pady=5)
        btncam=Button(ventana,text="3.- Camiones",command=lambda:View.menu_acciones(ventana,"Camiones")) 
        btncam.pack(pady=5)
        btnsal=Button(ventana,text="4.- Salir",command=ventana.quit)
        btnsal.pack(pady=5)





    @staticmethod
    def menu_acciones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Menú {tipo} ::.")
        lbltit.pack(pady=10)
        if tipo=="Autos":
            btnin=Button(ventana,text="1.- Insertar",command=lambda:View.insertar_autos(ventana,tipo))
            btnin.pack(pady=5)
            btncon=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_autos(ventana,tipo)) 
            btncon.pack(pady=5)
            btnact=Button(ventana,text="3.- Actualizar",command=lambda:View.checkid_autos(ventana,tipo,"Actualizar")) 
            btnact.pack(pady=5)
            btneli=Button(ventana,text="5.- Eliminar",command=lambda:View.checkid_autos(ventana,tipo,"Borrar")) 
            btneli.pack(pady=5)
            btnsal=Button(ventana,text="6.- Volver",command=lambda:View.menu_principal(ventana))
            btnsal.pack(pady=5)
        elif tipo=="Camionetas":
            btnin=Button(ventana,text="1.- Insertar",command=lambda:View.insertar_camionetas(ventana,tipo))
            btnin.pack(pady=5)
            btncon=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_camionetas(ventana,tipo)) 
            btncon.pack(pady=5)
            btnact=Button(ventana,text="3.- Actualizar",command=lambda:View.checkid_camionetas(ventana,tipo,"Actualizar")) 
            btnact.pack(pady=5)
            btneli=Button(ventana,text="5.- Eliminar",command=lambda:View.checkid_camionetas(ventana,tipo,"Borrar")) 
            btneli.pack(pady=5)
            btnsal=Button(ventana,text="6.- Volver",command=lambda:View.menu_principal(ventana))
            btnsal.pack(pady=5)
        else:
            btnin=Button(ventana,text="1.- Insertar",command=lambda:View.insertar_camiones(ventana,tipo))
            btnin.pack(pady=5)
            btncon=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_camiones(ventana,tipo)) 
            btncon.pack(pady=5)
            btnact=Button(ventana,text="3.- Actualizar",command=lambda:View.checkid_camiones(ventana,tipo,"Actualizar")) 
            btnact.pack(pady=5)
            btneli=Button(ventana,text="5.- Eliminar",command=lambda:View.checkid_camionetas(ventana,tipo,"Borrar")) 
            btneli.pack(pady=5)
            btnsal=Button(ventana,text="6.- Volver",command=lambda:View.menu_principal(ventana))
            btnsal.pack(pady=5)

    @staticmethod
    def insertar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Insertar {tipo}::.")
        lbltit.pack(pady=10)

        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar()

        lblmar=Label(ventana,text="Marca:").pack(pady=5)
        txtmar=Entry(ventana,textvariable=marca).pack(pady=5)
        lblcol=Label(ventana,text="Color:").pack(pady=5)
        txtcol=Entry(ventana,textvariable=color).pack(pady=5)
        lblmod=Label(ventana,text="Modelo:").pack(pady=5)
        txtmod=Entry(ventana,textvariable=modelo).pack(pady=5)
        lblvel=Label(ventana,text="Velocidad:").pack(pady=5)
        txtvel=Entry(ventana,textvariable=velocidad).pack(pady=5)
        lblcab=Label(ventana,text="Caballaje:").pack(pady=5)
        txtcab=Entry(ventana,textvariable=caballaje).pack(pady=5)
        lblpla=Label(ventana,text="Plazas:").pack(pady=5)
        txtpla=Entry(ventana,textvariable=plazas).pack(pady=5)
        
        btnreg=Button(ventana,text="Registrar",command=lambda:funciones.Funciones.insertar_autos(ventana,tipo,marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get()))
        btnreg.pack(pady=10)

        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Consultar {tipo}::.")
        lbltit.pack(pady=10)

        datos=funciones.Funciones.consultar_autos()

        lblreg=Label(ventana,text=f"{datos}").pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=(20,0))

    @staticmethod
    def checkid_autos(ventana,tipo,accion):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Verificar ID existente de {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()

        lblid=Label(ventana,text="ID:").pack(pady=5)
        txtid=Entry(ventana,textvariable=id).pack(pady=5)

        btncon=Button(ventana,text="Verificar",command=lambda:funciones.Funciones.check_id(ventana,tipo,id.get(),accion))
        btncon.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=10)

    @staticmethod
    def cambiar_autos(ventana,tipo,registros):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Cambiar {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()
        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar()

        id.set(registros[0])
        marca.set(registros[1])
        color.set(registros[2])
        modelo.set(registros[3])
        velocidad.set(registros[4])
        caballaje.set(registros[5])
        plazas.set(registros[6])

        txtid=Entry(ventana,textvariable=id,state="readonly").pack(pady=5)
        lblmar=Label(ventana,text="Marca:").pack(pady=5)
        txtmar=Entry(ventana,textvariable=marca).pack(pady=5)
        lblcol=Label(ventana,text="Color:").pack(pady=5)
        txtcol=Entry(ventana,textvariable=color).pack(pady=5)
        lblmod=Label(ventana,text="Modelo:").pack(pady=5)
        txtmod=Entry(ventana,textvariable=modelo).pack(pady=5)
        lblvel=Label(ventana,text="Velocidad:").pack(pady=5)
        txtvel=Entry(ventana,textvariable=velocidad).pack(pady=5)
        lblcab=Label(ventana,text="Caballaje:").pack(pady=5)
        txtcab=Entry(ventana,textvariable=caballaje).pack(pady=5)
        lblpla=Label(ventana,text="Plazas:").pack(pady=5)
        txtpla=Entry(ventana,textvariable=plazas).pack(pady=5)
        
        btncamb=Button(ventana,text="Actualizar",command=lambda:funciones.Funciones.cambiar_autos(ventana,tipo,marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),id.get()))
        btncamb.pack(pady=10)

        btnsal=Button(ventana,text="Volver",command=lambda:View.checkid_autos(ventana,tipo,"Actualizar"))
        btnsal.pack(pady=10)

    @staticmethod
    def borrar_autos(ventana,tipo,registros):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Borrar {tipo}::.")
        lbltit.pack(pady=10)



        id=IntVar()
        id.set(registros[0])

        lblid=Label(ventana,text="ID del auto a borrar:").pack(pady=5)
        txtid=Entry(ventana,textvariable=id,state="readonly").pack(pady=5)

        btncon=Button(ventana,text="Borrar",command=lambda:funciones.Funciones.borrar_autos(ventana,tipo,id.get()))
        btncon.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.checkid_autos(ventana,tipo,"Eliminar"))
        btnsal.pack(pady=10)






    @staticmethod
    def insertar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Insertar {tipo}::.")
        lbltit.pack(pady=10)

        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar()
        traccion=IntVar()
        cerrado=StringVar()

        lblmar=Label(ventana,text="Marca:").pack(pady=5)
        txtmar=Entry(ventana,textvariable=marca).pack(pady=5)
        lblcol=Label(ventana,text="Color:").pack(pady=5)
        txtcol=Entry(ventana,textvariable=color).pack(pady=5)
        lblmod=Label(ventana,text="Modelo:").pack(pady=5)
        txtmod=Entry(ventana,textvariable=modelo).pack(pady=5)
        lblvel=Label(ventana,text="Velocidad:").pack(pady=5)
        txtvel=Entry(ventana,textvariable=velocidad).pack(pady=5)
        lblcab=Label(ventana,text="Caballaje:").pack(pady=5)
        txtcab=Entry(ventana,textvariable=caballaje).pack(pady=5)
        lblpla=Label(ventana,text="Plazas:").pack(pady=5)
        txtpla=Entry(ventana,textvariable=plazas).pack(pady=5)
        lbltra=Label(ventana,text="Traccion:").pack(pady=5)
        txttra=Entry(ventana,textvariable=traccion).pack(pady=5)
        lblcer=Label(ventana,text="Cerrado:").pack(pady=5)
        txtcer=Entry(ventana,textvariable=cerrado).pack(pady=5)
        
        btnreg=Button(ventana,text="Registrar",command=lambda:funciones.Funciones.insertar_camionetas(ventana,tipo,marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),traccion.get(),cerrado.get()))
        btnreg.pack(pady=10)

        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=10)

    @staticmethod
    def consultar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Consultar {tipo}::.")
        lbltit.pack(pady=10)

        datos=funciones.Funciones.consultar_camionetas()

        lblreg=Label(ventana,text=f"{datos}").pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=(20,0))

    @staticmethod
    def checkid_camionetas(ventana,tipo,accion):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Verificar ID existente de {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()

        lblid=Label(ventana,text="ID:").pack(pady=5)
        txtid=Entry(ventana,textvariable=id).pack(pady=5)

        btncon=Button(ventana,text="Verificar",command=lambda:funciones.Funciones.check_idcamionetas(ventana,tipo,id.get(),accion))
        btncon.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=10)

    @staticmethod
    def cambiar_camionetas(ventana,tipo,registros):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Cambiar {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()
        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar()
        traccion=IntVar()
        cerrado=StringVar()

        id.set(registros[0])
        marca.set(registros[1])
        color.set(registros[2])
        modelo.set(registros[3])
        velocidad.set(registros[4])
        caballaje.set(registros[5])
        plazas.set(registros[6])
        traccion.set(registros[7])
        cerrado.set(registros[8])

        txtid=Entry(ventana,textvariable=id,state="readonly").pack(pady=5)
        lblmar=Label(ventana,text="Marca:").pack(pady=5)
        txtmar=Entry(ventana,textvariable=marca).pack(pady=5)
        lblcol=Label(ventana,text="Color:").pack(pady=5)
        txtcol=Entry(ventana,textvariable=color).pack(pady=5)
        lblmod=Label(ventana,text="Modelo:").pack(pady=5)
        txtmod=Entry(ventana,textvariable=modelo).pack(pady=5)
        lblvel=Label(ventana,text="Velocidad:").pack(pady=5)
        txtvel=Entry(ventana,textvariable=velocidad).pack(pady=5)
        lblcab=Label(ventana,text="Caballaje:").pack(pady=5)
        txtcab=Entry(ventana,textvariable=caballaje).pack(pady=5)
        lblpla=Label(ventana,text="Plazas:").pack(pady=5)
        txtpla=Entry(ventana,textvariable=plazas).pack(pady=5)
        lbltra=Label(ventana,text="Traccion:").pack(pady=5)
        txttra=Entry(ventana,textvariable=traccion).pack(pady=5)
        lblcer=Label(ventana,text="Cerrado:").pack(pady=5)
        txtcer=Entry(ventana,textvariable=cerrado).pack(pady=5)

        btncamb=Button(ventana,text="Actualizar",command=lambda:funciones.Funciones.cambiar_camionetas(ventana,tipo,marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),traccion.get(),cerrado.get(),id.get()))
        btncamb.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.checkid_camionetas(ventana,tipo,"Actualizar"))
        btnsal.pack(pady=10)

    @staticmethod
    def borrar_camionetas(ventana,tipo,registros):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Borrar {tipo}::.")
        lbltit.pack(pady=10)


        id=IntVar()
        id.set(registros[0])

        lblid=Label(ventana,text="ID de la camioneta a borrar:").pack(pady=5)
        txtid=Entry(ventana,textvariable=id,state="readonly").pack(pady=5)

        btncon=Button(ventana,text="Borrar",command=lambda:funciones.Funciones.borrar_camionetas(ventana,tipo,id.get()))
        btncon.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.checkid_camionetas(ventana,tipo,"Eliminar"))
        btnsal.pack(pady=10)





    @staticmethod
    def insertar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Insertar {tipo}::.")
        lbltit.pack(pady=10)

        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar()
        eje=IntVar()
        capcarg=IntVar()

        lblmar=Label(ventana,text="Marca:").pack(pady=5)
        txtmar=Entry(ventana,textvariable=marca).pack(pady=5)
        lblcol=Label(ventana,text="Color:").pack(pady=5)
        txtcol=Entry(ventana,textvariable=color).pack(pady=5)
        lblmod=Label(ventana,text="Modelo:").pack(pady=5)
        txtmod=Entry(ventana,textvariable=modelo).pack(pady=5)
        lblvel=Label(ventana,text="Velocidad:").pack(pady=5)
        txtvel=Entry(ventana,textvariable=velocidad).pack(pady=5)
        lblcab=Label(ventana,text="Caballaje:").pack(pady=5)
        txtcab=Entry(ventana,textvariable=caballaje).pack(pady=5)
        lblpla=Label(ventana,text="Plazas:").pack(pady=5)
        txtpla=Entry(ventana,textvariable=plazas).pack(pady=5)
        lbleje=Label(ventana,text="Eje:").pack(pady=5)
        txteje=Entry(ventana,textvariable=eje).pack(pady=5)
        lblcap=Label(ventana,text="Capacidad carga:").pack(pady=5)
        txtcap=Entry(ventana,textvariable=capcarg).pack(pady=5)
        
        btnreg=Button(ventana,text="Registrar",command=lambda:"")
        btnreg.pack(pady=10)

        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=10)

    @staticmethod
    def consultar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Consultar {tipo}::.")
        lbltit.pack(pady=10)

        lblreg=Label(ventana,text="registros").pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=(20,0))

    @staticmethod
    def checkid_camiones(ventana,tipo,accion):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Verificar ID existente de {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()

        lblid=Label(ventana,text="ID:").pack(pady=5)
        txtid=Entry(ventana,textvariable=id).pack(pady=5)

        btncon=Button(ventana,text="Verificar",command=lambda:"")
        btncon.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,tipo))
        btnsal.pack(pady=10)

    @staticmethod
    def cambiar_camiones(ventana,tipo,registros):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Cambiar {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()
        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar()
        eje=IntVar()
        capcarg=IntVar()

        txtid=Entry(ventana,textvariable=id,state="readonly").pack(pady=5)
        lblmar=Label(ventana,text="Marca:").pack(pady=5)
        txtmar=Entry(ventana,textvariable=marca).pack(pady=5)
        lblcol=Label(ventana,text="Color:").pack(pady=5)
        txtcol=Entry(ventana,textvariable=color).pack(pady=5)
        lblmod=Label(ventana,text="Modelo:").pack(pady=5)
        txtmod=Entry(ventana,textvariable=modelo).pack(pady=5)
        lblvel=Label(ventana,text="Velocidad:").pack(pady=5)
        txtvel=Entry(ventana,textvariable=velocidad).pack(pady=5)
        lblcab=Label(ventana,text="Caballaje:").pack(pady=5)
        txtcab=Entry(ventana,textvariable=caballaje).pack(pady=5)
        lblpla=Label(ventana,text="Plazas:").pack(pady=5)
        txtpla=Entry(ventana,textvariable=plazas).pack(pady=5)
        lbleje=Label(ventana,text="Eje:").pack(pady=5)
        txteje=Entry(ventana,textvariable=eje).pack(pady=5)
        lblcap=Label(ventana,text="Capacidad carga:").pack(pady=5)
        txtcap=Entry(ventana,textvariable=capcarg).pack(pady=5)

        btncamb=Button(ventana,text="Actualizar",command=lambda:"")
        btncamb.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.checkid_camiones(ventana,tipo,"Actualizar"))
        btnsal.pack(pady=10)

    @staticmethod
    def borrar_camiones(ventana,tipo,registros):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Borrar {tipo}::.")
        lbltit.pack(pady=10)

        id=IntVar()
        #id.set(id)

        lblid=Label(ventana,text="ID del camion a borrar:").pack(pady=5)
        txtid=Entry(ventana,textvariable=id,state="readonly").pack(pady=5)

        btncon=Button(ventana,text="Borrar",command=lambda:"")
        btncon.pack(pady=10)
        
        btnsal=Button(ventana,text="Volver",command=lambda:View.checkid_camiones(ventana,tipo,"Eliminar"))
        btnsal.pack(pady=10)
