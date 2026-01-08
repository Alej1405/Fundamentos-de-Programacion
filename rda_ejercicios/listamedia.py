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
    #inpar
    print("La mediana: ",numeros[posicion])

#calculo de la moda
moda = max(numeros, key=numeros.count)
frecuencia = numeros.count(moda)

if moda > 1 :
    print("la moda es: ", moda)
    print("la frecuencia es: ", frecuencia)
else:
    print("no hay moda")

modas = [x for x in set(numeros) if numeros.count(x)==frecuencia ]

print("moda: ", modas)

maximo = 1 
moda = []
for num in numeros:
    conteo = numeros.count(num)
    if conteo >= maximo:
        if num in moda:
            pass
        else:
            moda.append(num)
        maximo = conteo
moda.reverse()
moda.pop()
if maximo > 1: 
    print("Moda: ",moda)
else:
    print("no hay moda")
