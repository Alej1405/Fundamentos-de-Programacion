tupla = (1,2,3,4,5,45,6,4,6,3,36,34,86)
print("Tupla: ", tupla)

conte_tupla = tupla.count(6)
print("Conteo tupla: ", conte_tupla)

indice_tupla = tupla.index(45)
print("Indece tupla: ", indice_tupla)

print("imprimir por posicion: ", tupla[5])

# tupla[5] = 25
# print("Insertar por posicion: ", tupla)

# solo genera desde el 0 al cinco
lista = list(range(5))
print("Range: ", lista)

# inicia desde el 1
lista = list(range(1,5))
print("Range: ", lista)

lista = list(range(1,6))
print("Range: ", lista)

# genera impares
lista = list(range(1,20,2))
print("Range: ", lista)

# genera paras
lista = list(range(2,20,2))
print("Range: ", lista)

# invertir aclarar que resta el nuemro
lista = list(range(5,1,-1))
print("Range: ", lista)

lista = [12,2,23,4,2,12,3,4,2314,12,12,2,2,12]

longitud = len(lista)
print("longitud de la lista: ", longitud)

print("lista")
for i in range(longitud):
    print(lista[i])
