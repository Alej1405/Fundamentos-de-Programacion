#-*-utf-8-*

'''
Docstring para Practica.practicaMatriz
'''
matriz = [[1, 3, 4, 5],
        [2, 2, 3, 4],
        [3, 3, 4, 3],
        [4, 5, 5, 2]]

long_fila = len(matriz)

for fila in range(long_fila):
    long_columna = len(matriz[1])
    for columna in range(long_columna):
        #print(matriz[fila][columna])
        if matriz[fila][columna] %2 > 0:
            matriz[fila][columna] = matriz[fila][columna] + 1 

print ("Matriz modificada")
for fila in matriz:
    print(fila)