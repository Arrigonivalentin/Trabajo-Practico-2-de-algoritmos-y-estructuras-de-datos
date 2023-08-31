# Escribir un procedimiento digito, que determine si un carácter es uno de los dígitos de o a 
# 9.
def determinar(x):
    if x>=0 and x<=9:
        print("el número se encuentra entre el 0 y el 9")
    else: print("el número no se encuentra entre el 0 y el 9")

x=float(input("ingrese un numero: "))

determinar(x)