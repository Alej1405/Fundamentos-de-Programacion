numeros = input("Ingresa numeros separados por un espacio:")
lista = numeros.split(",")
suma = 0
for i in lista:
    suma = suma + int(i)

print(suma)