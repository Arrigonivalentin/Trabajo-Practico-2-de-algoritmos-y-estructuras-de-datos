# Escribir una función que dados 2 números, calcule el porcentaje que el primero representa 
# respecto del segundo.

def porcentaje(num1,num2):
    total=num1*100
    porcentajee=total/num2
    return(porcentajee)
    
num1=float(input("ingrese el primer número: "))
num2=float(input("ingrese el segundo número: "))


print ("el porcentaje que representa el primero respecto al segundo es del",porcentaje(num1,num2),"%")
