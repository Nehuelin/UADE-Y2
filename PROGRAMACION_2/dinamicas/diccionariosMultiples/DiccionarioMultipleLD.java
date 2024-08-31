package dinamicas.diccionariosMultiples;

import dinamicas.conjuntos.ConjuntoLD;
import tdas.ConjuntoTDA;
import tdas.DiccionarioMultipleTDA;

public class DiccionarioMultipleLD implements DiccionarioMultipleTDA{
    private class NodoClave {
        int clave;
        NodoValor valores;
        NodoClave sigClave;
    }

    private class NodoValor {
        int valor;
        NodoValor sigValor;
    }

    private NodoClave origen;

    public void inicializarDiccionario(){
        origen = null;
    }

    private NodoClave clave2NodoClave(int clave) {
        NodoClave aux = origen;
        while (aux != null && aux.clave != clave){
            aux = aux.sigClave;
        }
        return aux;
    }

    public void agregar(int clave, int valor){
        NodoClave nc = clave2NodoClave(clave);
        if (nc == null) {
            nc = new NodoClave();
            nc.clave = clave;
            nc.sigClave = origen;
            origen = nc; // nuevo origen
        }
        NodoValor aux = nc.valores; // nodo viajero
        while (aux != null && aux.valor != valor){
            aux = aux.sigValor;
        }
        if (aux == null){
            NodoValor nv = new NodoValor();
            nv.valor = valor;
            nv.sigValor = nc.valores;
            nc.valores = nv; // nuevo origen de valores
        }
    }

    public void eliminar(int clave){
        if (origen != null){
            if (origen.clave == clave){
                origen = origen.sigClave;
            } else {
                NodoClave aux = origen;
                while (aux.sigClave != null && aux.sigClave.clave != clave){
                    aux = aux.sigClave;
                }
                if (aux.sigClave != null){
                    aux.sigClave = aux.sigClave.sigClave;
                }
            }
        }
    }

    private void eliminarValorEnNodo(NodoClave nodo, int valor){
        if (nodo.valores != null) {
            if (nodo.valores.valor == valor) {
                nodo.valores = nodo.valores.sigValor;
            } else {
                NodoValor aux = nodo.valores;
                while (aux.sigValor != null && aux.sigValor.valor != valor){
                    aux = aux.sigValor;
                }
                if (aux.sigValor != null){
                    aux.sigValor = aux.sigValor.sigValor;
                }
            }
        }
    }

    public void eliminarValor(int clave, int valor){
        if (origen != null) {
            if (origen.clave == clave) { // Si es el primero...
                eliminarValorEnNodo(origen, valor);
                if(origen.valores == null){ // Si quedo vacio...
                    origen = origen.sigClave;
                }
            } else { // Es en algun otro
                NodoClave aux = origen;
                while (aux.sigClave != null && aux.sigClave.clave != clave){
                    aux = aux.sigClave;
                }
                if (aux.sigClave != null) {
                    eliminarValorEnNodo(aux.sigClave, valor);
                    if (aux.sigClave.valores == null){ // Si quedo vacio...
                        aux.sigClave = aux.sigClave.sigClave;
                    }
                }
            }
        }
    }

    public ConjuntoTDA recuperar(int clave) {
        NodoClave nc = clave2NodoClave(clave);
        ConjuntoTDA c = new ConjuntoLD();
        c.inicializarConjunto();
        if (nc != null){
            NodoValor aux = nc.valores;
            while (aux != null) {
                c.agregar(aux.valor);
                aux = aux.sigValor;
            }
        }
        return c;
    }

    public ConjuntoTDA claves() {
        ConjuntoTDA c = new ConjuntoLD();
        c.inicializarConjunto();
        NodoClave aux = origen;
        while (aux != null) {
            c.agregar(aux.clave);
            aux = aux.sigClave;
        }
        return c;
    }

    public void imprimirDiccionario(){
        ConjuntoTDA claves = this.claves();
        while(!claves.conjuntoVacio()){
            int clave = claves.elegir();
            ConjuntoTDA valores = this.recuperar(clave);
            System.out.print(clave +": ");
            valores.imprimirConjunto();
            claves.sacar(clave);
        }
    }
}  
