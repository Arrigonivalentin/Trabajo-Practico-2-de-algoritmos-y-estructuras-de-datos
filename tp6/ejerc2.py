def perimetro (num1,num2):
    peri=num1*2+num2*2
    return (peri)

num1=int(input("ingrese el lado 1: "))
num2=int(input("ingrese el lado 2: "))

print("el perimetro del rectangulo es: ", perimetro(num1,num2))