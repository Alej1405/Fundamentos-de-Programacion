
# Ingresar la frase encriptada por teclado
encriptada = input("Ingresa la frase encriptada: ")

# Clave usada para cifrar (debe ser la misma)
clave = 5
# Si prefieres ingresar la clave por teclado, descomenta la siguiente línea:
# clave = int(input("Ingresa la clave (entero): "))

descifrada = ""

for caracter in encriptada:
    codigo = ord(caracter)                 # número Unicode del carácter encriptado
    original = (codigo - clave) % 1114112  # invertimos el desplazamiento
    nuevo_caracter = chr(original)         # convertimos nuevamente a carácter
    descifrada += nuevo_caracter

print("Frase descifrada:")
print(descifrada)
