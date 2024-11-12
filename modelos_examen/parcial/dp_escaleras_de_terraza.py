# EL ASCENSOR DE LA TERRAZA

# ESTRATEGIA: Para encontrar cuantas formas hay de subir n escalones, se puede hacer un algoritmo de programacion dinamica similar a la de Fibonacci, en donde se guarda en una lista el resultado de las operaciones, que se usan despues de manera subsecuente para determinar la cantidad de formas posible de subir el escalon i. Los casos bases ocurren en el primer y segundo escalon. Como se empieza desde el primer escalon, las formas de subirlo son 0. Y hay solo una forma de subir el segundo escalon. 

# ALGORITMO contarManeras(int n){
# 	maneras = int[n + 1]; // n + 1 elementos
# 	for i in range(len(n)){
# 		if(i <= 1){
# 			maneras[i] = i
# 		} else {
# 			maneras[i] = maneras[i-1] + maneras[i-2];
# 		}
# 	}
# 	return maneras[n]
# }

# COSTO: O(n)

def contarManeras(n):
    maneras = [0] * (n + 1)
    for i in range(n + 1):
        if i == 0:
            maneras[i] = 0
        elif i == 1:
            maneras[i] = 1
        else:
            maneras[i] = maneras[i - 1] + maneras[i - 2]
    return maneras[n]

print(contarManeras(8)) 
