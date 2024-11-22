from DFS import DFS  
from Grafo import Grafo 

def main():
    dfs = DFS()

    try:
        with open(r"trabajos_practicos\centros_de_distribucion\rutas.txt", "r") as file:
            grafo = Grafo()

            for line in file:
                line = line.strip()
                if line != "156\t#Total de rutas":
                    datos = line.split(",")
                    grafo.agregar_vertice(int(datos[0]))
                    grafo.agregar_arista(int(datos[0]), int(datos[1]), int(datos[2]))
        
        grafo2 = grafo 
        camino_corto = []

        dfs.camino_corto(grafo, 42, camino_corto, 0, 9999999)

        while grafo2.vertices(): 
            v = grafo2.vertices().pop()  
            dfs.camino_corto(grafo, v, camino_corto, 0, 9999999)
            grafo2.eliminar_vertice(v)

            # while camino_corto:
            #     print(camino_corto.pop())

    except IOError as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    main()