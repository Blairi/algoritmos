
# Busqueda binaria de números
# Algortimo top-down

import random
import time

##@author:      Marín Montaño Josué
##@date:        04/05/2022
##@brief:       Busca un numero en una lista ordenada de numeros
##@param  objetivo El numero a buscar
##@param  lista La lista de numeros

def búsqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):
    if límite_inferior is None:
        límite_inferior = 0 # Inicio de la lista
    if límite_superior is None:
        límite_superior = len(lista) - 1 # Final de la lista

    if límite_superior < límite_inferior:
        return -1

    punto_medio = (límite_inferior + límite_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return búsqueda_binaria(lista, objetivo, límite_inferior, punto_medio-1)
    else:
        return búsqueda_binaria(lista, objetivo, punto_medio+1, límite_superior)


if __name__=='__main__':
    # Crear una lista ordenada con 10000 números aleatorios.
    tamaño = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el tiempo de búsqueda binaria.
    inicio = time.time()

    objetivo = 3
    búsqueda_binaria(lista_ordenada, objetivo)

    fin = time.time()
    print(f"Tiempo de búsqueda de {objetivo} binaria: {fin - inicio} segundos.")
