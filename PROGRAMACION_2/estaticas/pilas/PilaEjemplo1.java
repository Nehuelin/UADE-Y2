package estaticas.pilas;
import tdas.PilaTDA;

// pasar todos los elementos de una pila ORIGEN a una pila DESTINO
public class PilaEjemplo1 {
    public static void pasarPila(PilaTDA origen, PilaTDA destino){
        while(!origen.pilaVacia()){
            destino.apilar(origen.tope());
            origen.desapilar();
        }
    }

    public static void main(String[] args) {
        PilaTDA origen = new PilaTF();
        PilaTDA destino = new PilaTF();
        origen.inicializarPila();
        origen.apilar(1);
        origen.apilar(2);
        origen.apilar(3);
        destino.inicializarPila();
        pasarPila(origen, destino);
    }
}
