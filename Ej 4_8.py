def division (a,b):
    if b==0: 
        return "No se puede dividir por cero"
    else:
        return a/b

num=int(input("Ingrese numerador: "))
den=int(input("Ingrese denominador: "))

print(division(num,den))