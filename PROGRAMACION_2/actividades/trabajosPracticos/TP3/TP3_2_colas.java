package actividades.trabajosPracticos.TP3;
import tdas.*;
import estaticas.colas.ColaPI;
import estaticas.conjuntos.ConjuntoA;

/*Eliminar de una Cola C las repeticiones de elementos, dejando un representante
de cada uno de los elementos presentes originalmente. Se deberá respetar el
orden original de los elementos, y en el caso de los repetidos se conservará el
primero que haya ingresado en C.
b) Repartir una Cola C en dos mitades M1 y M2 de elementos consecutivos,
respetando el orden. Asumir que la cantidad de elementos de C es par.
c) Generar el conjunto de elementos que se repiten en una Cola */

public class TP3_2_colas {
    public static void eliminarRepetidos(ColaTDA cola){
        ColaTDA colaAux = new ColaPI();
        colaAux.inicializarCola();
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();

        while(!cola.colaVacia()){
            int elemento = cola.primero();
            if(!c.pertenece(elemento)){
                c.agregar(elemento);
                colaAux.acolar(elemento);
            }
            cola.desacolar();
        }

        while(!colaAux.colaVacia()){
            cola.acolar(colaAux.primero());
            colaAux.desacolar();
        }
    }

    public static void dividirCola(ColaTDA cola, ColaTDA M1, ColaTDA M2){
        ColaTDA colaAux = new ColaPI();
        colaAux.inicializarCola();
        int contador = 0;

        while(!cola.colaVacia()){
            colaAux.acolar(cola.primero());
            cola.desacolar();
            contador++;
        }

        if(contador % 2 != 0){
            while(!colaAux.colaVacia()){
                cola.acolar(colaAux.primero());
                colaAux.desacolar();
            }
            System.out.println("LA COLA TIENE CANTIDAD IMPAR DE ELEMENTOS");
            return;
        }

        int mitad = contador / 2;
        contador = 0;

        while(contador < mitad){
            M1.acolar(colaAux.primero());
            colaAux.desacolar();
            contador++;
        }
        while(!colaAux.colaVacia()){
            M2.acolar(colaAux.primero());
            colaAux.desacolar();         
        }
    }
    
    public static ConjuntoTDA juntarRepetidos(ColaTDA cola){
        ColaTDA colaAux = new ColaPI();
        colaAux.inicializarCola();
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();
        ConjuntoTDA r = new ConjuntoA();
        r.inicializarConjunto();

        while(!cola.colaVacia()){
            int elemento = cola.primero();
            if(!c.pertenece(elemento)){
                c.agregar(elemento);
            } else {
                r.agregar(elemento);
            }
            colaAux.acolar(elemento);
            cola.desacolar();
        }

        while(!colaAux.colaVacia()){
            cola.acolar(colaAux.primero());
            colaAux.desacolar();
        }

        return r;
    }

    public static void main(String[] args) {
        ColaTDA cola = new ColaPI();
        cola.inicializarCola();
        cola.acolar(1);
        cola.acolar(2);
        cola.acolar(3);
        cola.acolar(2);
        cola.acolar(5);
        cola.acolar(3);

        System.out.print("COLA: ");
        cola.imprimirCola();

        eliminarRepetidos(cola); // a)
        System.out.print("COLA SIN ELEMENTOS REPETIDOS: ");
        cola.imprimirCola();

        ColaTDA cola2 = new ColaPI();
        cola2.inicializarCola();
        ColaTDA cola3 = new ColaPI();
        cola3.inicializarCola();

        dividirCola(cola, cola2, cola3); // b)
        System.out.print("M1: ");
        cola2.imprimirCola();
        System.out.print("M2: ");
        cola3.imprimirCola();

        cola.acolar(1);
        cola.acolar(2);
        cola.acolar(3);
        cola.acolar(2);
        cola.acolar(5);
        cola.acolar(3);

        ConjuntoTDA repetidos = juntarRepetidos(cola);
        System.out.print("ELEMENTOS REPETIDOS DE LA COLA: ");
        repetidos.imprimirConjunto();
    }
}
