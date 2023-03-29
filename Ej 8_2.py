nota = int(input("Ingrese una nota: "))
suma=0
cant=0
while nota != -1:
    suma= suma + nota
    cant= cant + 1
    nota = int(input("Ingrese una nota: "))

promedio= suma /cant
print (f"Su promedio es {promedio}") 