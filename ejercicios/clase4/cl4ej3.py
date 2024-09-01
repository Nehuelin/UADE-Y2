# Tenemos un conjunto de tareas que deben ser realizadas por un único recurso, de manera que no se pueden realizar dos al mismo tiempo. 
# Cada tarea j tiene un tiempo de procesamiento tj y un plazo dj. 
# Si la tarea j comienza en el tiempo sj, terminará en el tiempo fj = sj + tj. 
# Definimos la demora ℓj de la tarea j como ℓj = max(0, fj − dj).
# Queremos un esquema greedy que minimice la máxima demora, es decir L = maxjℓj

class Tarea:
    def __init__(self, tiempo_procesamiento, plazo):
        self.tiempo_procesamiento = tiempo_procesamiento
        self.plazo = plazo

    def calcular_finalizacion(self, tiempo_inicio):
        return tiempo_inicio + self.tiempo_procesamiento

    def calcular_demora(self, tiempo_inicio):
        tiempo_finalizacion = self.calcular_finalizacion(tiempo_inicio)
        return max(0, tiempo_finalizacion - self.plazo)


def minimizar_maxima_demora(tareas):
    tareas_ordenadas = sorted(tareas, key=lambda tarea: tarea.plazo)

    tiempo_actual = 0
    maxima_demora = 0

    for tarea in tareas_ordenadas:
        tiempo_finalizacion = tarea.calcular_finalizacion(tiempo_actual)
        demora = tarea.calcular_demora(tiempo_actual)
        maxima_demora = max(maxima_demora, demora)
        tiempo_actual = tiempo_finalizacion

    return maxima_demora


tareas = [
    Tarea(4, 7),
    Tarea(4, 5),
    Tarea(3, 5)
]

maxima_demora = minimizar_maxima_demora(tareas)
print(f"La máxima demora mínima es: {maxima_demora}")