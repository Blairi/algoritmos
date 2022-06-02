
# Subarreglo

# Algoritmo divide y venceras

def arreglo_max(arr):
    if len( arr ) == 1:
        return arr[0]

    mitad = len( arr ) // 2
    arr_izq = arr[0:mitad]
    arr_der = arr[mitad:]

    max_izq = arreglo_max(arr_izq)
    max_der = arreglo_max(arr_der)
    max_mitad = calc_max_mitad(arr, mitad)

    return max(max_izq, max_der, max_mitad)
