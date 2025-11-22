import tkinter as tk

ventana=tk.Tk()#creo objeto del arhcivo tk de la clase TK
ventana.title("Uso de Frame o Marcos")
ventana.geometry("800x600")

marco=tk.Frame(ventana,width=300,height=200,background="peru",borderwidth=2,relief="solid") #solid black con border
marco.pack_propagate(False) #para que no se ajusten los frames superiorres y pongo en pack otra vez
marco.pack(pady=200)
#marco.place(x=100,y=200) para mover los frames es place o pack con pady y padx
marco2=tk.Frame(marco,width=200,height=100,background="sienna",borderwidth=2,relief="sunken")#dentro de marco
marco2.pack(pady=50, padx=50)


ventana.mainloop()