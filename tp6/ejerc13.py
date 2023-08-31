#  Escribir una función lógica vocal que determine si un carácter es una vocal.

def caracter(caract):
    if caract=="a" or caract=="e" or caract=="i" or caract=="o" or caract=="u":
        print("el caracter es una vocal")

    else:
        print("el caracter no es una vocal")

caract=(input("ingrese una caracter: "))

caracter(caract)