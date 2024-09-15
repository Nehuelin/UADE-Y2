def fibonacci(n):
    if n < 2:
        return 1
    else:
        tabla = []
        tabla.append(1)
        tabla.append(1)
        for i in range(2, n + 1):
            tabla.append(tabla[i - 2] + tabla[i - 1])
        return tabla[n - 1]

print(fibonacci(10)) 

# Costo O(n), mejor que el algoritmo recursivo que tiene costo O(2^n)