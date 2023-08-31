#  Escribir un procedimiento que permita calcular la suma 1+2+3+ ... + n.
def sumaa(num):
    sum=0
    for i in range(1,num+1,1):
        sum=sum+i
    return(sum)


num=int(input("ingrese un número: "))
final=sumaa(num)
print("la suma es: ",final)