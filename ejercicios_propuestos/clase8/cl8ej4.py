# Se tiene un tablero de tamaño n×n y un rey en una casilla arbitraria (x0, y0).
# Por supuesto, x0, y0 ∈ {1, ..., n}. Cada casilla (x,) del tablero tiene asignado un peso T(x, y), de tal forma que a cada recorrido 
# τ = (x0, y0), (x1, y1), ..., (xk, yk) se le puede asignar un valor V(R) que está determinado por la siguiente expresión: V(R)= Σ(k, i=0) i·T(xi, yi)
# El problema consiste en diseñar un algoritmo que proporcione el recorrido de peso mínimo que visite todas las casillas del tablero sin repetir ninguna.
# Recuerde que un rey de ajedrez puede mover a cualquier casilla vecina en cualquier dirección.