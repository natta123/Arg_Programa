print("Convierte medidas inglesas a metros: ")
print("Que unidad desea convertir? ")
opc= int (input ("Ingrese opcion: \n 1-Millas \n 2-Pies \n 3-Pulgadas \n"))
millas= float(1609.344)
pie= float (0.3048)
pulgada= float(0.0254)
medida= float(0.0)
medida2= float(0.0)
if opc==1:
    medida= float(input("Ingrese millas: "))
    medida2= medida*millas
    print (medida, " millas son: ", medida2, " metros")
if opc==2:
    medida= float(input("Ingrese millas: "))
    medida2= medida*pie
    print (medida, " pies son: ", medida2, " metros")
if opc==3:
    medida= float(input("Ingrese millas: "))
    medida2= medida*pulgada
    print (medida, " pulgada son: ", medida2, " metros")
if opc!=1 and opc!=2 and opc!=3:
    print("ingrese una opcion correcta: ")
    
print("Nada mas")
