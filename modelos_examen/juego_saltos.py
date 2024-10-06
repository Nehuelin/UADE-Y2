# JUEGO DE LOS SALTOS

# ESTRATEGIA: Se hace una lista dp donde, inicialmente, se almacenan un conjunto de infinitos
# Como inicialmente estamos parados en primer elemento, se considera que no se requieren saltos, por ende se le pone un 0. Despues se inician dos bucles:
# --> El primero (i) es para iterar por todos los elementos de la lista de saltos
# --> El segundo (j) es para verificar, por cada elemento que vino antes, si el indice i es menor o igual que j + los saltos habilitados. Si es asi, entonces a ese indice de la lista dp se le asignara el minimo entre el elemento que ya haya en ese indice, o el del indice j, sumandole 1.

# ALGORITMO saltosMinimos(jumps){
# 	n = len(jumps);
# 	dp = [0] * n;
# 	dp[0] = 0;
# 	for i in range(1, n){
# 		dp[i] = 99999999;
# 		for j in range(i){
# 			if i <= j + jumps[j]{
# 				dp[i] = min(dp[i], dp[j] + 1)
# 			}
# 		}
# 	}

# 	return dp[n - 1]
# }

# COSTO: O(n^2) ya que hay dos bucles anidados que, en el peor caso, iteran n veces al mismo tiempo

# Para mostrar en que indices se realizaron los saltos, se deberia hacer una segunda lista llamada inx, en la cual se asignan los indices del cual se hizo el salto. En este caso, el primer elemento inicia con -1, y por cada elemento siguiente, si dp[i] = dp[j] + 1, entonces inx[i] = j

def saltos_minimos(jumps):
    n = len(jumps)
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i):
            if i <= j + jumps[j]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n - 1]

V = [2, 3, 1, 1, 4]
print(saltos_minimos(V))

