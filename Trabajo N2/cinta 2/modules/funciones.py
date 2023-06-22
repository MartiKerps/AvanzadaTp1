def promedio_aw (lista1,lista2):
   
    suma_lista1 = sum(lista1)
    
    suma_lista2 = sum(lista2)
    
    promedio_lista1 = suma_lista1 / len(lista1)
    promedio_lista2 = suma_lista2 / len(lista2)
    
    promedio_total = (promedio_lista1 + promedio_lista2) / 2
    
    return promedio_total


def promedio_alimentos (*listas):
 
    # Inicializar la suma de elementos y el número total de elementos
    suma_total = 0
    elementos_totales = 0
    
    # Iterar sobre cada lista
    for lista in listas:
        suma_lista = sum(lista)  # Calcular la suma de la lista actual
        elementos_lista = len(lista)  # Obtener el número de elementos en la lista actual
        
        suma_total += suma_lista  # Sumar la suma de la lista actual a la suma total
        elementos_totales += elementos_lista  # Sumar el número de elementos de la lista actual al total
        
    # Calcular el promedio total dividiendo la suma total entre el número total de elementos
    promedio_total = suma_total / elementos_totales
    
    return promedio_total
