# BUSQUEDA EN ARREGLOS CASI ORDENADOS

# ESTRATEGIA: Para encontrar un elemento x se puede utilizar una busqueda binaria en donde se hagan las siguientes verificaciones:
# a) que haya un solo elemento y sea el que se busca (caso base)
# b) que el elemento medio sea x
# c) que alguno de sus vecinos sea x
# Si no se logra verificar ninguna de las anteriores, se realiza la recursion en la mitad donde podria estar el elemento; esto es, si el elemento del medio es mayor a x, entonces x debe estar del lado izquierdo, de lo contrario se busca del otro lado.

# ALGORITMO encontrarElemento(int[] V, int x, int ini, int fin){
# 	if (ini > fin){
# 		return -1;
# 	}

# 	if (ini == fin && V[ini] == x){
# 		return ini;
# 	}

# 	int mid = (ini + fin) // 2

# 	if (V[mid] == x){
# 		return mid;
# 	} else if (V[mid - 1] == x){
# 		return mid - 1;
# 	} else if (V[mid + 1] == x){
# 		return mid + 1;
# 	}

# 	if (V[mid] > x) {
# 		return encontrarElemento(V, x, ini, mid - 1);
# 	} else {
# 		return encontrarElemento(V, x, mid + 1, fin);
# 	}
# }

# COSTO: O(log(n))

def encontrarElemento(V, x, ini, fin):
    if ini > fin:
        return -1

    if ini == fin and V[ini] == x:
        return ini

    mid = (ini + fin) // 2

    if V[mid] == x:
        return mid
    elif V[mid - 1] == x:
        return mid - 1
    elif V[mid + 1] == x:
        return mid + 1

    if V[mid] > x:
        return encontrarElemento(V, x, ini, mid - 1)
    else:
        return encontrarElemento(V, x, mid + 1, fin)
    
V = [2, 1, 3, 5, 4, 7, 6, 8]

print(encontrarElemento(V, 2, 0, len(V) - 1))
print(encontrarElemento(V, 1, 0, len(V) - 1))
print(encontrarElemento(V, 3, 0, len(V) - 1))
print(encontrarElemento(V, 5, 0, len(V) - 1))
print(encontrarElemento(V, 4, 0, len(V) - 1))
print(encontrarElemento(V, 7, 0, len(V) - 1))
print(encontrarElemento(V, 6, 0, len(V) - 1))
print(encontrarElemento(V, 8, 0, len(V) - 1))
print(encontrarElemento(V, 9, 0, len(V) - 1))