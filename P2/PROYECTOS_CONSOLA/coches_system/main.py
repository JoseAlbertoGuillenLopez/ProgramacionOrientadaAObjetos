#Instanciar los objetos para posterior implementarlos 
from model import coches
from model import cochesBD
#from model.coches import *
import os

def borraPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t\t Oprime tecla para continuar")

def res(respuesta):
    if respuesta:
        print("\n\t...Accion realizada con exito...")
    else:
        print("\n\t..No fue posible realizar la accion, vuela a intentarlo....")
    esperarTecla()

def datos_autos(tipo):
    borraPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    borraPantalla()
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n Color: {color} \n Modelo: {modelo} \n Velocidad: {velocidad} \n Caballaje: {potencia} \n Plazas: {plazas}")

def menu_acciones(tipo):
    print(f"\n\t\t .:: Menu de {tipo}::. \n\t1.-Insertar\n\t2.-Consultar\n\t3.-Actualizar\n\t4.-Eliminar\n\t5.-Regresar\n\tElige un opción:")
    opcion=input("\n\t\t Elige una opcion: ").upper().strip()
    return opcion


def menu_autos():
    while True:
        borraPantalla()
        opcion=menu_acciones("AUTOS")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,potencia,plazas=autos()
            #Agregar registro a la BD
            auto=cochesBD.Autos(marca,color,modelo,velocidad,potencia,plazas)
            respuesta=auto.insertar()
            res(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            borraPantalla()
            registros=cochesBD.Autos.consultar()
            if registros:
                num_autos=0
                borraPantalla()
                print(F"{'AUTO #':<13}{'ID':<13}{'MARCA':<13}{'COLOR':<13}{'MODELO':<13}{'VELOCIDAD':<13}{'CABALLAJE':<13}{'PLAZAS':<13}")
                for i in registros:
                    num_autos=num_autos+1
                    print(F"{num_autos:<13}{i[0]:<13}{i[1]:<13}{i[2]:<13}{i[3]:<13}{i[4]:<13}{i[5]:<13}{i[6]:<13}")
                esperarTecla()
            else:
                print("\n\t\t...No hay vehiculos que mostrar...")
                esperarTecla()
            
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borraPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,potencia,plazas=autos()
            respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,potencia,plazas,id)
            res(respuesta)
        elif opcion=="4" or opcion=="ELIMINAR":
            borraPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Autos.eliminar(id)
            res(respuesta)
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            input("Opcion invalida ... vuelva a intertarlo ... ")     

def menu_camionetas():
    while True:
        borraPantalla()
        opcion=menu_acciones("CAMIONETAS")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada=camionetas()
            #evita crear constuctor y objetos
            respuesta=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
            res(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            mostrar=cochesBD.Camionetas.consultar()
            if mostrar:
                num_camioneta=0
                borraPantalla()
                print(F"{'CAMIONETA#':<13}{'ID':<13}{'MARCA':<13}{'COLOR':<13}{'MODELO':<13}{'VELOCIDAD':<13}{'CABALLAJE':<13}{'PLAZAS':<13}{'TRACCION':<13}{'CERRADA':<13}")
                for i in mostrar:
                    num_camioneta+=1
                    print(F"{num_camioneta:<13}{i[0]:<13}{i[1]:<13}{i[2]:<13}{i[3]:<13}{i[4]:<13}{i[5]:<13}{i[6]:<13}{i[7]:<13}{i[8]:<13}")
                esperarTecla()
            else:
                borraPantalla()
                print("No hay vehiculos que mostrar")
                esperarTecla()  
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borraPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada=camionetas()
            respuesta=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id)
            res(respuesta)
        elif opcion=="4" or opcion=="ELIMINAR":
            borraPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Camionetas.eliminar(id)
            res(respuesta)
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            input("Opcion invalida ... vuelva a intertarlo ... ")  

def menu_camiones():
    while True:
        borraPantalla()
        opcion=menu_acciones("CAMIONES")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga=camiones()
            #evita crear constuctor y objetos
            respuesta=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
            res(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            mostrar=cochesBD.Camiones.consultar()
            if mostrar:
                num_camiones=0
                borraPantalla()
                print(F"{'CAMION #':<13}{'ID':<13}{'MARCA':<13}{'COLOR':<13}{'MODELO':<13}{'VELOCIDAD':<13}{'CABALLAJE':<13}{'PLAZAS':<13}{'TRACCION':<13}{'CERRADA':<13}")
                for i in mostrar:
                    num_camiones+=1
                    print(F"{num_camiones:<13}{i[0]:<13}{i[1]:<13}{i[2]:<13}{i[3]:<13}{i[4]:<13}{i[5]:<13}{i[6]:<13}{i[7]:<13}{i[8]:<13}")
                esperarTecla()
            else:
                borraPantalla()
                print("No hay vehiculos que mostrar")
                esperarTecla()  
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borraPantalla()
            id=input("Ingrese el ID a actualizar: ").strip()
            marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga=camiones()
            respuesta=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga,id)
            res(respuesta)
        elif opcion=="4" or opcion=="ELIMINAR":
            borraPantalla()
            id=input("Ingrese el ID a eliminar: ").strip()
            respuesta=cochesBD.Camiones.eliminar(id)
            res(respuesta)
        elif opcion=="5" or opcion=="REGRESAR":
            break
        else:
            input("Opcion invalida ... vuelva a intertarlo ... ")  


def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    borraPantalla()
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f" Traccion: {coche.traccion}\n Cerrada: {coche.cerrada}")
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f" #Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga


def main():
    opcion=True
    while opcion:
        borraPantalla()
        opcion=input("\n\t\t .:: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
        match opcion:
            case "1":
                menu_autos()
                esperarTecla()
            case "2":
                menu_camionetas()
                esperarTecla()  
            case "3":
                menu_camiones()
                esperarTecla()
            case "4":
                borraPantalla()
                input("\n\tSalir del Sistema")
                opcion=False   
            case _:
                input("Opcion invalida ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    main()


