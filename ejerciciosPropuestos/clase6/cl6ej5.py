# El paseo probabilístico:
# El párroco de la iglesia de San Hilario en Fraile Muerto es conocido por ser una persona de costumbres sistemáticas. 
# Todos los días, luego de su inevitable siesta, 
# se dirige desde su casa (situada en la esquina noroeste en el mapa del centro de la ciudad (posición M[0, 0]) a su 
# iglesia situada en el extremo opuesto, es decir la esquina sudeste del mapa (posición M[m − 1, n − 1].) 
# El mapa del centro de la ciudad de Fraile Muerto, como el de tantas otras ciudades de la Pampa, es una cuadrícula M de m filas por n columnas.
# Su recorrido se dirige hacia el este o hacia el sur (nunca vuelve hacia el oeste ni hacia el norte.) 
# La probabilidad de que en un punto dado se dirija hacia el este es del 40 %; 
# la probabilidad de que se dirija hacia el sur es del 60 %. 
# Por supuesto, una vez que llega al extremo sur (fila m − 1), la probabilidad de tomar hacia el este es del 100 % y análogamente cuando llega al extremo este.
# Describa una estrategia de programación dinámica para determinar la probabilidad de que el cura pase por un punto M[y, y] dado con x ∈ {0, ..., m-1}, y ∈ {0, ..., n-1}.



def crearMatriz(m, n):
    # Inicializamos la matriz de probabilidades
    matriz = []
    for i in range(m):
        matriz.append([0] * n)
    matriz[0][0] = 1
    # Calculamos las probabilidades
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                matriz[i][j] = matriz[i][j - 1] * 0.4
            elif j == 0:
                matriz[i][j] = matriz[i - 1][j] * 0.6
            else:
                matriz[i][j] = matriz[i - 1][j] * 0.6 + matriz[i][j - 1] * 0.4
    return matriz

def probabilidad(m, n, y, x):
    matriz = crearMatriz(m, n)
    return matriz[y][x]

def main():
    m = 5
    n = 5
    matriz = crearMatriz(m, n)
    for i in range(m):
        for j in range(n):
            print(f'{matriz[i][j]:.2f}', end=' ')
        print()
    print(probabilidad(m, n, 3, 3))
if __name__ == '__main__':
    main()


