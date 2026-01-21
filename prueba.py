print ("calculos estadisticos")
numeros_ingreso = input("ingrese los numero separados por coma, ejemplo (1,2,3): ")
numeros = numeros_ingreso.split(",")

suma = 0 
longitud = len(numeros)
for i in range(longitud): 
    numeros[i] = float(numeros[i])
    suma = suma + numeros[i]
promedio = suma / longitud

# Parte entera y parte decimal
entero = int(promedio)
decimal = promedio - entero

# Regla: 0.5 o más sube; menor a 0.5 se queda igual
if decimal >= 0.5:
    print("redondeado")
    resultado = entero + 1    # sube al siguiente entero
else:
    resultado = promedio        # se queda igual, con su decimal

print("Promedio redondeado es: ", resultado)