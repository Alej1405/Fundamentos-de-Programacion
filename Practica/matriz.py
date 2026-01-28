matriz = [['a','b','c'],['c','d','e'],['f','g','h']]

    

for fila in matriz:
    for elemento in fila:
        print(elemento)


longitud_m = len(matriz)
longitud_m_c = len(matriz[1])

for i in range(longitud_m):
    #print(matriz[i])
    for i in range(longitud_m_c):
        print(matriz[i][i])

