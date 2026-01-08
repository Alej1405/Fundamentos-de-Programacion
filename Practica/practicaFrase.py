frase = "hola mundo"
clave = 5

for caracter in frase:
    codigo = ord(caracter)
    encriptado = (codigo + clave) % 1114112
    print(caracter, codigo, encriptado)