from coches import * #es como copiar y pegar en este archivo  
#import coches agarro todo el archivo
#coche1=coches.Coches("VW","Blanco","2022",220,150,5)
import os


#solicitar los datos que posteriormente seran los atributos del objeto

def autos():
    print(f"\n\t...Datos del Vehiculo...")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo del auto: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa las plazas: "))

    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"\n\tDatos del Coche: \n Marca:{coche.marca} \n Color: {coche.color} \n Modelo: {coche.modelo} \n Velocidad: {coche.velocidad} \n Caballaje: {coche.caballaje} \n Plazas: {coche.plazas} ")

def camionetas():
    print(f"\n\t...Datos del Vehiculo...")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa las plazas: "))
    traccion=input("Ingresa la traccion: ").upper()
    cerrada=input("Ingresa SI/NO si es cerrada: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False


    coche=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    print(f"\n\tDatos de la camioneta: \n Marca:{coche.marca} \n Color: {coche.color} \n Modelo: {coche.modelo} \n Velocidad: {coche.velocidad} \n Caballaje: {coche.caballaje} \n traccion: {coche.traccion} \n cerrada: {coche.cerrada} ")

def camiones():
    print(f"\n\t...Datos del Vehiculo...")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa las plazas: "))
    eje=int(input("Ingresa el numero de ejes: "))
    capacidadCarga=int(input("Ingresa la capacidad de carga: "))

    coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    print(f"\n\tDatos del camion: \n Marca:{coche.marca} \n Color: {coche.color} \n Modelo: {coche.modelo} \n Velocidad: {coche.velocidad} \n Caballaje: {coche.caballaje} \n Ejes: {coche.eje} \n Capacidad carga: {coche.capacidadCarga} ")



op="1"
while op!="4":
    os.system("cls")
    op=input("\n\t\t.::Menu Principal::.\n\t\n \t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige una opcion: ").lower().strip()
    match op:
        case "1": 
            os.system("cls")
            print("\n\tAutos")
            autos()
            input("Oprima tecla para continuar")
        case "2":
            os.system("cls")
            print("\n\tCamionetas")
            camionetas()
            input("Oprima tecla para continuar")
        case "3":
            os.system("cls")
            print("\n\tCamiones")
            camiones()
            input("Oprima tecla para continuar")
        case "4":
            input("\n\tSalir del sistema")
        case _:
            input("\n\tOpcion invalida... intente de nuevo...")
            







'''coche1=Coches("VW","Rojo","2020",200,160,4)
print(coche1.color, coche1.acelerar())

camion1=Camiones("VW","Blanco","2020",210,170,4,2,2500)
print(camion1.color, camion1.acelerar())

camioneta1=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)
print(camioneta1.color, camioneta1.acelerar())
'''

'''#Crear un objetos o instanciar la clase

coche1=Coches("VW","Blanco","2022",220,150,5)
coche1.num_serie=("hw78cwe") #se pueden agregar mas atributos que no esten en el init pero se tienen que llenar los campos del contructir antes
print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")


coche2=Coches("Nissan","Azul","2020",180,150,6)
print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")
#Segunda palabra de una funcion en mayusculas


#con decoradores
coche3=Coches("Honda","","",0,0,0)
print(f"Datos del Vehiculo: \n Marca: {coche3.marca2}")

coche4=Coches("Honda","","",0,0,0)
coche4.marca2="Volvo"
print(f"Datos del Vehiculo: \n Marca: {coche4.marca2}")'''

