nombre=input("ingrese el nombre del primer socio: ")
nombre2=input("ingrese el nombre del segundo socio: ")
edadsoc1=int(input("ingrese la edad del primer socio:"))
edadsoc2=int(input("ingrese la edad del segundo socio: "))
direccionsoc1=input("ingrese la direccion del primer socio: ")
direccionsoc2=input("ingrese la direccion del segundo socio: ")

if edadsoc1<edadsoc2:
    print("datos del primer socio:",nombre,",",edadsoc1,"años,",direccionsoc1)
else:
    print("datos del segundo socio:",nombre2,",",edadsoc2,"años,",direccionsoc2)