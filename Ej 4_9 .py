a=input("Ingrese caracteres: ")

def funcion (a):
    if a.isdigit():
        print(f"{a} es numerico")
    elif a.isalpha():
        print(f"{a} es lafebetico")
    elif a.isalnum():
        print(f"{a} es alfanumerico")

funcion (a)