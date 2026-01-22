#ingresar 10 numeros, con los 5 primeros calcular el promedio y con los cinco restantes, la mediana.
numeros_ingreso = input("ingrese 10 numero separados por coma, ejemplo (1,2,3): ")
numeros = numeros_ingreso.split(",")

#ingresar al leng para dividir la lista en dos y que cada una tenga 5 numero
longitud = len(numeros)
division = int(longitud/2)


#calcular el promerio
suma = 0
for i in range(division):
    numeros[i] = float(numeros[i])
    suma = suma + numeros[i]
    print(f"Indice {i}: valor = {numeros[1]}")

promedio = suma / division
print("el promero es:",promedio)

#calculo de la mediana
numeros.reverse()
mediana = 3
numeros_m = []

for i in range(division):
    numeros_m.append(float(numeros[i]))

numeros_m.sort()
print(numeros_m)
print("La mediana: ",numeros[mediana])

#slicing recibe dos parametros : inicio en cero 5 nuermo hasta el numero de indice.

