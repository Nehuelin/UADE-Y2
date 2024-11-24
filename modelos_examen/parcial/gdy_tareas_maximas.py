# ESTRATEGIA: Para encontrar el conjunto Tmax, se puede utilizar un algoritmo greedy que ordena la lista de menor a mayor por tiempo de finalizacion, 
# y luego por cada tarea se fija el inicio de dicha tarea es igual o mayor al tiempo de finalizacion de la ultima tarea registrada. Si es asi, el tiempo de finalizacion de
# la tarea seleccionada se vuelve el ultimo fin registrado. Cada tarea seleccionada se agrega a una lista solucion, que se devuelve al final del algoritmo.

# ALGORITMO maximizarTareas(T: Vector<Tarea>){ // sea Tarea un objeto con atributos numero, inicio y fin (todos enteros)
#  	T.ordenar(x.fin) // se ordena por tiempo de finalizacion
# 	last_fin = 0
# 	solucion = int[]
# 	para i = 0 hasta len(T){
# 		si (T[i].inicio >= last_fin){
# 			last_fin = T[i].fin
# 			solucion.agregar(T[i])
# 		}
# 	}

# 	devolver solucion
# }

# COMPLEJIDAD: O(T) siendo T la cantidad de tareas

class Tarea:
    def __init__(self, numero, inicio, fin) -> None:
        self.numero = numero
        self.inico = inicio
        self.fin = fin

def maximizar_tareas(T: list[Tarea]):
    tareas_ordenadas = sorted(T, key=lambda x: x.fin)
    last_fin = 0
    solucion = []
    for tarea in tareas_ordenadas:
        if tarea.inico >= last_fin:
            last_fin = tarea.fin
            solucion.append(tarea)
    
    return solucion

T = [Tarea(1, 2, 4), 
     Tarea(2, 1, 5),
     Tarea(3, 4, 7),
     Tarea(4, 3, 5),
     Tarea(5, 6, 8),
     Tarea(6, 5, 8),
     Tarea(7, 5, 10),
     Tarea(8, 8, 10),
     Tarea(9, 7, 10),
     Tarea(10, 10, 12)]

solucion = maximizar_tareas(T)

for tarea in solucion:
    print(tarea.numero)