package estaticas.grafos;
import dinamicas.conjuntos.ConjuntoLD;
import tdas.ConjuntoTDA;
import tdas.GrafoTDA;

public class GrafoMA implements GrafoTDA{
    static int n = 100;
    int [][] MAdy; // Matriz de adyacencia
    int [] Etiqs; // Vector para mapeo a indices
    int cantNodos;

    public void InicializarGrafo() {
        MAdy = new int[n][n];
        Etiqs = new int[n];
        cantNodos = 0;
    }

    
    public void AgregarVertice(int v) {
        Etiqs[cantNodos] = v;
        for(int i = 0; i <= cantNodos; i++){
            MAdy[cantNodos][i] = 0;
            MAdy[i][cantNodos] = 0;
        }
        cantNodos++;
    }

    private int Vert2Indice(int v){
        int i = cantNodos - 1;
        while(i >= 0 && Etiqs[i] != v)
            i--;
        return i;
    }

    
    public void EliminarVertice(int v) {
        int ind = Vert2Indice(v);
        for (int i = 0; i < cantNodos; i++)
            MAdy[i][ind] = MAdy[i][cantNodos - 1]; // Se "pisa" la columna... 
        for (int i = 0; i < cantNodos; i++)
            MAdy[ind][i] = MAdy[cantNodos - 1][i]; // ... y la fila
        Etiqs[ind] = Etiqs[cantNodos - 1];
        cantNodos--;
    }

    
    public void AgregarArista(int v1, int v2, int p) {
        int o = Vert2Indice(v1);
        int d = Vert2Indice(v2);
        MAdy[o][d] = p;
    }

    
    public void EliminarArista(int v1, int v2) {
        int o = Vert2Indice(v1);
        int d = Vert2Indice(v2);
        MAdy[o][d] = 0;
    }

    
    public int PesoArista(int v1, int v2) {
        int o = Vert2Indice(v1);
        int d = Vert2Indice(v2);
        return MAdy[o][d];
    }

    
    public ConjuntoTDA Vertices() {
        ConjuntoTDA Vert = new ConjuntoLD();
        Vert.inicializarConjunto();
        for(int i = 0; i < cantNodos; i++)
            Vert.agregar(Etiqs[i]);
        return Vert;
    }

    
    public boolean ExisteArista(int v1, int v2) {
        int o = Vert2Indice(v1);
        int d = Vert2Indice(v2);
        return (MAdy[o][d] != 0);
    }    
}
