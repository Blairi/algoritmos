memoria = {0:1, 1:1, 2:2}


##@author:      Marín Montaño Josué
##@date:        04/05/2022
##@brief:       Calcula los numeros de fibbonacci del 2 a un numero dado y los almacena en la memoria
##@param  numero Numero dado
def fibonacci_suma(numero):
    f1=0
    f2=1
    for i in range(1,numero-1):
        f1,f2= f2,f1+f2 
    return f2

##@author:      Marín Montaño Josué
##@date:        04/05/2022
##@brief:       Devuelve el numero de fibbonacci de un numero dado en base a los resultados previamente calculados
##@param  numero Numero dado

def fibonacci_busqueda (numero):
    if numero in memoria:   
        return memoria [numero] #Retorna el resultado si se calculo previamente
    f = fibonacci_suma(numero-1) + fibonacci_suma(numero-2)#Si no se tiene el rrsultado, se calcula mediante la suma de los 2 numeros de fibonnacci previos
    memoria[numero] = f
    return memoria [numero]


print(fibonacci_busqueda(8))
