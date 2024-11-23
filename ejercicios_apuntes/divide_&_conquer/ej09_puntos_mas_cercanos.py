# El problema del par más cercano consiste en encontrar dos puntos dentro de un 
# conjunto de puntos cuya distancia sea menor que la que existe entre cualquier otro 
# par de puntos del conjunto. Suponiendo que los puntos vienen ordenados por sus 
# coordenadas (x; y), y que han sido clasificados en orden ascendente de la 
# coordenada x, resolver el problema

import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def par_mas_cercano(puntos):
    if len(puntos) <= 3:
        return fuerza_bruta(puntos)
    
    mitad = len(puntos) // 2
    izquierda = puntos[:mitad]
    derecha = puntos[mitad:]
    
    (p1, q1, d1) = par_mas_cercano(izquierda)
    (p2, q2, d2) = par_mas_cercano(derecha)

    d = min(d1, d2)
    (p_min, q_min) = (p1, q1) if d1 < d2 else (p2, q2)

    p_cruce = [p for p in puntos if abs(p[0] - puntos[mitad][0]) < d]
    p_cruce.sort(key=lambda p: p[1]) 

    for i in range(len(p_cruce)):
        for j in range(i + 1, min(i + 8, len(p_cruce))):
            d_cruce = distancia(p_cruce[i], p_cruce[j])
            if d_cruce < d:
                d = d_cruce
                p_min, q_min = p_cruce[i], p_cruce[j]
    
    return (p_min, q_min, d)

def fuerza_bruta(puntos):
    min_d = float('inf')
    p_min = q_min = None
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            d = distancia(puntos[i], puntos[j])
            if d < min_d:
                min_d = d
                p_min, q_min = puntos[i], puntos[j]
    return (p_min, q_min, min_d)


puntos = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
puntos.sort()  
p1, p2, distancia_minima = par_mas_cercano(puntos)
print(f"Par mas cercano: {p1} y {p2}, con distancia {distancia_minima}")
