# # datos estructuradoss
lista = [1,2,3,4,5]
print("Lista", lista)

lista.append(6)
print("Append", lista)

lista.extend([7,8])
print("Extend", lista)

# para insert hay que pasar posicion y valor a insertar
lista.insert(1, 1.5)
print("Insert", lista)

lista.remove(1.5)
print("Remove", lista)

# elimina el ultimo elmento de la lista y lo muestra
ultimo_elemento = lista.pop()
print("Pop", lista, "Ultimo elementos",ultimo_elemento)

# busca y muestra la posicion del valor que consultamos.
indice = lista.index(4)
print("Indice: ", indice)

conteo = lista.count(4)
print("Count: ", conteo)

# cambia el sentido de la lista, pero por default esta en false
lista.sort(reverse=True)
print("SortV: ", lista)

# revertir el orden a la lista
lista.reverse()
print("Reverse: ", lista)

#ordena sin crear una nueva lista.
lista.sort(reverse=False)
print("SortF: ", lista)

# revertir el orden a la lista
lista.reverse()
print("Reverse: ", lista)

# limpia la lista es decir borra el contenido
lista.clear()
print("Clear: ", lista)

lista = [1,2,3,4,5,6,7,8,9,0]

# inserta un elemento por el orden de lista.
lista[5] = 78
print("Insertar por posicion", lista)

#bucle for 
print("Lista: ")
for i in lista:
    print(i)