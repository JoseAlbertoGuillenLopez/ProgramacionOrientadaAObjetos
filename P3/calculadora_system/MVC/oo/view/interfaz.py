'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en alerta
'''

from tkinter import *
from controller import funciones
from model import operaciones
from tkinter import messagebox

class vista:
    def __init__(self,ventana):
        ventana.geometry("600x600")
        ventana.resizable(False,False)
        ventana.title("CALCULADORA BASICA")
        self.interfaz(ventana)

    @staticmethod
    def menuprincipal(ventana):
        barra=Menu(ventana)
        ventana.config(menu=barra)
        OperacionesMenu=Menu(barra,tearoff=0) #0 o 1 tearoff
        barra.add_cascade(label="Operaciones", menu=OperacionesMenu)
        OperacionesMenu.add_command(label="Agregar",command=lambda: vista.interfaz(ventana))
        OperacionesMenu.add_command(label="Consultar",command=lambda: vista.mostar_screen(ventana)) 
        OperacionesMenu.add_command(label="Actualizar",command=lambda: vista.actuallizar_dag1(ventana))   #vista.actualizar_screen(ventana)
        OperacionesMenu.add_command(label="Eliminar",command=lambda: vista.eliminar_screen(ventana)) 
        OperacionesMenu.add_separator()
        OperacionesMenu.add_command(label="Salir",command=ventana.quit) #destruye todo el programa

    @staticmethod
    def borrar_pantalla(ventana):
        for i in ventana.winfo_children():
            i.destroy()
    
    @staticmethod
    def interfaz(ventana):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)

        op1=IntVar()
        op2=IntVar()

        caja1=Entry(ventana,textvariable=op1,width=5,justify="right")
        caja1.focus()
        caja1.pack(pady=10,anchor="center",side="top")

        caja2=Entry(ventana,textvariable=op2,width=5,justify="right")
        caja2.pack(pady=10,anchor="center",side="top")



        btn1=Button(ventana,text="+",command=lambda:funciones.funcionesc.resultado(op1.get(),op2.get(),"SUMA","+"))
        btn1.pack(pady=5)
        btn2=Button(ventana,text="-",command=lambda:funciones.funcionesc.resultado(op1.get(),op2.get(),"RESTA","-"))
        btn2.pack(pady=5)
        btn3=Button(ventana,text="x",command=lambda:funciones.funcionesc.resultado(op1.get(),op2.get(),"MULTIPLICACION","*"))
        btn3.pack(pady=5)
        btn4=Button(ventana,text="/",command=lambda:funciones.funcionesc.resultado(op1.get(),op2.get(),"DIVISION","/"))
        btn4.pack(pady=5)


        btn5=Button(ventana,text="SALIR",command=ventana.destroy)
        btn5.pack(pady=5) 

    @staticmethod 
    def eliminar_screen(ventana):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Borrar una Operacion::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID de la operacion: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Eliminar",command=lambda:funciones.funcionesc.eliminar(id.get()))
        btneli.pack(pady=5)
        btnvol=Button(ventana,text="Volver",command=lambda:vista.interfaz(ventana))
        btnvol.pack(pady=5)

    @staticmethod
    def mostar_screen(ventana):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)
        lbltit=Label(ventana,text=".:: Listado de la Operaciones ::.")
        lbltit.pack(pady=10)
        lblmos=Label(ventana)
        res=funciones.funcionesc.mostrar()
        lblmos.config(text=f"{res}")
        lblmos.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:vista.interfaz(ventana))
        btnvolv.pack()

    @staticmethod
    def actuallizar_dag1(ventana):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)
        lbltit=Label(ventana,text=".:: Cambiar una Operacion ::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text="ID de la operacion: ")
        lblind.pack(pady=5)
        id=IntVar()
        caja0=Entry(ventana,textvariable=id,width=5,justify="right")
        caja0.focus()
        caja0.pack(pady=5)


        btngua=Button(ventana,text="Checar ID",command=lambda:funciones.funcionesc.checar_actualizacion(id.get(),ventana))       
        btngua.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:vista.interfaz(ventana))
        btnvolv.pack(pady=10)
    
        #cambiiar menu principal a la otra y en operaciones quitar el rowcount   
    
    @staticmethod
    def actuallizar_dag(n1,n2,sig,resul,id,ventana):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)
        lbltit=Label(ventana,text=".:: Cambiar una Operacion ::.")
        lbltit.pack(pady=5)

        num1=IntVar()
        num2=IntVar()
        simb=StringVar()
        res=DoubleVar()
        idl=IntVar()

        num1.set(n1)
        num2.set(n2)
        simb.set(sig)
        res.set(resul)
        idl.set(id)


        
        caja0=Entry(ventana,textvariable=idl,width=5,justify="right",state="readonly")
        caja0.pack(pady=5)

        lblnum1=Label(ventana,text="Número 1:")
        lblnum1.pack(pady=5)
        caja1=Entry(ventana,textvariable=num1,width=6,justify="right")
        caja1.focus()
        caja1.pack(pady=5)
        lblnum2=Label(ventana,text="Número 2:")
        lblnum2.pack(pady=5)
        caja2=Entry(ventana,textvariable=num2,width=6,justify="right")
        caja2.pack(pady=5)
        lblsimb=Label(ventana,text="Signo:")
        lblsimb.pack(pady=5)
        caja3=Entry(ventana,textvariable=simb,width=6,justify="center")
        caja3.pack(pady=5)
        lblres=Label(ventana,text="Resultado:")
        lblres.pack(pady=5)
        caja4=Entry(ventana,textvariable=res,width=6,justify="right")
        caja4.pack(pady=10)

        btngua=Button(ventana,text="Guardar",command=lambda:funciones.funcionesc.enviar_actualizacion(num1.get(),num2.get(),simb.get(),res.get(),idl.get()))       
        btngua.pack(pady=5)
        btnvolv=Button(ventana,text="Volver",command=lambda:vista.interfaz(ventana))
        btnvolv.pack(pady=10)
    
        #cambiiar menu principal a la otra y en operaciones quitar el rowcount   

    












    @staticmethod
    def actualizar_screen(ventana):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)
        id=StringVar()
        lblind=Label(ventana,text="Ingresa el id de la operacion a modificar")
        lblind.pack(pady=5)
        caja1=Entry(ventana,textvariable=id,width=5)
        caja1.focus()
        caja1.pack(pady=5)
        btnenv=Button(ventana,text="Actualizar",command=lambda:funciones.funcionesc.check(id.get(),ventana))
        btnenv.pack()
        
        btnvolv=Button(ventana,text="Volver",command=lambda:vista.interfaz(ventana))
        btnvolv.pack(pady=10)
    
    @staticmethod
    def actualizar_screen2(ventana,respuesta):
        vista.borrar_pantalla(ventana)
        vista.menuprincipal(ventana)

        num1=StringVar()
        num2=StringVar()
        simb=StringVar()
        res=StringVar()

        lbltit=Label(ventana,text="Introduce los nuevos cambios")
        lbltit.pack(pady=5)

        caja1=Entry(ventana,textvariable=num1,width=6)
        caja1.insert(0,respuesta[2])
        caja1.focus()
        caja1.pack(pady=5)
        caja2=Entry(ventana,textvariable=num2,width=6)
        caja2.insert(0,respuesta[3])
        caja2.pack(pady=5)
        caja3=Entry(ventana,textvariable=simb,width=6)
        caja3.insert(0,respuesta[4])
        caja3.pack(pady=5)
        caja4=Entry(ventana,textvariable=res,width=6)
        caja4.insert(0,respuesta[5])
        caja4.pack(pady=5)

        btnenv=Button(ventana,text="Actualizar",command=lambda:funciones.funcionesc.enviar_actualizacion(num1.get(),num2.get(),simb.get(),res.get(),respuesta[0]))
        btnenv.pack()
        btnvolv=Button(ventana,text="Volver",command=lambda:vista.interfaz(ventana))
        btnvolv.pack(pady=10)



#voy a tener una interfaz para cada CRUD la que se llama interfaz en realidad es interfaz
#una sola clase con cada interfaz (pantallas o ventanas) en un metodo 
# Radiobutton(ventana, text="+", variable=simb, value="+").pack()
