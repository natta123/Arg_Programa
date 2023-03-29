num= input("Ingrese un numero: ")

while not (num.isdecimal()) or not (int(num) in range (1,101)):
    if not (num.isdecimal()):
        print("Ingrese un numero: ")
    elif  not (int(num) in range (1,101)):
        print("Ingrese un numero en el rango correcto")
    num= input("Ingrese una nota: ")

print(f"{num} es valido. Gracias")