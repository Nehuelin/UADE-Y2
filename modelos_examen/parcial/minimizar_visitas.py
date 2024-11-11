# MINIMIZAR VISITAS

# ESTRATEGIA: Para minimizar la cantidad de veces que debe ir el controlador podemos utilizar un algoritmo que por cada horario verifique si la hora de inicio de una clase supera a la hora que tuvo la ultima visita. Con esto nos aseguramos que todas las clases que tengan un horario de inicio menor al de la ultima visita sean visitadas.

# Class Horario{
# 	int inicio;
# 	int fin;
# }

# ALGORITMO minimizarVisitas(Horario[] S){
# 	int visitas = 0;
# 	int ultimaVisita = -1;

# 	S.sort(S.fin); // ordena de menor a mayor por horario de finalizacion
	
# 	for i in range(len(S) - 1){
# 		if(S[i].inicio >= ultimaVisita){
# 			visitas++;
# 			ultimaVisita = S[i].fin;
# 		}
# 	}

# 	return visita;
# }

# COSTO: O(n log n) por ordenamiento de elementos

def visitas_minimas(S):
    S_ordenado = sorted(S, key=lambda x: x[1])

    visitas = 0
    ultima_visita = -1  

    for inicio, fin in S_ordenado:
        if inicio > ultima_visita:
            visitas += 1
            ultima_visita = fin  
    return visitas

# S = [(8, 10), (9, 12), (11, 13), (11, 14), (13, 16), (17, 19)]
S = [(8, 11), (10, 14), (11, 12), (14, 17)]
print(visitas_minimas(S))