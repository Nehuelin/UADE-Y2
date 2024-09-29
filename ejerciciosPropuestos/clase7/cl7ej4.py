# La fábrica de saxofones. Son necesarios varias etapas para producir un saxofón: 
# formación del cuerpo principal, curvado, perforación, adición de teclas, adición de la parte superior y adición de la boquilla.
# La fábrica Blue Note de Fraile Muerto cuenta con dos líneas de producción. 
# Cada línea de ensamblaje i contiene todas las estaciones (cuerpo principal, curvado, perforaciones, teclas, parte superior, boquilla).
# Denotamos a las estaciones S[i, j] con i ∈ {1,2} y j ∈ {1,...,6}. 
# Las estaciones S[1,j] y S[2,j] realizan el mismo trabajo pero no en el mismo tiempo, ya que el procedimiento es a mano. 
# Llamamos T[i, j] al tiempo pasado en a estación j de la línea de ensamblaje i.
# Un saxofón debe atravesar las seis etapas mencionadas hasta que está terminado. 
# Puede hacerlo en una única línea de ensamblaje o alternar entre ambas. 
# Cuando el instrumento pasa de la estación j a la estación j +1 de la misma línea de ensamblaje, esto es instantáneo; 
# pero cuando cambia de una línea de ensamblaje a la otra, esto tiene una demora D[j] con j ∈ {1,...,5}.

# EJEMPLO:  
# supongamos que es D = [3,2,2,3,2] y S = [[6 4 5 2 3 4], [4 3 5 5 6 6]
# La producción de un saxofón en la línea 1 toma 6 + 4 + 5 + 2 + 3 + 4 = 24 unidades de tiempo;
# Con S[2,1], S[2,2], S[1,3], S[1,4], S[2,5], S[2,6], tenemos 4 + 3 + (2) + 5 + 2 + (3) + 5 + 5 = 27 unidades de tiempo.
# Los números entre paréntesis dan el tiempo para cambiar de una línea de ensamblaje a la otra.

# Encuentre una estrategia de programación dinámica para minimizar el tiempo de producción de un saxofón


import numpy as np

def minimize_production_time(S, D):
    optimal_walkthrough = []
    acum = np.zeros((2, 6), int)
    for j in range(len(acum[0])):
        for i in range(len(acum)):
            if j == 0:
                acum[i][j] = S[i][j]
                if i == 1:
                    minimum_time = min(acum[i - 1][j], acum[i][j])
                    coordinates = [0, j] if minimum_time == acum[i - 1][j] else [1, j]
                    optimal_walkthrough.append(coordinates)
            elif i == 0:
                acum[i][j] = min(acum[i][j - 1], acum[i + 1][j - 1] + D[j - 1]) + S[i][j]
            elif i == 1:
                acum[i][j] = min(acum[i][j - 1], acum[i - 1][j - 1] + D[j - 1]) + S[i][j]
                minimum_time = min(acum[i - 1][j], acum[i][j])
                coordinates = [0, j] if minimum_time == acum[i - 1][j] else [1,j]  
                optimal_walkthrough.append(coordinates)  

    return minimum_time, optimal_walkthrough

S = [[6, 4, 5, 2, 3, 4],
     [4, 3, 5, 5, 6, 6]]

D = [3, 2, 2, 3, 2]

tiempo_minimo, tiempos = minimize_production_time(S, D)
print(f"El tiempo minimo posible para producir saxofonos es de {tiempo_minimo} segundos siguiendo la siguiente secuencia: \n{tiempos}")