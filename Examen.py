"""def contarMS (cadena):
    cadena= cadena.lower()
    contador=0
    for i in cadena:
        if i== "s" or i=="m":
            contador= contador +1
    return contador

print( contarMS("mamas"))"""

"""def minimo(lista):
    min=min(lista)
    return min   

lista=[3,5,2,-1,8,9,4]

print(min(lista))"""

"""def promedio(lista):
    suma=0
    cont=0
    prom=0
    for i in lista:
        if i != -1:
            suma= suma + i
            cont= cont + 1
        elif i==-1:
            break
    prom= suma / cont
    prom= round(prom,2)
    return prom

lista=[2,3,2,-1,8,8,8,8,1000]

print (promedio(lista))"""

# Escribir una función que reciba dos números enteros positivos
# y retorne la suma de los dígitos de su resta. 
# Ayuda un int se puede pasar a str y viceversa
# Ejemplo 627 y 246 (627-246=381) retornaría 12 (3+8+1)
# Ejemplo 127 y 673 (673-127=546) retornaría 15 (5+4+6)

def suma_digitos(n1,n2):
    resta=0
    suma=0
    if n1>n2:
        resta=n1-n2
    elif n2>n1:
        resta=n2-n1
    resta= str(resta)
    restalist=list (resta)
    
    for i in restalist:
        suma= suma + int(i)
        
    return suma

print(suma_digitos(30,100))