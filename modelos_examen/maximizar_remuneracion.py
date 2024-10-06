# MAXIMIZAR GANANCIA 

# ESTRATEGIA: Para maximizar las ganancias se puede utilizar un algoritmo greedy que ordena la lista de forma descendiente segun la remuneracion de las solicitudes, y despues itera de forma inversa por los dias, asegurandose de que, mientras se pueda cumplir el plazo, se elija la solicitud de mayor prioridad

# NOTA: Para este ejercicio considero como tiempo del plan de trabajo el plazo maximo posible entre todas las solicitudes

# Clase Solicitud{
# 	int r; // remuneracion
# 	int e; // plazo entrega
# }

# ALGORITMO maximizarRemuneracion(Solicitud[] S, int t){
# 	S.sort(S.r, reverse=true) // se ordena la lista en orden descendiente por remuneracion

# 	int plazo_maximo = max(S[i].e for i in range(len(S) - 1));
# 	boolean[] dias = [false for _ in range(plazo_maximo + 1)];
# 	int total = 0;

# 	for remuneracion, plazo in S{ 
# 		for i in range(plazo_maximo, 0, -1){
# 			if(!dias[i]){ // recorro los dias de adelante hacia atras
# 				dias[i] = true;
# 				total += remuneracion;
# 			}
# 		}

# 	return total;
# }

# COSTO: O(S*t) siendo S la cantidad de solicitudes y t el plazo maximo posible de todas las solicitudes


def maximizar_remuneracion(solicitudes):
    solicitudes.sort(key=lambda x: x[1], reverse=True)
    max_plazo = max([s[0] for s in solicitudes])
    dias_ocupados = [False] * (max_plazo + 1)
    
    remuneracion_total = 0
    for plazo, pago in solicitudes:
        for dia in range(plazo, 0, -1):
            if not dias_ocupados[dia]: 
                dias_ocupados[dia] = True  
                remuneracion_total += pago  
                break  
    return remuneracion_total

solicitudes = [(2, 10), (3, 15), (4, 10), (2, 20), (3, 10), (4, 30), (5, 20), (6, 20), (7, 15), (5, 10), (5, 10), (6, 35), (7, 10)]
print("Remuneración máxima:", maximizar_remuneracion(solicitudes))