# diccionarios

diccionario = {"nombre":"Ana", "edad":"25", "ciudad":"Quito"}

# para acceder al valor lo hacemos por medio de la clave
edad = diccionario.get("edad")
print("Get: ", edad)

# muestra todas las claves disponibles en el sistema
claves = diccionario.keys()
print("Keys: ", claves)

# muestra los valores de todos los diccionarios
valores = diccionario.values()
print("Values: ", valores)

# imprimir un recorrido de clave y valor
items = diccionario.items()
print("Items: ", items)

diccionario.update({"edad":"26", "pais":"Ecuador"})
print("Update: ", diccionario)

edad_eliminada = diccionario.pop("edad")
print("pop: ", diccionario, " Edad Eliminada", edad_eliminada)

ultimo_item = diccionario.popitem()
print("Pop item: ", diccionario)
print("Ultimo elemento: ", ultimo_item)

ciudad = diccionario.setdefault("ciudad","cuenca")
print("Setdefault: ", ciudad)

pais = diccionario.setdefault("pais","otro")
print("Diccionario: ", diccionario)
print("setdefault: ", pais)

diccionario.clear()
print("clear: ", diccionario)