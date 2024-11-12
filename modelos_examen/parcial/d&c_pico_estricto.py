# PICO ESTRICTO EN UN ARREGLO

# ESTRATEGIA: Para encontrar un pico estricto se puede utilizar una busqueda binaria en la cual, por cada recursion, se verifican las siguientes condiciones:
# a) Si hay un solo elemento en la lista, es el pico estricto (caso base) 
# b) Si es el primero elemento de la lista y es mayor al siguiente, es un pico estricto
# c) Si es el ultimo elemento de la lista y es mayor al anterior, es un pico estricto
# d) Si el elemento seleccionado es mayor tanto al elemento anterior como a su siguiente, es un pico estricto

# Si no se cumplen esas condiciones, se verifica si el elemento donde esta el indice ini es mayor al elemento seleccionado. Si es asi, entonces un posible pico podrias estar en la primera mitad. De lo contrario, se visita la otra mitad.

# ALGORITMO encontrarPicoEstricto(int[] V, int ini, int fin){
# 	if (ini == fin){
# 		return V[ini];
# 	}

# 	int mid = (ini + fin) // 2;

# 	if (mid == 0 && V[0] > V[1]){
# 		return V[0];
# 	}

# 	if (mid == len(V) - 1 && V[len(V) - 2] < A[len(V) - 1]){
# 		return V[len(V) - 1];
# 	}

# 	if (V[mid] > V[mid - 1] && V[mid] > V[mid + 1]){
# 		return V[mid];
# 	} 

# 	if (V[ini] > V[mid]){
# 		return encontrarPicoEstricto(V, ini, mid - 1);
# 	} else {
# 		return encontrarPicoEstricto(V, mid + 1, fin);
# 	}
# }

# COSTO: O(log(n)) ya que es una recursion del tipo D&C donde a = 1, b = 2 y k = 0, entonces como a = b^k el costo va a ser O((n^k)log(n)), como n^k = 1 entonces queda O(log(n)).
def encontrarPicoEstricto(V, ini, fin):
    if ini == fin:
        return V[ini]

    mid = (ini + fin) // 2

    if mid == 0 and V[0] > V[1]:
        return V[0]

    if mid == len(V) - 1 and V[len(V) - 2] < V[len(V) - 1]:
        return V[len(V) - 1]

    if V[mid] > V[mid - 1] and V[mid] > V[mid + 1]:
        return V[mid]

    if V[ini] > V[mid]:
        return encontrarPicoEstricto(V, ini, mid - 1)
    else:
        return encontrarPicoEstricto(V, mid + 1, fin)
    
V = [1, 2, 3, 4, 6, 7, 8]
print(encontrarPicoEstricto(V, 0, len(V) - 1))
