# El conservatorio de música de Fraile Muerto es una institución con limitados recursos. 
# Cuando se acercan los exámenes, un solo piano de cola está disponible para que los estudiantes puedan practicar. 
# Los estudiantes deben presentar una solicitud para usar el piano. 
# La solicitud debe indicar la hora de inicio y de finalización.
# Tenemos el conjunto de solicitudes para un día determinado y queremos maximizar el número de estudiantes que pueden usar el piano. 
# Proponga un esquema greedy para resolver este problema.

class Solicitud:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __repr__(self):
        return f"({self.inicio}, {self.fin})"

def create_schedule(V: list[Solicitud]):
    sorted_requests = sorted(V, key=lambda x: x.fin)
    last_fin = 0
    schedule = []
    for request in sorted_requests:
        if request.inicio > last_fin:
            schedule.append(request)
            last_fin = request.fin

    return schedule

solicitudes = [
    Solicitud(1, 4),
    Solicitud(2, 3),
    Solicitud(3, 5),
    Solicitud(0, 6),
    Solicitud(5, 7),
    Solicitud(8, 9),
    Solicitud(5, 9)
]

resultado = create_schedule(solicitudes)
print("Cronograma:")
for solicitud in resultado:
    print(solicitud)
