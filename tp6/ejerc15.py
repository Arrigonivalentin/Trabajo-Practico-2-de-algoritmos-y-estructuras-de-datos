#  Escribir un procedimiento tipo calculadora donde se le da como entrada dos números y el 
# tipo de operación y esta devuelve el resultado.

def calculadora(num1,sum2):
    if op=="*":
     print("El resultado es:",num1*num2)

    elif op=="/" and num2!=0:
     print("El resultado es: ",num1/num2)

    elif op=="/" and num2==0:
     print("no se puede dividir por cero")

    elif op=="+":
     print("El resultado es: ",num1+num2)

    elif op=="-":
     print("El resultado es: ",num1-num2)


op=input("ingrese el tipo de operacion que desea hacer (*, /, +, -): ")

num1=float(input("ingrese el primer número: "))

num2=float(input("ingrese el segundo número: "))

calculadora(num1,num2)