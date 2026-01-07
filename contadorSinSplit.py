
frase = input("Ingresa una frase: ")

#separadores
separadores = set([" ", "\t", "\n"])
#omitir signos de puntuacion
puntuacion = set([",", ".", ";", ":", "!", "?", "¡", "¿"])

en_palabra = False
contador = 0

for ch in frase:
    if ch in separadores:
        en_palabra = False
    else:
        # caracteres de puntuación por sí solos no inician palabra
        if ch in puntuacion and not en_palabra:
            continue
        if not en_palabra:
            contador += 1
            en_palabra = True

print(f"La frase tiene {contador} palabras.")
