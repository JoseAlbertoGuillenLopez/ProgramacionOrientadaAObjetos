from tkinter import *

def cambiarTexto():
    mensajeCambiante.config(text="Texto cambiado")


def volverTexto():
    mensajeCambiante.config(text="Texto original")

def ventananeuv():
    ventana2=Toplevel()
    ventana2.geometry("200x200")
    ventana2.title("ventana 2")

    labeltxt=Label(ventana2,text="Bienvenido JOSE",background="peru").pack()
    #ventana2.mainloop() #solo un mainloope en todo el programa y solo un tk, otra ventana con toplevel


ventana=Tk()

ventana.geometry("800x600")
ventana.title("USO DE BOTONES")

frame_principal=Frame(ventana)
frame_principal.config(background="red",width=800,height=50, border=2, relief="solid")
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

Lable_titulo=Label(frame_principal,text="USO DE BOTONES")
Lable_titulo.config(background="red",width=20)
Lable_titulo.pack(pady=10)


mensajeCambiante=Label(ventana,text="Texto original")
mensajeCambiante.pack(pady=10)

boton_cambiar=Button(ventana,text="cambiar texto",command=cambiarTexto).pack(pady=10)
boton_regresar=Button(ventana,text="regresar texto",command=volverTexto).pack(pady=30)

marcouser=Frame(ventana,width=200, height=130,background="blue")
marcouser.pack_propagate(False)
marcouser.pack()

label_user=Label(marcouser,text="USUARIO: JOSE").pack(pady=10)
label_pass=Label(marcouser,text="PASSWORD: *****").pack(pady=10)

boton_cuenta=Button(marcouser,text="Iniciar Sesion",command=ventananeuv).pack(pady=10)
#se maanda a llamar la funcion sin los ()
#pad dentro de pad para margin, dentro del objeto para pad de verdad



ventana.mainloop()