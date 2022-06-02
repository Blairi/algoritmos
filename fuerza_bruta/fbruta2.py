
# Cifrar un mensaje
# Algoritmo Fuerza Bruta

import string

def cifrar( cadena, clave ):
    abcedario = string.ascii_lowercase
    mensaje_cifrado = ""

    for letra in cadena:
        if letra in abcedario:

            indice = abcedario.find(letra)
            indice += clave

            if indice > len( abcedario ):
                indice -= len( abcedario )

            mensaje_cifrado += abcedario[indice]

        else:
            mensaje_cifrado += letra

    return mensaje_cifrado

print(cifrar("Mensaje secreto y cifrado", 5))
