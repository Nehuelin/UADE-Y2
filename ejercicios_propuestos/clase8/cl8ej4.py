# Se tiene un tablero de tamaño n×n y un rey en una casilla arbitraria (x0, y0).
# Por supuesto, x0, y0 ∈ {1, ..., n}. Cada casilla (x, y) del tablero tiene asignado un peso T(x, y), de tal forma que a cada recorrido 
# τ = (x0, y0), (x1, y1), ..., (xk, yk) se le puede asignar un valor V(R) que está determinado por la siguiente expresión: V(R)= Σ(k, i=0) i·T(xi, yi)
# El problema consiste en diseñar un algoritmo que proporcione el recorrido de peso mínimo que visite todas las casillas del tablero sin repetir ninguna.
# Recuerde que un rey de ajedrez puede mover a cualquier casilla vecina en cualquier dirección.

from typing import List, Tuple
import random

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def is_within_bounds(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n

def backtrack(x: int, y: int, n: int, T: List[List[int]], visited: List[List[bool]], path: List[Tuple[int, int]], weight: int, step: int, min_path: List[Tuple[int, int]], min_weight: List[int]) -> None:
    if len(path) == n * n:
        if weight < min_weight[0]:
            min_weight[0] = weight
            min_path[:] = path[:]
    else: 
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if is_within_bounds(nx, ny, n) and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx, ny))
                
                backtrack(nx, ny, n, T, visited, path, weight + step * T[nx][ny], step + 1, min_path, min_weight)
                
                visited[nx][ny] = False
                path.pop()

def find_minimum_weight_path(n: int, x0: int, y0: int, T: List[List[int]]) -> Tuple[List[Tuple[int, int]], int]:
    visited = [[False] * n for _ in range(n)]
    min_path = []
    min_weight = [float('inf')]  
    
    visited[x0][y0] = True
    initial_path = [(x0, y0)]
    
    backtrack(x0, y0, n, T, visited, initial_path, T[x0][y0], 1, min_path, min_weight)
    
    return min_path, min_weight[0]

n = 4
x0, y0 = 2, 2

# T = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]

T = [[1, 4, 1, 5],
    [5, 5, 1, 2],
    [4, 5, 5, 2],
    [2, 4, 5, 3]]

for fila in T:
    print(fila)
    

min_path, min_weight = find_minimum_weight_path(n, x0, y0, T)
print("Minimum weight path:", min_path)
print("Minimum weight:", min_weight)
