# Subsecuencia de suma máxima: 
# Dado un vector V[0..n] de enteros, encontrar los valores de i y j, con 0 <= i <= j <= n, tales que se maximice la suma de los elementos de V[i..j].
# Diseñar un algoritmo recursivo que resuelva el problema en un tiempo en O(n log n). 

def subsecuencia_suma_maxima(V):
    def subsecuencia_suma_maxima_rec(V, i, j):
        if i == j:
            return (i, j, V[i])
        else:
            m = (i + j) // 2
            (i1, j1, s1) = subsecuencia_suma_maxima_rec(V, i, m)
            (i2, j2, s2) = subsecuencia_suma_maxima_rec(V, m + 1, j)
            s3 = 0
            i3 = m
            j3 = m
            s = 0
            for k in range(m, i - 1, -1):
                s += V[k]
                if s > s3:
                    s3 = s
                    i3 = k
            s = 0
            for k in range(m + 1, j + 1):
                s += V[k]
                if s > s3:
                    s3 = s
                    j3 = k
            if s1 >= s2 and s1 >= s3:
                return (i1, j1, s1)
            elif s2 >= s1 and s2 >= s3:
                return (i2, j2, s2)
            else:
                return (i3, j3, s3)
    return subsecuencia_suma_maxima_rec(V, 0, len(V) - 1)

V = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(subsecuencia_suma_maxima(V))  # (2, 6)

