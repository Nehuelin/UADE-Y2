# Varios cursos están programados en el campus de la Universidad de Fraile Muerto. 
# Por supuesto, no puede haber dos cursos al mismo tiempo en la misma aula. 
# Dé un algoritmo greedy que calcule el número mínimo de aulas necesarias para programar todos los cursos. 
# Usted tiene a su disposición un número arbitrario de aulas.

class curso:
    def __init__(self, inicio: int, fin: int):
        self.inicio = inicio
        self.fin = fin


def assign_classrooms(V: list[curso]):
    events = []
    for i in range(len(V)):
        events.append((V[i].inicio, "inicio"))
        events.append((V[i].fin, "fin"))
    
    sorted_events = sorted(events, key= lambda x: (x[0], x[1] == "fin"))

    min_rooms = 0
    rooms_in_use = 0

    for i in range(len(events)):
        if sorted_events[i][1] == "inicio":
            rooms_in_use += 1
            min_rooms = max(min_rooms, rooms_in_use)
        else:
            rooms_in_use -= 1
    
    return min_rooms

cursos = [
    curso(30, 75), 
    curso(0, 50), 
    curso(60, 150)
]

print(f"Aulas minimas para atender a todos los cursos: {assign_classrooms(cursos)}")