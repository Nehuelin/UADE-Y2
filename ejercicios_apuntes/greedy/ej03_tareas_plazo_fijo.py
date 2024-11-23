# Planificación de tareas con plazo fijo: Se deben procesar n tareas en un único 
# procesador. Cada tarea se procesa en una unidad de tiempo y debe ser ejecutada 
# en un plazo no superior a  ti. La tarea i produce una ganancia gi > 0 si se 
# procesa en un instante anterior a ti. Una solución es factible si existe al menos 
# una secuencia S de tareas que se ejecuten antes de sus respectivos plazos. 

class Tarea:
    def __init__(self, time_limit: int, gain: int) -> None:
        self.time_limit = time_limit
        self.gain = gain

    def __repr__(self):
        return f"Tarea(tiempo_limite={self.time_limit}, ganancia={self.gain})"

def maximizar_ganancia(T: list[Tarea]):
    tareas_ordenadas = sorted(T, key=lambda tarea: (tarea.time_limit, -tarea.gain))
    t_MAX = max(tarea.time_limit for tarea in tareas_ordenadas)
    t = 1
    solucion = []
    i = 0
    while(t <= t_MAX):
        if tareas_ordenadas[i].time_limit == t: 
            solucion.append(tareas_ordenadas[i])
            t += 1
        else:
            i += 1
    
    return solucion



t1 = Tarea(2, 50)
t2 = Tarea(1, 10)
t3 = Tarea(2, 15)
t4 = Tarea(1, 30)

T = [t1, t2, t3, t4]

solucion = maximizar_ganancia(T)

for tarea in solucion:
    print(tarea)