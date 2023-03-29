def lista_numero (lista):
    numero= input("Ingrese numero: (Escriba salir para terminar): ")
    while numero!= "salir":
        lista.append(numero)
        numero= input("Ingrese numero: (Escriba salir para terminar): ")
    return lista

lista=[]
lista_numero(lista)
print (lista)