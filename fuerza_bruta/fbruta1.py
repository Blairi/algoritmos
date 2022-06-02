
# Encontrar el divisor de un número natural
# Algoritmo Fuerza Bruta

def divisores(numero):
    lista_divisores = []

    for i in range(1, numero + 1, 1): # iteramos n veces encontrando todos los divisiores
        if numero / i % 1 == 0:       # evaluamos la división para saber si da un número entero
            lista_divisores.append( i )

    return lista_divisores

print(f"Divisiores de 99999: { divisores( 99999 ) }")
