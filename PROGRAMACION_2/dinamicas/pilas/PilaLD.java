package dinamicas.pilas;
import estaticas.colas.ColaPI;
import tdas.ColaTDA;
import tdas.PilaTDA;

public class PilaLD implements PilaTDA{
    class Nodo {
        int info;
        Nodo sig;
    }

    Nodo primero;

    public void inicializarPila() {
        primero = null;
    }

    public void apilar(int x){
        Nodo nuevo = new Nodo();
        nuevo.info = x;
        nuevo.sig = primero;
        primero = nuevo;
    }

    public void desapilar(){
        primero = primero.sig;
    }

    public boolean pilaVacia(){
        return (primero == null);
    }

    public int tope(){
        return primero.info;
    }

    public void imprimirPila(){
        ColaTDA cola = new ColaPI();
        cola.inicializarCola();

        System.out.print("[");
        while(!this.pilaVacia()){
            int elemento = this.tope();
            this.desapilar();
            if(!this.pilaVacia()){
                System.out.print(elemento+", ");
            }else{
                System.out.print(elemento);
            }
            cola.acolar(elemento);
        }
        System.out.print("]\n");

        while(!cola.colaVacia()){
            this.apilar(cola.primero());
            cola.desacolar();
        }
    }
}
