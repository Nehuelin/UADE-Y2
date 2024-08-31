package dinamicas.diccionariosSimples;

import dinamicas.conjuntos.ConjuntoLD;
import tdas.DiccionarioSimpleTDA;
import tdas.ConjuntoTDA;


public class DiccionarioSimpleLD implements DiccionarioSimpleTDA{
    private class NodoClave {
        int clave;
        int valor;
        NodoClave sigClave;
    }

    private NodoClave origen; // referencia de la estructura

    public void inicializarDiccionario(){
        origen = null;
    }

    public void agregar(int clave, int valor){
        NodoClave nc = clave2NodoClave(clave);
        if (nc == null) { // si la clave no existe
            nc = new NodoClave();
            nc.clave = clave;
            nc.sigClave = origen;
            origen = nc; // nuevo origen
        }
        nc.valor = valor;
    }

    private NodoClave clave2NodoClave(int clave){
        NodoClave aux = origen;
        while (aux != null && aux.clave != clave){
            aux = aux.sigClave;
        }
        return aux;
    }

    public void eliminar(int clave){
        if (origen != null){ 
            if (origen.clave == clave) { // Es el primero
                origen = origen.sigClave;
            } else { // Es algun otro
                NodoClave aux = origen;
                while (aux.sigClave != null && aux.sigClave.clave != clave) {
                    aux = aux.sigClave;
                }
                if (aux.sigClave != null) {
                    aux.sigClave = aux.sigClave.sigClave;
                }
            }
        }
    }

    public int recuperar(int clave){
        NodoClave nc = clave2NodoClave(clave);
        return nc.valor;
    }

    public ConjuntoTDA claves(){
        ConjuntoTDA c = new ConjuntoLD();
        c.inicializarConjunto();
        NodoClave aux = origen;
        while (aux != null){
            c.agregar(aux.clave);
            aux = aux.sigClave;
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
