from tkinter import *

def entrar():
    lbl_resultado.config(text=f"BIENVENDIO... {txt_nombre.get()}",background="red")

def borrar():
    lbl_resultado.config(text="")
    txt_nombre.delete(0,END)
    txt_password.delete(0,END)
    txt_nombre.focus()
    #lbl_resultado.destroy()

    #limpiar inputs xt_password.delete(0,END)
    #obtener valor de input txt_nombre.get()

def salir():
    ventana.quit()
    #quit destruye




ventana=Tk()

ventana.geometry("800x600")
ventana.title("ENTRY")


lbltit=Label(ventana,text="ACCESO AL SISTEMA")
lbltit.config(background="light blue",foreground="dark blue",width=50,height=4,font=("helvetica",30,"italic"),border=2,relief="groove")
#foreground=color de letra
#with y heigh muy pequeños 1-50
# font con 3 parametros
#show="*" en entry para ****

lbltit.pack()


marco_principal=Frame(ventana,width=800,height=300)
marco_principal.pack()

lbl_nombre=Label(marco_principal,text="INGRESE EL NOMBRE:")
lbl_nombre.grid(row=0,column=0,padx=5,pady=5)
lbl_password=Label(marco_principal,text="INGRESE LA CONTRASEÑA:")
lbl_password.grid(row=1,column=0,padx=5,pady=5)

#nombre y txt_nombre son el mismo objeto
nombre=StringVar()
txt_nombre=Entry(marco_principal,width=30,textvariable=nombre)
txt_nombre.focus()
#cursor parpadeando
txt_nombre.grid(row=0,column=1,padx=5,pady=5)

txt_password=Entry(marco_principal,width=30,show="*")
txt_password.grid(row=1,column=1,padx=5,pady=5)



marco_botones=Frame(ventana,width=800,height=100)
marco_botones.pack()

btn_entrar=Button(marco_botones,text="ENTRAR",command=entrar)
btn_entrar.grid(row=0,column=0,padx=5,pady=5)

btn_borrar=Button(marco_botones,text="BORRAR",command=borrar)
btn_borrar.grid(row=0,column=1,padx=5,pady=5)

btn_salir=Button(marco_botones,text="SALIR",command=salir)
btn_salir.grid(row=0,column=2,padx=5,pady=5)

#etiqueta bienvenido y quien entro


lbl_resultado=Label(ventana,text="")
lbl_resultado.pack(pady=10)

ventana.mainloop()