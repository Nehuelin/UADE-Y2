package actividades.trabajosPracticos.TP6;

import tdas.GrafoTDA;
import tdas.ConjuntoTDA;
import estaticas.grafos.GrafoMA;
import estaticas.conjuntos.ConjuntoA;
/*4) Dado un Grafo G y un vértice v, calcular el conjunto de vértices AdyacentesDobles de v. Se define que un vértice w es adyacente doble de un vértice v, si existe otro vértice x y hay una arista que comienza en v y termina en x y otra que comienza en x y termina en w 
5) Dado un vértice v de un grafo, calcular el mayor de los costos de las aristas salientes 
6) Dado un Grafo G y un vértice v, escribir un método que permita obtener el conjunto de los Predecesores del vértice v en G. Se define que un vértice o es predecesor de otro vértice d, si hay una arista que comienza en o y termina en d.
7) Dado un Grafo G escribir un método que permita obtener el conjunto de los vértices aislados en G. Se define que un vértice v es aislado si v no tiene aristas entrantes ni salientes.
8) Dado un Grafo G y dos vértices v1 y v2, escribir un método que permita obtener el conjunto de todos los vértices puente entre v1 y v2. Se define que un vértice p es puente entre dos vértices o y d, si hay una arista que comienza en o y termina en p y otra que comienza en p y termina en d.
9) Dado un Grafo G y un vértice v, calcular el grado de v. Se define el grado de un vértice v como el entero que es igual a la resta entre la cantidad de aristas que salen de v menos la cantidad de aristas que llegan a v.*/
public class TP6_1_grafos{
    public static ConjuntoTDA calcularAdyacentesDobles(GrafoTDA G, int v){
        ConjuntoTDA adyacentesDobles = new ConjuntoA();
        adyacentesDobles.inicializarConjunto();

        ConjuntoTDA vertices1 = G.Vertices();
        ConjuntoTDA vertices2 = G.Vertices();

        while(!vertices1.conjuntoVacio()){
            int x = vertices1.elegir();
            if(G.ExisteArista(v, x)){
                while(!vertices2.conjuntoVacio()){
                    int w = vertices2.elegir();
                    if(G.ExisteArista(x, w)){
                        adyacentesDobles.agregar(w);
                    }
                    vertices2.sacar(w);
                }
            }
            vertices1.sacar(x);
        }

        return adyacentesDobles;
    }
    
    public static int mayorPesoSaliente(GrafoTDA G, int v1){
        int maximo = Integer.MIN_VALUE;
        ConjuntoTDA vertices = G.Vertices();
        while(!vertices.conjuntoVacio()){
            int v2 = vertices.elegir();
            vertices.sacar(v2);
            if(G.ExisteArista(v1, v2)){
                int costo = G.PesoArista(v1, v2);
                if(costo > maximo){
                    maximo = costo;
                }
            }
        }
        return maximo;
    }

    public static ConjuntoTDA obtenerPredecesores(GrafoTDA G, int v1){
        ConjuntoTDA predecesores = new ConjuntoA();
        predecesores.inicializarConjunto();
        ConjuntoTDA vertices = G.Vertices();
        while(!vertices.conjuntoVacio()){
            int v2 = vertices.elegir();
            vertices.sacar(v2);
            if(G.ExisteArista(v2, v1)){
                predecesores.agregar(v2);
            }
        }
        return predecesores;
    }

    public static ConjuntoTDA obtenerAislados(GrafoTDA G){
        ConjuntoTDA aislados = new ConjuntoA();
        aislados.inicializarConjunto();
        ConjuntoTDA vertices1 = G.Vertices();
        while(!vertices1.conjuntoVacio()){
            boolean aislado = true;
            ConjuntoTDA vertices2 = G.Vertices();
            int v1 = vertices1.elegir();
            vertices1.sacar(v1);
            while(!vertices2.conjuntoVacio()){
                int v2 = vertices2.elegir();
                vertices2.sacar(v2);
                if(G.ExisteArista(v1, v2) || G.ExisteArista(v2, v1)){
                    aislado = false;
                    break;
                }
            }
            if(aislado)
                aislados.agregar(v1);
        }

        return aislados;
    }

    public static ConjuntoTDA obtenerPuentes(GrafoTDA G, int v1, int v2){
        ConjuntoTDA puentes = new ConjuntoA();
        puentes.inicializarConjunto();
        ConjuntoTDA vertices = G.Vertices();
        while(!vertices.conjuntoVacio()){
            int v3 = vertices.elegir();
            vertices.sacar(v3);
            if(G.ExisteArista(v1, v3) && G.ExisteArista(v3, v2)){
                puentes.agregar(v3);
            } 
        }
        
        return puentes;
    } 

    /*Se define el grado de un vértice v como el entero que es igual a la resta entre la cantidad de aristas que salen de v menos la cantidad de aristas que llegan a v.*/
    public static int obtenerGrado(GrafoTDA G, int v){
        int salientes = 0;
        int entrantes = 0;
        ConjuntoTDA vertices = G.Vertices();
        while(!vertices.conjuntoVacio()){
            int v2 = vertices.elegir();
            vertices.sacar(v2);
            if(G.ExisteArista(v, v2))
                salientes++;
            if(G.ExisteArista(v2, v))
                entrantes++;
        }
        return salientes - entrantes;
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

        ConjuntoTDA AD = calcularAdyacentesDobles(grafo, 2); // 4)
        AD.imprimirConjunto();

        int pesoMaximo = mayorPesoSaliente(grafo, 2); // 5) 
        System.out.println("PESO MAXIMO SALIENTE DE 2: "+pesoMaximo);

        ConjuntoTDA predecesores = obtenerPredecesores(grafo, 3); // 6)
        System.out.print("CONJUNTO DE VERTICES PREDECESORES DE 3: ");
        predecesores.imprimirConjunto();
        
        ConjuntoTDA aislados = obtenerAislados(grafo); // 7)
        System.out.print("CONJUNTO DE VERTICES AISLADOS: ");
        aislados.imprimirConjunto();
        
        ConjuntoTDA puentes = obtenerPuentes(grafo, 2, 1); // 7)
        System.out.print("CONJUNTO DE VERTICES PUENTE ENTRE 2 Y 1: ");
        puentes.imprimirConjunto();

        int grado = obtenerGrado(grafo, 5);
        System.out.print("GRADO DEL VERTICE 5: "+grado);
    }
}


