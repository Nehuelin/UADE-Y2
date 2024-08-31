# Suponga que v es un vector de n dígitos binarios ordenados. 
# Encuentre un algoritmo eficiente (mejor que O(n)) que determine la cantidad de unos en v.
# Ejemplo. Si v = [0, 0, 0, 1, 1, 1, 1, 1] (aquí n = 8). El programa debería retornar 5, que es la cantidad de unos en v.

def cantidad_de_unos(v: list[int], ini: int, fin: int) -> int:
    """
    Calcula la cantidad de unos en un vector binario ordenado

    Parameters: 
    v (list[int]): Arreglo binario ordenado
    ini (int): Indice inicial del arreglo a investigar
    fin (int): Indice final del arreglo a invesigar

    Returns:
    int: La cantidad de unos en el arreglo
    """
    if ini > fin:
        return 0
    
    mid = (ini + fin) // 2
    
    if v[mid] == 0:
        return cantidad_de_unos(v, mid + 1, fin)
    else:
        if mid == 0 or v[mid - 1] == 0:
            return (fin - mid + 1)
        else:
            return cantidad_de_unos(v, ini - 1, fin)
        
test = [0, 0, 0, 0, 0, 0, 0, 0]

cant = cantidad_de_unos(test, 0, len(test) - 1)
print(cant)
