def factorial(num1):
    fact = 1

    for i in range(1, num1+1):
        fact = fact * i

    return (fact)
    
num1=int(input("ingrese un numero: "))

print("el factorial es:", factorial(num1))