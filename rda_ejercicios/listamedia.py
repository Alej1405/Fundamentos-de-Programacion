print ("calculos estadisticos")
numeros_ingreso = input("ingrese los numero separados por coma, ejemplo (1,2,3): ")
numeros = numeros_ingreso.split(",")

suma = 0 
longitud = len(numeros)
for i in range(longitud): 
    numeros[i] = float(numeros[i])
    suma = suma + numeros[i]
print (numeros)
promedio = suma / longitud
print("el promedio es igual a: ", promedio)

#calculo de la mediana
numeros.sort()
posicion = int(longitud/2)
if longitud % 2 == 0 :
    #par
    med_1 = numeros[posicion] 
    med_2_p = posicion - 1
    med_2 = numeros[med_2_p]
    mediana = (med_1+med_2)/2
    print("mediana", mediana)
else:
    print("La mediana: ",numeros[posicion])
    #inpar