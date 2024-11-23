# Un organismo ha decidido organizar un torneo de fútbol con n equipos 
# participantes. Cada equipo ha de competir exactamente una vez con todos 
# los demás equipos oponentes. Además, se ha decidió que cada equipo juega 
# exactamente un partido cada jornada, con la posible excepción de un solo día en 
# el cual no juega. Si n es una potencia de 2, diseñar un algoritmo que permita 
# que el torneo concluya en n-1 jornadas. 

def organizar_torneo(equipos):
    n = len(equipos)
    if n == 1:
        return []

    mitad = n // 2
    grupo1 = equipos[:mitad]
    grupo2 = equipos[mitad:]
 
    partidos_grupo1 = organizar_torneo(grupo1)
    partidos_grupo2 = organizar_torneo(grupo2)

    partidos_intergrupo = []
    for i in range(mitad):
        partidos_intergrupo.append((grupo1[i], grupo2[i]))

    jornadas = []
    for i in range(mitad - 1):
        jornadas.append(partidos_grupo1[i] + partidos_grupo2[i])
    jornadas.append(partidos_intergrupo)
    
    return jornadas



n = 8 
equipos = [f"Equipo {i + 1}" for i in range(n)]

jornadas = organizar_torneo(equipos)

for i, jornada in enumerate(jornadas, start=1):
    print(f"Jornada {i}: {jornada}")
