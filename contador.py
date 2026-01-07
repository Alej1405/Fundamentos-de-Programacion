# Solicitar la frase al usuario
frase = input("Ingresa una frase: ")

# Dividir la frase en palabras usando split()
palabras = frase.split()

# Contar la cantidad de palabras
contador = len(palabras)

# Mostrar el resultado
print(f"La frase tiene {contador} palabras.")
