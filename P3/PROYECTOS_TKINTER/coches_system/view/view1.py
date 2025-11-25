from tkinter import *
from tkinter import ttk
from controller import funciones
from model import coches,camiones,camionetas

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.geometry("1200x400")
        ventana.title("Gestion de Coches")
        self.menu_principal(ventana)

    def borrar_pantalla(self,ventana):
        for i in ventana.winfo_children():
            i.destroy()

    def menu_principal(self,ventana):
        self.borrar_pantalla(ventana)
        lbltit=Label(text="MENU PRINCIPAL").pack(pady=10)
        btnco=Button(ventana,background="#824942",text="Coches",command=lambda:self.menu_coches(ventana)).pack(pady=5)
        btncamionetas=Button(ventana,background="#bf938b",text="Camionetas",command=lambda:self.menu_camionetas(ventana)).pack(pady=5)
        btncamiones=Button(ventana,background="#ffdcd3",text="Camiones",command=lambda:self.menu_camiones(ventana)).pack(pady=5)
        btnsal=Button(ventana,background="#f9210e",text="Salir",command=ventana.destroy).pack(pady=5)
    
    def menu_coches(self,ventana):
        self.borrar_pantalla(ventana)

        frame0=Frame(ventana)
        frame0.grid(row=0,column=0)
        frame1=Frame(ventana)
        frame1.grid(row=1,column=0)
        frame2=Frame(ventana)
        frame2.grid(row=2,column=0)
        frame3=Frame(ventana)
        frame3.grid(row=3,column=0)


        lbltit=Label(frame0,text="MENU COCHES").grid(row=0,column=0,pady=15)

        id=IntVar()
        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar() 

        lblmar=Label(frame1,text="marca:").grid(row=0,column=0)
        txtmar=Entry(frame1,textvariable=marca).grid(row=0,column=1)
        lblcol=Label(frame1,text="color:").grid(row=0,column=2)
        txtcol=Entry(frame1,textvariable=color).grid(row=0,column=3)
        lblmod=Label(frame1,text="modelo:").grid(row=0,column=4)
        txtmod=Entry(frame1,textvariable=modelo).grid(row=0,column=5)
        lblvel=Label(frame1,text="velocidad:").grid(row=1,column=0)
        txtvel=Entry(frame1,textvariable=velocidad).grid(row=1,column=1)
        lblcab=Label(frame1,text="caballaje:").grid(row=1,column=2)
        txtcab=Entry(frame1,textvariable=caballaje).grid(row=1,column=3)
        lblpl=Label(frame1,text="plazas:").grid(row=1,column=4)
        txtpl=Entry(frame1,textvariable=plazas).grid(row=1,column=5)

        tabla=ttk.Treeview(frame2,columns=("id","marca","color","modelo","velocidad","caballaje","plazas"),show="headings")
        tabla.heading("id",text="ID")
        tabla.heading("marca",text="marca")
        tabla.heading("color",text="color")
        tabla.heading("modelo",text="modelo")
        tabla.heading("velocidad",text="velocidad")
        tabla.heading("caballaje",text="caballaje")
        tabla.heading("plazas",text="plazas")

        tabla.column("id", width=30)
        tabla.column("marca", width=170)
        tabla.column("color", width=170)
        tabla.column("modelo", width=170)
        tabla.column("velocidad", width=170)
        tabla.column("caballaje", width=170)
        tabla.column("plazas", width=170)

        datos=coches.Autos.consultar()
        if datos:
            for i in datos:
                tabla.insert("",END,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

        def seleccionar(event):
            item=tabla.selection()
            if item:
                valores=tabla.item(item)["values"]
                id.set(valores[0])
                marca.set(valores[1])
                color.set(valores[2])
                modelo.set(valores[3])
                velocidad.set(valores[4])
                caballaje.set(valores[5])
                plazas.set(valores[6])

        def limpiar():
            marca.set("")
            color.set("")
            modelo.set(0)
            velocidad.set(0)
            caballaje.set(0)
            plazas.set(0)

        tabla.bind("<<TreeviewSelect>>", seleccionar)

        tabla.grid(row=0,column=0,padx=80,pady=10)

        btnag=Button(frame3,text="Agregar",command=lambda:funciones.Funciones.regcoche(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),ventana)).grid(row=0,column=0,padx=5)
        btnac=Button(frame3,text="Actualizar",command=lambda:funciones.Funciones.actcoche(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),id.get(),ventana)).grid(row=0,column=1,padx=5)
        btnel=Button(frame3,text="Eliminar",command=lambda:funciones.Funciones.elicoche(id.get(),ventana)).grid(row=0,column=2,padx=5)
        btnbor=Button(frame3,text="Limpiar",command=limpiar).grid(row=0,column=3,padx=5)
        btnvolv=Button(frame3,text="Volver",command=lambda:self.menu_principal(ventana)).grid(row=0,column=4,padx=5)

    def menu_camionetas(self,ventana):
        self.borrar_pantalla(ventana)

        frame0=Frame(ventana)
        frame0.grid(row=0,column=0)
        frame1=Frame(ventana)
        frame1.grid(row=1,column=0)
        frame2=Frame(ventana)
        frame2.grid(row=2,column=0)
        frame3=Frame(ventana)
        frame3.grid(row=3,column=0)


        lbltit=Label(frame0,text="MENU CAMIONETAS").grid(row=0,column=0,pady=15)

        id=IntVar()
        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar() 
        traccion=StringVar()
        cerrada=StringVar()

        lblmar=Label(frame1,text="marca:").grid(row=0,column=0)
        txtmar=Entry(frame1,textvariable=marca).grid(row=0,column=1)
        lblcol=Label(frame1,text="color:").grid(row=0,column=2)
        txtcol=Entry(frame1,textvariable=color).grid(row=0,column=3)
        lblmod=Label(frame1,text="modelo:").grid(row=0,column=4)
        txtmod=Entry(frame1,textvariable=modelo).grid(row=0,column=5)
        lblvel=Label(frame1,text="velocidad:").grid(row=0,column=6)
        txtvel=Entry(frame1,textvariable=velocidad).grid(row=0,column=7)


        lblcab=Label(frame1,text="caballaje:").grid(row=1,column=0)
        txtcab=Entry(frame1,textvariable=caballaje).grid(row=1,column=1)
        lblpl=Label(frame1,text="plazas:").grid(row=1,column=2)
        txtpl=Entry(frame1,textvariable=plazas).grid(row=1,column=3)
        lbltr=Label(frame1,text="traccion:").grid(row=1,column=4)
        txttr=Entry(frame1,textvariable=traccion).grid(row=1,column=5)
        lblcer=Label(frame1,text="cerrada (si/no):").grid(row=1,column=6)
        txtcer=Entry(frame1,textvariable=cerrada).grid(row=1,column=7)

        tabla=ttk.Treeview(frame2,columns=("id","marca","color","modelo","velocidad","caballaje","plazas","traccion","cerrada"),show="headings")
        tabla.heading("id",text="ID")
        tabla.heading("marca",text="marca")
        tabla.heading("color",text="color")
        tabla.heading("modelo",text="modelo")
        tabla.heading("velocidad",text="velocidad")
        tabla.heading("caballaje",text="caballaje")
        tabla.heading("plazas",text="plazas")
        tabla.heading("traccion",text="traccion")
        tabla.heading("cerrada",text="cerrada")

        tabla.column("id", width=30)
        tabla.column("marca", width=150)
        tabla.column("color", width=150)
        tabla.column("modelo", width=150)
        tabla.column("velocidad", width=150)
        tabla.column("caballaje", width=150)
        tabla.column("plazas", width=150)
        tabla.column("traccion", width=120)
        tabla.column("cerrada", width=120)

        datos=camionetas.Camionetas.consultar()
        if datos:
            for i in datos:
                tabla.insert("",END,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

        def seleccionar(event):
            item=tabla.selection()
            if item:
                valores=tabla.item(item)["values"]
                id.set(valores[0])
                marca.set(valores[1])
                color.set(valores[2])
                modelo.set(valores[3])
                velocidad.set(valores[4])
                caballaje.set(valores[5])
                plazas.set(valores[6])
                traccion.set(valores[7])
                cerrada.set(valores[8])

        def limpiar():
            marca.set("")
            color.set("")
            modelo.set(0)
            velocidad.set(0)
            caballaje.set(0)
            plazas.set(0)
            traccion.set("")
            cerrada.set("")

        tabla.bind("<<TreeviewSelect>>", seleccionar)

        tabla.grid(row=0,column=0,pady=10,padx=10)

        btnag=Button(frame3,text="Agregar",command=lambda:funciones.Funciones.regcamioneta(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),traccion.get(),cerrada.get(),ventana)).grid(row=0,column=0,padx=5)
        btnac=Button(frame3,text="Actualizar",command=lambda:funciones.Funciones.actcamioneta(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),traccion.get(),cerrada.get(),id.get(),ventana)).grid(row=0,column=1,padx=5)
        btnel=Button(frame3,text="Eliminar",command=lambda:funciones.Funciones.elicamioneta(id.get(),ventana)).grid(row=0,column=2,padx=5)
        btnbor=Button(frame3,text="Limpiar",command=limpiar).grid(row=0,column=3,padx=5)
        btnvolv=Button(frame3,text="Volver",command=lambda:self.menu_principal(ventana)).grid(row=0,column=4,padx=5)

    def menu_camiones(self,ventana):
        self.borrar_pantalla(ventana)

        frame0=Frame(ventana)
        frame0.grid(row=0,column=0)
        frame1=Frame(ventana)
        frame1.grid(row=1,column=0)
        frame2=Frame(ventana)
        frame2.grid(row=2,column=0)
        frame3=Frame(ventana)
        frame3.grid(row=3,column=0)


        lbltit=Label(frame0,text="MENU CAMIONES").grid(row=0,column=0,pady=15)

        id=IntVar()
        marca=StringVar()
        color=StringVar()
        modelo=IntVar()
        velocidad=IntVar()
        caballaje=IntVar()
        plazas=IntVar() 
        eje=IntVar()
        capacidad=IntVar()

        lblmar=Label(frame1,text="marca:").grid(row=0,column=0)
        txtmar=Entry(frame1,textvariable=marca).grid(row=0,column=1)
        lblcol=Label(frame1,text="color:").grid(row=0,column=2)
        txtcol=Entry(frame1,textvariable=color).grid(row=0,column=3)
        lblmod=Label(frame1,text="modelo:").grid(row=0,column=4)
        txtmod=Entry(frame1,textvariable=modelo).grid(row=0,column=5)
        lblvel=Label(frame1,text="velocidad:").grid(row=0,column=6)
        txtvel=Entry(frame1,textvariable=velocidad).grid(row=0,column=7)


        lblcab=Label(frame1,text="caballaje:").grid(row=1,column=0)
        txtcab=Entry(frame1,textvariable=caballaje).grid(row=1,column=1)
        lblpl=Label(frame1,text="plazas:").grid(row=1,column=2)
        txtpl=Entry(frame1,textvariable=plazas).grid(row=1,column=3)
        lbleje=Label(frame1,text="eje:").grid(row=1,column=4)
        txteje=Entry(frame1,textvariable=eje).grid(row=1,column=5)
        lblcap=Label(frame1,text="capacidad:").grid(row=1,column=6)
        txtcap=Entry(frame1,textvariable=capacidad).grid(row=1,column=7)

        tabla=ttk.Treeview(frame2,columns=("id","marca","color","modelo","velocidad","caballaje","plazas","eje","capacidad"),show="headings")
        tabla.heading("id",text="ID")
        tabla.heading("marca",text="marca")
        tabla.heading("color",text="color")
        tabla.heading("modelo",text="modelo")
        tabla.heading("velocidad",text="velocidad")
        tabla.heading("caballaje",text="caballaje")
        tabla.heading("plazas",text="plazas")
        tabla.heading("eje",text="eje")
        tabla.heading("capacidad",text="capacidad")

        tabla.column("id", width=30)
        tabla.column("marca", width=150)
        tabla.column("color", width=150)
        tabla.column("modelo", width=150)
        tabla.column("velocidad", width=150)
        tabla.column("caballaje", width=150)
        tabla.column("plazas", width=150)
        tabla.column("eje", width=120)
        tabla.column("capacidad", width=120)

        datos=camiones.Camiones.consultar()
        if datos:
            for i in datos:
                tabla.insert("",END,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

        def seleccionar(event):
            item=tabla.selection()
            if item:
                valores=tabla.item(item)["values"]
                id.set(valores[0])
                marca.set(valores[1])
                color.set(valores[2])
                modelo.set(valores[3])
                velocidad.set(valores[4])
                caballaje.set(valores[5])
                plazas.set(valores[6])
                eje.set(valores[7])
                capacidad.set(valores[8])

        def limpiar():
            marca.set("")
            color.set("")
            modelo.set(0)
            velocidad.set(0)
            caballaje.set(0)
            plazas.set(0)
            eje.set(0)
            capacidad.set(0)

        tabla.bind("<<TreeviewSelect>>", seleccionar)

        tabla.grid(row=0,column=0,pady=10,padx=13)

        btnag=Button(frame3,text="Agregar",command=lambda:funciones.Funciones.regcamion(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),eje.get(),capacidad.get(),ventana)).grid(row=0,column=0,padx=5)
        btnac=Button(frame3,text="Actualizar",command=lambda:funciones.Funciones.actcamion(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),eje.get(),capacidad.get(),id.get(),ventana)).grid(row=0,column=1,padx=5)
        btnel=Button(frame3,text="Eliminar",command=lambda:funciones.Funciones.elicamion(id.get(),ventana)).grid(row=0,column=2,padx=5)
        btnbor=Button(frame3,text="Limpiar",command=limpiar).grid(row=0,column=3,padx=5)
        btnvolv=Button(frame3,text="Volver",command=lambda:self.menu_principal(ventana)).grid(row=0,column=4,padx=5)