# Programa principal
'''
Docstring para PracticaMatrices.IngresoMatriz
'''
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

'''
ingresamos la matriz por teclado
'''
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Ingrese el valor para posición [{i},{j}]: "))
        fila.append(valor)
    matriz.append(fila)

for i in matriz:
    print(i)