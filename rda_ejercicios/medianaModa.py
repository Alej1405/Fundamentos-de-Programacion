numeros = []

cantidad = int(input("cuantos numeros deseas ingresar? "))

for i in range(cantidad):
    numero = int(input(f"ingrese el numero {i+1}: "))
    numeros.append(numero)

print("La lista de numero es:", numeros)