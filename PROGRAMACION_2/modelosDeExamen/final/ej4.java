import tdas.*;
import estaticas.grafos.GrafoMA;

public class ej4 {
    public static int obtenerMayorCostoEntrante(GrafoTDA G, int vO){ // vO --> vertice objetivo, vX --> vertice del conjunto
        int mayor = 0;
        ConjuntoTDA vertices = G.Vertices();
        while(!vertices.conjuntoVacio()){
            int vX = vertices.elegir();
            vertices.sacar(vX);
            int peso = G.PesoArista(vX, vO);
            if(peso > mayor)
                mayor = peso;
        }
        return mayor;
    }

    public static void main(String[] args) {
        GrafoTDA grafo = new GrafoMA();
        grafo.InicializarGrafo();
        grafo.AgregarVertice(1);
        grafo.AgregarVertice(2);
        grafo.AgregarVertice(3);
        grafo.AgregarVertice(4);
        grafo.AgregarVertice(5);
        grafo.AgregarVertice(6);
        grafo.AgregarArista(1, 2, 1);
        grafo.AgregarArista(2, 4, 4);
        grafo.AgregarArista(2, 5, 2);
        grafo.AgregarArista(3, 3, 1);
        grafo.AgregarArista(4, 1, 3);
        grafo.AgregarArista(4, 2, 3);
        grafo.AgregarArista(5, 4, 6);
        grafo.AgregarArista(5, 3, 2);

        int peso = obtenerMayorCostoEntrante(grafo, 4);
        System.out.println(peso);
    }
}

/*ESTRATEGIA: 
1) Se obtiene el conjunto de vertices del grafo
2) Para cada vertice, se obtiene el peso de la arista que sale del vertice del conjunto y llega al vertice objetivo
--> Si el peso supera a la variable mayor en ese momento, ese peso se convierte en el nuevo mayor
--> Sino, continua el bucle hasta que se investigan todos los vertices del grafo 
*/