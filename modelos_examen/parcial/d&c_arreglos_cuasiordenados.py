# ARREGLOS CUASIORDENADOS

# ESTRATEGIA: Para encontrar el elemento desordenado se utilizar una busqueda binaria en donde por cada recursion se verifica las siguientes condiciones:
# a) si hay un solo elemento en la lista (caso base), quiere decir que no hay elemento desordenado
# b) si el elemento seleccionado es menor a su antecesor y al mismo tiempo es menor a su sucesor, entonces el elemento antecesor es el desordenado. Si el elemento seleccionado es MAYOR a su sucesor entonces el elemento seleccionado es el desordenado
# c) si el elemento seleccionado es mayor al elemento del indice donde esta el inicio de la busqueda binaria, quiere decir que el elemento desordenado esta en la mitad derecha. De lo contrario, se busca en la izquierda

# ALGORITMO encontrarElemento(Array[int] V, int ini, int fin){
# 	if(ini == fin){
# 		return -1;
# 	}

# 	mid = (ini + fin) / 2;

# 	if(mid > 0 && V[mid] < V[mid - 1]{
# 		if(V[mid] < V[mid + 1]){
# 			return V[mid - 1];
# 		} else {
# 			return V[mid];
# 		}
# 	} 

# 	if(mid < len(V) - 1 && V[mid] > V[mid + 1]){
# 		return V[mid];
# 	}

# 	if V[mid] >= V[ini]{
# 		return encontrarElemento(V, mid + 1, fin);
# 	} else {
# 		return encontrarElemento(V, ini, mid - 1);
# 	}
# }

# COSTO: O(log(n)) ya que es una recursion del tipo D&C donde a = 1, b = 2 y k = 0, entonces como a = b^k el costo va a ser O((n^k)log(n)), como n^k = 1 entonces queda O(log(n)).

def encontrar_elemento(V, ini, fin):
    if ini >= fin:
        return -1  

    mid = (ini + fin) // 2

    if mid > 0 and V[mid] < V[mid - 1] and V[mid] < V[mid + 1]:
        return V[mid - 1]
    elif mid > 0 and V[mid] < V[mid - 1] and V[mid] > V[mid + 1]:
        return V[mid]
    if mid < len(V) - 1 and V[mid] > V[mid + 1]:
        return V[mid]
    if V[mid] >= V[ini]:
        return encontrar_elemento(V, mid + 1, fin)
    else:
        return encontrar_elemento(V, ini, mid - 1)

V = [1, 2, 3, 4, 6, 5, 7]
print(encontrar_elemento(V, 0, len(V) - 1))
