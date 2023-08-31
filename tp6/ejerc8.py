max=3

def descuentos(precio,unidades):
    if unidades>= max:
        desc=precio*unidades * 0.2
        print("se dencontaron $",desc)
    else:
        print("no cumple con el monto minimo de unidades")

precio=int(input("ingrese el precio del producto: "))
unidades=int(input("ingrese la cantidad de unidades: "))

descuentos(precio,unidades)