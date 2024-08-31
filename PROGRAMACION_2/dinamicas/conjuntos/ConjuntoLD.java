package dinamicas.conjuntos;

import tdas.ConjuntoTDA;

public class ConjuntoLD implements ConjuntoTDA {
    private class Nodo {
        int info;
        Nodo sig;
    }

    private Nodo c;

    public void inicializarConjunto(){
        c = null;
    }

    public int elegir(){
        return c.info;
    }

    public void sacar(int x){
        if (c != null){
            if (c.info == x){ // Es el primero
                c = c.sig;
            } else { // buscamos otro
                Nodo aux = c;   
                while (aux.sig != null && aux.sig.info != x){ 
                    aux = aux.sig;
                }
                if (aux.sig != null) {
                    aux.sig = aux.sig.sig;
                }
            }
        }
    }

    public void agregar(int x) {
        if (!this.pertenece(x)) { // Se verifica pertenencia
            Nodo nuevo = new Nodo(); // Creamos nodo que se agregara
            nuevo.info = x;
            nuevo.sig = c;
            c = nuevo;
        }
    }

    public boolean pertenece(int x) {
        Nodo aux = c;
        while (aux != null && aux.info != x) {
            aux = aux.sig;
        }
        return (aux != null);
    }

    public boolean conjuntoVacio(){
        return (c == null);
    }

    public void imprimirConjunto(){
        ConjuntoTDA conjAux = new ConjuntoLD();
        conjAux.inicializarConjunto();
        System.out.print("[");
        while(!this.conjuntoVacio()){
            int elemento = this.elegir();
            conjAux.agregar(elemento);
            this.sacar(elemento);
            if(!this.conjuntoVacio()){
                System.out.print(elemento+", ");
            }else{
                System.out.print(elemento);
            }
        }
        System.out.print("]\n");
        while(!conjAux.conjuntoVacio()){
            int elemento = conjAux.elegir();
            this.agregar(elemento);
            conjAux.sacar(elemento);
        }
    }
}
