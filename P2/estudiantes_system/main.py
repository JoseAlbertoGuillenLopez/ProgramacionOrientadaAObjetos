from estudiantes import estudiante
import os

class App:
    def __init__(self):
        self.main()
        
    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\nPresiona ENTER para continuar...")

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t.. Ingresar los datos del estudiante :{tipo}")
        nombre=input("Nombre: ").upper()
        nota=float(input("Nota: "))
        return nombre, nota
    
    def menu_acciones(self, tipo):
        print(f"\n\t ..:: MENU DE {tipo} ::..")
        print("\n\t 1.-Insertar \n\t 2.-Consultar \n\t 3.-Actualizar \n\t 4.-Eliminar \n\t 5.-Regresar")
        opcion=input("\n\t Selecciona una opcion: ").upper().strip()
        return opcion
    
    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t\t...Accion realizada con éxito!...")
            self.esperarTecla()
        else:
            print("\n\t...No fue posible realizar la accion. Vuelva a intentar ...") 
            self.esperarTecla()
    
    def menu_estudiantes(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Estudiante")
            if opcion == '1':
                self.borrarPantalla()
                nombre,nota=self.datos_estudiante("estudiante")
                obj=estudiante.Estudiante(nombre,nota)
                respuesta=estudiante.Estudiante.insertar(obj.nombre,obj.nota)
                self.respuesta_sql(respuesta)

            elif opcion == '2':
                self.borrarPantalla()
                registros = estudiante.Estudiante.consultar()
                if registros:
                    for i in registros:
                        estado = "Reprobado " 
                        if i[2] >= 7:
                            estado= "Aprobado "
                        print(f"| ID: {i[0]:<10} | Nombre: {i[1]:<10} | Nota: {i[2]:<10} | {estado:<10} |")
                else:
                    print("\n\t No hay estudiantes registrados.")
                self.esperarTecla()

            elif opcion == '3':
                self.borrarPantalla()
                id = input("\t ID del estudiante: ")
                nombre,nota=self.datos_estudiante("estudiante")
                obj=estudiante.Estudiante(nombre,nota)
                respuesta=estudiante.Estudiante.actualizar(obj.nombre,obj.nota,id)
                self.respuesta_sql(respuesta)
                

            elif opcion == '4':
                self.borrarPantalla()
                id = input("\t ID del estudiante a eliminar: ")
                respuesta=estudiante.Estudiante.eliminar(id)
                self.respuesta_sql(respuesta)

            elif opcion == '5':
                break
            else:
                print("\n\t ... Opción no válida. Intenta de nuevo ...")
                self.esperarTecla()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Estudiante \n\t2.-Salir\n\t Elige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_estudiantes()
                    self.esperarTecla()
                case "2":
                    self.borrarPantalla()
                    input("\n\t\tSalir del Sistema")
                    opcion=False   
                case _:
                    input("Opcion invalidad ... vuelva a intertarlo ... ")      

if __name__ == "__main__":
    app = App()