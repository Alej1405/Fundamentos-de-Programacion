# Ingresar la frase encriptada por teclado
encriptada = input("Ingresa la frase encriptada: ")

# Clave usada para cifrar 
clave = 5
descifrada = ""

for caracter in encriptada:
    codigo = ord(caracter)                 # número Unicode del carácter encriptado
    original = (codigo - clave) % 1114112  # invertimos el desplazamiento
    nuevo_caracter = chr(original)         # convertimos nuevamente a carácter
    descifrada += nuevo_caracter

print("---SISTEMA DE DESENCRIPTACION DE CLAVES---")
print("Frase descifrada:")
print(descifrada)
