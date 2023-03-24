a=int(input("Ingrese nota primer parcial: "))
b=int(input("Ingrese nota segundo parcial: "))
c= (a+b)/2

if c >= 8:
    print(f"Usted esta promovido con {c}")
elif c < 8 and c >=4:
    print(f"Usted esta regular con {c}")
else:
    print(f"Usted esta libre con {c}")