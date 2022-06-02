
# Tener el máximo número de eventos en un salón sin que choquen sus horarios
# Algoritmo Greedy

eventos = {
    "evento1": [0,5],
    "evento2": [1,2],
    "evento3": [2,3]
}

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
