# CONTAR APARICIONES DE UN ELEMENTO

# ESTRATEGIA: Para contar las apariciones de un elemento podemos utilizar la busqueda binaria para encontrar la primera y ultima aparicion de dicho elemento. Para eso considere tres algoritmos: 
# 1) encontrarPrimero: este algoritmo usa busqueda binaria para encontrar la primera aparicion del elemento en la lista. En ese caso, se verifica que el elemento anterior al seleccionado sea distinto a x, indicando de que efectivamente es el primer elemento. El caso base ocurre cuando queda un elemento en la lista: si es igual a x, es el primer elemento. 
# 2) encontrarUltimo: idem al algoritmo anterior, pero busca la ultima aparicion. Para verificar que se trate de ese caso, el elemento posterior al seleccionado debe ser distinto de x. 
# 3) contarApariciones: este algoritmo invoca a los otros dos y devuelve la diferencia entre los indices, sumando uno al final para contrarrestar la base 0. 


# ALGORITMO encontrarPrimero(int[] V, int x, int ini, int fin){
# 	if(ini > fin){
# 		return -1;
# 	}

# 	if (ini == fin && V[ini] == x){
# 		return ini;
# 	}

# 	int mid = (ini + fin) / 2

# 	if (mid != 0){
# 		if(V[mid] == x && V[mid - 1] != x){
# 			return mid; // encontramos el primero
# 		} 
# 	}
	

# 	if(V[mid] >= x){
# 		return encontrarPrimero(V, x, ini, mid - 1);
# 	} else {
# 		return encontrarPrimero(V, x, mid + 1, fin); 
# 	}


# ALGORITMO encontrarUltimo(int[] V, int x, int ini, int fin){
# 	if(ini > fin){
# 		return -1;
# 	}

# 	if (ini == fin && V[fin] == x){
# 		return fin;
# 	}

# 	int mid = (ini + fin) / 2

# 	if (mid != len(V) - 1) {
# 		if(V[mid] == x && V[mid + 1] != x){
# 			return mid; // encontramos el ultimo
# 		} 
# 	} 
	

# 	if(V[mid] > x){
# 		return encontrarPrimero(V, x, ini, mid - 1);
# 	} else {
# 		return encontrarPrimero(V, x, mid + 1, fin); 
# 	}
# }

# ALGORITMO contarApariciones(int[] V, int x){
# 	indexA = encontrarPrimero(V, x, 0, len(V) - 1) // O(log(n))
# 	indexB = encontrarUltimo(V, x, 0, len(V) - 1) // O(log(n))
# 	return (indexB - indexA + 1) // O(1)
# }

# COSTO: O(log(n))

def encontrarPrimero(V, x, ini, fin):
    if ini > fin:
        return -1

    if ini == fin and V[ini] == x:
        return ini

    mid = (ini + fin) // 2

    if mid != 0:
        if V[mid] == x and V[mid - 1] != x:
            return mid
        

    if V[mid] >= x:
        return encontrarPrimero(V, x, ini, mid - 1)
    else:
        return encontrarPrimero(V, x, mid + 1, fin)

def encontrarUltimo(V, x, ini, fin):
    if ini > fin:
        return -1

    if ini == fin and V[fin] == x:
        return fin

    mid = (ini + fin) // 2

    if mid != len(V) - 1:
        if V[mid] == x and V[mid + 1] != x:
            return mid
        

    if V[mid] > x:
        return encontrarUltimo(V, x, ini, mid - 1)
    else:
        return encontrarUltimo(V, x, mid + 1, fin)
    
def contarApariciones(V, x):
    indexA = encontrarPrimero(V, x, 0, len(V) - 1)
    indexB = encontrarUltimo(V, x, 0, len(V) - 1)
    return (indexB - indexA + 1)

V = [1, 2, 3, 3, 3, 3, 3, 6, 7, 8, 9]
print(contarApariciones(V, 0)) 

