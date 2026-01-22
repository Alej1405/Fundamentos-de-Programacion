#ingresar dos frases por teclado y controlar que el usuario solo ingrese 3 palabras 

while True:
    frase1 = input("ingrese una frase no mas de tres palabras: ")
    frase2 = input("ingrese una frase no mas de tres palabras: ")

    frase1 = frase1.split()
    frase2 = frase2.split()

    uno = len(frase1)
    dos = len(frase2)

    if uno == 3 and dos == 3 :
        break
    else:
        print("Las dos frases solo deben tener tres palabras")

print(frase1[1:2])
print(frase2[2:3])

