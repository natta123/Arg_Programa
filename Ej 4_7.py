a=int(input("Ingrese lado1: "))
b=int(input("Ingrese lado2: "))
c=int(input("Ingrese lado3: "))

if a==b==c:
    print("Triangulo equilatero")
elif a==b or a==c or b==c:
    print("Triengulo isosceles")
else:
    print("Triengulo escaleno")