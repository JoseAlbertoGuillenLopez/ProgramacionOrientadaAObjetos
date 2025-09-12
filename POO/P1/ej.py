def sum(base,altura):
    suma=base*altura
    return suma

base=float(input("Tamaño de la base: "))
altura=float(input("Tamaño de la altura: "))
area=sum(base,altura)
print(f"El area del rectangulo es: {area}")