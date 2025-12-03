'''
commit_01_12_25

1ER DICIEMBRE

1) Implementacion de MVC
2) POO
3) INTERFACES: 
    3.1 menu_principal()
    3.2 menu_acciones()
    3.3 insertar_autos()
    3.4 consultar_autos()
    3.5 cambiar_autos()
    3.6 eliminar_autos()

    Productos entregables: 
    *Estructura del proyecto
    *Modulo principal main
    *Interaccion con interfaces

2 DICIEMBRE
    1) Interfaces
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()
    
    Productos Entregables
        ** Interacción con todas las interfaces
        ** Nombre del Commit: "commit_02_12_25"

3 DICIEMBRE
    1) CONTROLADOR:
        1.1 menu_principal()
        1.2 menu_acciones()
        1.3 insertar_autos()
        1.4 consultar_autos()
        1.5 cambiar_autos()
        1.6 borrar_autos()
        
    
    Productos Entregables
        ** Interacción con la funcionalidad (controlador) de las interfaces anteriores
        ** Nombre del Commit: "commit_03_12_25 "

    

'''
from tkinter import *
from view import view1

class APP:
    def __init__(self,ventana):
        view=view1.View(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=APP(ventana)
    ventana.mainloop() 


'''git remote add origin https://github.com/JoseAlbertoGuillenLopez/.git 
git push -u origin main'''