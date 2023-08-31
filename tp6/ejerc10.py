# Escribir una función que tenga un parámetro de tipo entero y que devuelva la letra P si el 
# Nº es positivo y N si es negativo o cero.

def numero (num):

    if num>0:
        print("P")

    elif num<0:
     print("N")

    else:
       print("El número ingresado es 0")

num=int(input("ingrese un número: "))

numero (num)