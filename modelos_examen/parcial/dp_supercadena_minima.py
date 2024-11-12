# SUPERCADENA MINIMA

# ESTRATEGIA: Para encontrar la supercadena minima diseñe el siguiente algoritmo:
# 1) El algoritmo hara iteraciones sobre la lista hasta que esta tenga un solo elemento (la cadena final). Por cada iteracion, se inicializan tres variables: la superposicionMaxima, la cual guardará la mayor superposicion posible entre todas las cadenas de la lista, y los indices A y B de las cadenas que lograron esa superposicion maxima.
# 2) Se itera dos veces mas sobre la lista, la primera es para cubrir elemento a elemento, y la segunda para ir de derecha a izquierda hasta el indice en frente del elemento i. Durante cada iteracion j, se verificara si la superposicion maxima posible entre las dos cadenas supera al maximo actual. Si es asi, se le asignara el nuevo valor a la variable y se guardara los indices de dichas cadenas, segun corresponda. 
# 3) Cada vez que se termina los dos bucles anidados, se procede a combinar las dos cadenas que lograron la superposicion maxima: la del indice chico será reemplazada por la nueva cadena y la otra será eliminada. Esto pasará hasta que quede la cadena final en la lista.   

# ALGORITMO encontrarSupercadenaMinima(String[] L){
# 	while(len(L) > 1){
# 		int superposicionMaxima = -1;
# 		int inxA = -1
# 		int inxB = -1
# 		for i in range(len(L)-1){
# 			for j in range(len(L)-1, 0, -1){
# 				if(max(super(L[i], L[j])) > superposicionMaxima){
# 					superposicionMaxima = max(super(L[i], L[j]), super(L[j], L[i]));
# 					if (super(L[j], L[i]) > super(L[i], L[j])){
# 						inxA = j;
# 						inxB = i;
# 					} else {
# 						inxA = i;
# 						inxB = j;
# 					}		
# 				}
# 			}
# 		}
# 		if (inxA > inxB){
# 			L[inxB] = combinar(L[inxA], L[inxB], superposicionMaxima);
#   	    L.remove(inxA);	
#       } else {
# 			L[inxA] = combinar(L[inxA], L[inxB], superposicionMaxima);
# 		    L.remove(inxB);
#       } 
# 	}
#}

# COSTO: O(n^3) ya que hay tres bucles anidados.

def super(A, B):
    max_superposicion = 0
    for i in range(1, min(len(A), len(B)) + 1):
        if A[-i:] == B[:i]:
            max_superposicion = i
    return max_superposicion

def combinar(A, B, k):
    return A + B[k:]

def encontrar_supercadena_minima(L):
    while len(L) > 1:
        superposicion_maxima = -1
        inxA = -1
        inxB = -1
        for i in range(len(L)-1):
            for j in range(i+1, len(L)):
                if max(super(L[i], L[j]), super(L[j], L[i])) > superposicion_maxima:
                    superposicion_maxima = max(super(L[i], L[j]), super(L[j], L[i]))
                    if super(L[j], L[i]) > super(L[i], L[j]):
                        inxA = j
                        inxB = i
                    else:
                        inxA = i
                        inxB = j
        if inxA > inxB:
            L[inxB] = combinar(L[inxA], L[inxB], superposicion_maxima)
            L.remove(L[inxA])
        else:
            L[inxA] = combinar(L[inxA], L[inxB], superposicion_maxima)
            L.remove(L[inxB])
        
    return L[0]

L = ["CATGC", "CTAAGT", "GCTA", "TTCA", "ATGCATC"]
print(encontrar_supercadena_minima(L))
