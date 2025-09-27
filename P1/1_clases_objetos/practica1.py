def sum(base,altura):
    suma=base*altura
    return suma

base=float(input("Tamaño de la base: "))
altura=float(input("Tamaño de la altura: "))
area=sum(base,altura)
print(f"El area del rectangulo es: {area}")




class Rectangulos:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    

base=float(input("Valor Base: "))
altura=float(input("Valor Altura: "))
rect1=Rectangulos(base,altura)
print(f"Area: {rect1.area()}")