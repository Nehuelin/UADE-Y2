package estaticas.diccionariosSimples;

import tdas.DiccionarioSimpleTDA;
import tdas.ConjuntoTDA;
import estaticas.conjuntos.ConjuntoA;

public class DiccionarioSimpleA implements DiccionarioSimpleTDA{
    private Elemento[] elementos;
    private int cant;

    public void inicializarDiccionario() {
        elementos = new Elemento[100];
        cant = 0;
    }

    public void agregar(int clave, int valor){
        int pos = clave2Indice(clave);
        if (pos == -1){
            pos = cant;
            elementos[pos] = new Elemento();
            elementos[pos].clave = clave;
            cant++;
        }
        elementos[pos].valor = valor;
    }

    private int clave2Indice(int clave){
        int i = cant - 1;
        while (i >= 0 && elementos[i].clave != clave){
            i--;
        }
        return i;
    }

    public void eliminar(int clave){
        int pos = clave2Indice(clave);
        if (pos == -1){
            elementos[pos] = elementos[cant - 1];
            cant--;
        }        
    }

    public int recuperar(int clave){
        int pos = clave2Indice(clave);
        return elementos[pos].valor;
    }

    public ConjuntoTDA claves(){
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();
        for(int i = 0; i < cant; i++){
            c.agregar(elementos[i].clave);
        }
        return c;
    }

    public void imprimirDiccionario(){
        ConjuntoTDA claves = this.claves();
        while(!claves.conjuntoVacio()){
            int clave = claves.elegir();
            int valor = this.recuperar(clave);
            System.out.print(clave +": "+valor+"\n");
            claves.sacar(clave);
        }
    }
}
