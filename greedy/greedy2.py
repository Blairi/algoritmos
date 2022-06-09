# Algoritmo Greedy

eventos = {
    "evento1": [0,5],
    "evento2": [1,2],
    "evento3": [2,3]
}

##@author:      Montiel Aviles Axel Fernando
##@date:        04/05/2022
##@brief:       Ordena los eventos para tener el mayor numero posible sin que sus horarios choquen
##@param  valor Los eventos a organizar


def ordenar_eventos(eventos):
    eventos_ordenados = []
    horarios_ascendentes = []
    for evento in eventos:
        horarios_ascendentes.append(eventos[evento][1])

    print(horarios_ascendentes)

ordenar_eventos(eventos)

def max_eventos():
    pass

print(max_eventos())
