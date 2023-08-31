# Escribir una función lógica de dos parámetros enteros que devuelva True si uno divide al 
# otro y False en caso contrario

def divisible(num1,num2):

    if num1%num2==0:
        print ("true")

    else:
        print("false")

num1=int(input("ingrese el primer número: "))
num2=int(input("ingrese el segundo número: "))

divisible(num1,num2)