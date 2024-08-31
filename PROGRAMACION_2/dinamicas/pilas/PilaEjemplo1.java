package dinamicas.pilas;
import tdas.PilaTDA;

// Pasar todos los elementos de una pila ORIGEN a una pila DESTINO
public class PilaEjemplo1 {

    public static void main(String[] args) {
        PilaTDA pila1 = new PilaLD();
        PilaTDA pila2 = new PilaLD();
        pila1.inicializarPila();
        pila2.inicializarPila();
        pila1.apilar(1);
        pila1.apilar(2);
        pila1.apilar(3);
        pila1.apilar(4);
        pila1.apilar(5);
        pasarElementos(pila1, pila2);
        System.out.println();
    }

    public static void pasarElementos(PilaTDA origen, PilaTDA destino){
        while(origen.pilaVacia() != true){
            destino.apilar(origen.tope());
            origen.desapilar();
        }
    }
}

// void inicializarPila();
// void apilar(int x);
// void desapilar();
// boolean pilaVacia();
// int tope();