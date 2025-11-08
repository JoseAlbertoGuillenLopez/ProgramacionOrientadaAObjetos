import tkinter as tk

ventana=tk.Tk()
ventana.title("MAINLOOP")
ventana.geometry("800x600")

marco=tk.Frame(ventana)
marco.config(width=600,height=400,background="#1EDE9B", border=100, relief="raised") #para configurar fuera de la linea
marco.pack(side="bottom",anchor="center") #side lados , achor otros

ventana.mainloop()