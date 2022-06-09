
# Encontrar el divisor de un número natural
# Algoritmo Fuerza Bruta


##@author:      López López Axel Dion
##@date:        02/05/2022
##@brief:       Devuelve los divisores de un numero natural
##@param  numero Un numero natural
##@return lista_divisores La lista de duvisores del numero proporcionado

def divisores(numero): ##O=n
    lista_divisores = []

    for i in range(1, numero + 1, 1): # iteramos n veces encontrando todos los divisiores
        if numero / i % 1 == 0:       # evaluamos la división para saber si da un número entero
            lista_divisores.append( i )

    return lista_divisores

print(f"Divisiores de 99999: { divisores( 99999 ) }")
