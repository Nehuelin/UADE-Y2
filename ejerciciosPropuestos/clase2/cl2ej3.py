def num_min_pesadas(n):
    if n <= 1:
        return 0
    # Dividimos n en tres partes iguales, o lo más cerca posible
    grupo1 = n // 3
    grupo2 = n // 3
    grupo3 = n - grupo1 - grupo2  # El tercer grupo toma el sobrante para sumar n

    # Siempre se realiza una pesada y luego se llama recursivamente al grupo más grande
    return 1 + num_min_pesadas(max(grupo1, grupo2, grupo3))
# costo temporal O(log3(n))