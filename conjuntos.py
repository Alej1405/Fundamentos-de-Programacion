conjunto = { 1,2,3,3,4,5}
print("Conjunto: ", conjunto)

# agregar un elemento al conjunto
conjunto.add(6)
print("Add: ", conjunto)

# el valor tiene que existir
conjunto.remove(3)
print("Remove: ", conjunto)

# lo descarta si el valor existe, sino existe no hay error
conjunto.discard(10)
print("Discard(inexistente): ", conjunto)

elemento = conjunto.pop()
print("Conjunto Pop: ", conjunto)
print("Pop: ", elemento)

conjunto1 = {5,3,4,3,231,23,123}
print("conjunto: ", conjunto1)
union_conjuntos = conjunto.union(conjunto1)
print("Union: ", union_conjuntos)

print("conjunto1: ", conjunto1)
interseccion = conjunto.intersection(conjunto1)
print("Interseccion: ", interseccion)

# elimina todos los elementos del conjunto 1 incluyendo la interseccion
diferencia = conjunto.difference(conjunto1)
print("Difference: ", diferencia)

# elimina solo la interseccion
diferencia_simereica = conjunto.symmetric_difference(conjunto1)
print("Symmetric.difference: ", diferencia_simereica)

# verifica si es un subconjutno de; regresa boolean
es_subconjunto = conjunto.issubset(union_conjuntos)
print("Issubset: ", es_subconjunto)

# verifica si es el conjunto abarca todo; resultad boolean
es_superconjunto = union_conjuntos.issuperset(conjunto)
print("Issuperset: ", es_superconjunto)

conjunto.clear()
print("Clear: ", conjunto)
