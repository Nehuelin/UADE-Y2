package actividades.trabajosPracticos.TP1;
import tdas.PilaTDA;
import estaticas.pilas.PilaTI;

/*2) A partir del TDA Pila definido, escribir distintos métodos que permitan
a) Pasar una Pila a otra (dejándola en orden inverso)
b) Copiar una Pila en otra (dejándola en el mismo orden que la original)
c) Invertir el contenido de una Pila.
d) Contar los elementos de una Pila
e) Sumar los elementos de una Pila
f) Calcular el promedio de los elementos de una Pila */

public class TP1_1_pilas { 
    public static void pasarPila(PilaTDA pilaOrigen, PilaTDA pilaDestino){
        while(!pilaOrigen.pilaVacia()){
            pilaDestino.apilar(pilaOrigen.tope());
            pilaOrigen.desapilar();
        }
    }

    public static void copiarPila(PilaTDA pilaOriginal, PilaTDA pilaCopia){
        PilaTDA pilaAux = new PilaTI();
        pilaAux.inicializarPila();
        pasarPila(pilaOriginal, pilaAux);
        while(!pilaAux.pilaVacia()){
            pilaCopia.apilar(pilaAux.tope());
            pilaOriginal.apilar(pilaAux.tope());
            pilaAux.desapilar();
        }
    }

    public static void invertirPila(PilaTDA pila){
        PilaTDA pilaAux = new PilaTI();
        pilaAux.inicializarPila();
        pasarPila(pila, pilaAux);
        copiarPila(pilaAux, pila);
        while(!pilaAux.pilaVacia()){
            pilaAux.desapilar();
        }
    }

    public static int contarElementosDeLaPila(PilaTDA pila){
        PilaTDA pilaAux = new PilaTI();
        pilaAux.inicializarPila();
        int i = 0;
        while(!pila.pilaVacia()){
            i++;
            pilaAux.apilar(pila.tope());
            pila.desapilar();
        }
        pasarPila(pilaAux, pila);
        return i;
    }
    
    public static int sumarElementosDeLaPila(PilaTDA pila){
        PilaTDA pilaAux = new PilaTI();
        pilaAux.inicializarPila();
        int total = 0;
        while(!pila.pilaVacia()){
            total += pila.tope();
            pilaAux.apilar(pila.tope());
            pila.desapilar();
        }
        pasarPila(pilaAux, pila);
        return total;
    }

    public static double promediarElementosDeLaPila(PilaTDA pila){
        int suma = sumarElementosDeLaPila(pila);
        int cantidad = contarElementosDeLaPila(pila);
        return (double) suma / cantidad; 
    }

    public static void main(String[] args) {
        PilaTDA pila1 = new PilaTI();
        PilaTDA pila2 = new PilaTI();
        pila1.inicializarPila();
        pila2.inicializarPila();
        pila1.apilar(1);
        pila1.apilar(2);
        pila1.apilar(3);
        pila1.apilar(4);
        pila1.apilar(5);
        pila1.apilar(6);
        pasarPila(pila1, pila2); // A)

        System.out.println();

        copiarPila(pila2, pila1); // B)

        System.out.println();

        invertirPila(pila1); // C)

        System.out.println();

        int cantidad_de_elementos = contarElementosDeLaPila(pila1); // D)
        System.out.println("CANTIDAD DE ELEMENTOS EN LA PILA 1: "+cantidad_de_elementos);

        int suma_de_elementos = sumarElementosDeLaPila(pila1); // E)
        System.out.println("SUMA TOTAL DE ELEMENTOS EN LA PILA 1: "+suma_de_elementos);

        double promedio_de_elementos = promediarElementosDeLaPila(pila1); // F)
        System.out.println("PROMEDIO DE ELEMENTOS EN LA PILA 1: "+promedio_de_elementos);
    }
}
