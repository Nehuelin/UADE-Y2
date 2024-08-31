package dinamicas.colas;
import estaticas.colas.ColaPI;
import tdas.ColaTDA;

public class ColaLD implements ColaTDA{
    class Nodo {
        int info;
        Nodo sig;
    }

    Nodo primero;
    Nodo ultimo;

    public void inicializarCola(){
        primero = null;
        ultimo = null;
    }

    public void acolar(int x){
        Nodo nuevo = new Nodo();
        nuevo.info = x;
        nuevo.sig = null;
        if (ultimo != null){
            ultimo.sig = nuevo;
        }
        ultimo = nuevo;
        if (primero == null){
            primero = nuevo;
        } 
    }

    public void desacolar(){
        primero = primero.sig;
        if (primero == null){
            ultimo = null;
        }
    }

    public boolean colaVacia(){
        return (ultimo == null);
    }

    public int primero(){
        return primero.info;
    }

    public void imprimirCola(){
        ColaTDA cAux = new ColaPI();
        cAux.inicializarCola();

        System.out.print("[");
        while(!this.colaVacia()){
            int elemento = this.primero();
            this.desacolar();
            if(!this.colaVacia()){
                System.out.print(elemento+", ");
            }else{
                System.out.print(elemento);
            }
            cAux.acolar(elemento);
        }
        System.out.print("]\n");

        while(!cAux.colaVacia()){
            this.acolar(cAux.primero());
            cAux.desacolar();
        }
    }
}
