def hashing_simple(lista, tamano_tabla):
    """
    Implementa una tabla hash utilizando la técnica de hashing simple.

    Este método usa la operación módulo (%) para calcular el índice de
    inserción. Si ocurre una colisión, se aplica sondeo lineal hasta
    encontrar una posición vacía en la tabla.

    Parámetros:
    lista (list): Lista de números a insertar en la tabla hash.
    tamano_tabla (int): Tamaño total de la tabla hash.

    Retorna:
    list: Tabla hash con los elementos insertados.
    """
    tabla = [None] * tamano_tabla
    for num in lista:
        indice = num % tamano_tabla
        while tabla[indice] is not None:
            indice = (indice + 1) % tamano_tabla
        tabla[indice] = num
    return tabla
