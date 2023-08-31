def geometria (alto,ancho):
    area=alto*ancho
    return (area)

alto=int(input("ingrese el alto: "))
ancho=int(input("ingrese el ancho: "))

print("el area del rectangulo es: ", geometria(alto, ancho))