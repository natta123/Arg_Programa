def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def lista_primos (lista):
    listadeprimos=[]
    for n in lista:
        if is_prime(n):
            listadeprimos.append(n)
    return listadeprimos

lista=[4,5,6,7,8,9]
print(lista_primos(lista))