
# Problema para elegir la cantidad de monedas más optima
# para una cantidad

# Algoritmo Greedy

def cantidad_monedas(valor):
    
    monedas = [1, 2, 5, 10, 20] # Definimos arreglo con la denominacion de las monedas
    monedas_seleccionadas = []
    
    # Guardamos el indice de la moneda con mayor denominacion,
    # suponiendo que estan ordenadas en orden ascendente 
    indice = len(monedas) - 1

    while( valor > 0 ): # Repetimos hasta que no haya valor 
        cambio = valor - monedas[indice] # Restamos la denominación de la moneda al valor

        if cambio >= 0: # Si el resultado de la resta es positivo, entonces
            valor = cambio # El nuevo valor a evaluar sera el cambio
            monedas_seleccionadas.append(monedas[indice]) # Guardamos la moneda seleccionada

        else: # Si el resultado de la resta es negativo, significa que no se puede pagar con esa moneda
            indice -= 1 # Cambiamos el indice para evaluar la denominación siguiente más baja

    return monedas_seleccionadas

print(f"Monedas a utilizar para 56: { cantidad_monedas(56) }")
