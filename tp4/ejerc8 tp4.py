num1=int(input("ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("ingrese el tercer numero: "))
if num1>num2 and num1>num3:
    print(num1,"es el mayor")
elif num2>num1 and num2>num3:
 print(num2,"es el mayor")
else:
 print(num3,"es el mayor")