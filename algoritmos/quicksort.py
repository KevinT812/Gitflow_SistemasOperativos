def quicksort(lista):
    """
    Ordena una lista utilizando el algoritmo QuickSort.

    QuickSort es un algoritmo de ordenamiento basado en la estrategia
    “divide y vencerás”. Selecciona un pivote, divide la lista en dos
    sublistas (menores y mayores al pivote) y las ordena recursivamente.

    Parámetros:
    lista (list): Lista de números a ordenar.

    Retorna:
    list: Nueva lista ordenada de menor a mayor.
    """
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivote]
        centro = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x > pivote]
        return quicksort(izquierda) + centro + quicksort(derecha)
