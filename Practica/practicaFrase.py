
frase = "hola mundo"
clave = 5

encriptada = ""

for caracter in frase:
    codigo = ord(caracter)
    encriptado = (codigo + clave) % 1114112   # rango Unicode completo
    nuevo_caracter = chr(encriptado)
    encriptada += nuevo_caracter
    print(caracter, codigo, encriptado, nuevo_caracter)

print("\nFrase encriptada:")
print(encriptada)
