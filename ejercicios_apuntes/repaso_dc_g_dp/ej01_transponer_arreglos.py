# Trasponer un vector
# Dados un vector V[0..n] y un número natural k entre 1 y n,  
# diseñar un algoritmo eficiente que trasponga los k primeros elementos de V en los elementos en las n-k últimas posiciones, sin hacer uso de un vector auxiliar. 
# Por ejemplo, si V = [3, 5, 12, 8, 9, 12, 4, 7, 13, 21] y k = 3, entonces la funcion debe devolver [8, 9, 12, 4, 7, 13, 21, 3, 5, 12].

# # algoritmo recursivo con costo logn, el algoritmo debe ir elemento por elemento

def trasponer_arreglo(V, k):
    n = len(V)
    if k == 0 or k == n:
        return V
    else:
        V[n-k], V[k-1] = V[k-1], V[n-k]
        return trasponer_arreglo(V, k-1)
V = [3, 5, 12, 8, 9, 12, 4, 7, 13, 21]
k = 3
print(trasponer_arreglo(V, k)) # [8, 9, 12, 4, 7, 13, 21, 3, 5, 12]   





