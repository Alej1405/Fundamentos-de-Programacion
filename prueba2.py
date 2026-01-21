
print("calculos estadisticos")
numeros_ingreso = input("ingrese los numeros separados por coma, ejemplo (1,2,3): ")

numeros = numeros_ingreso.split(",")

suma = 0
longitud = len(numeros)

for i in range(longitud):
    numeros[i] = float(numeros[i])
    suma = suma + numeros[i]

print(numeros)

promedio = suma / longitud
print("el promedio es igual a:", promedio)

# REDONDEO SIN LIBRERÍAS (0.5 SUBE)
promedio_redondeado = int(promedio + 0.5)

print("promedio redondeado:", promedio_redondeado)
