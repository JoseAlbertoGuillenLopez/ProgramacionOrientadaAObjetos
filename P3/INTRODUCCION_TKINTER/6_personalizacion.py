from tkinter import *

def hazclic():
    lbltit.config(background="green",foreground="red",width=50,height=4,font=("arial",30,"bold"),border=2,relief="groove",text="POO con Python")

def regersarclic():
    lbltit.config(background="light blue",foreground="dark blue",width=50,height=4,font=("helvetica",30,"italic"),border=2,relief="groove",text="Bienvenidos a Tkinter")

ventana=Tk()

ventana.geometry("500x500")
ventana.title("PERSONALIZAR WIDGETS")


lbltit=Label(ventana,text="Bienvenidos a Tkinter")
lbltit.config(background="light blue",foreground="dark blue",width=50,height=4,font=("helvetica",30,"italic"),border=2,relief="groove")
#foreground=color de letra
#with y heigh muy pequeños 1-50
# font con 3 parametros
lbltit.pack(pady=10)

btn_hazclick=Button(ventana,text="Haz Click Aqui")
btn_hazclick.config(foreground="white",activeforeground="yellow",width=15,font=("arial",20,"bold"),command=hazclic)
btn_hazclick.pack(pady=10)

btn_regresar=Button(ventana,text="Regresar Click Aqui")
btn_regresar.config(foreground="black",activeforeground="red",width=15,font=("arial",20,"bold"),command=regersarclic)
btn_regresar.pack(pady=10)

ventana.mainloop()