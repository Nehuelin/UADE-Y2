package actividades.trabajosPracticos.TP3;
import tdas.*;
import estaticas.pilas.PilaTF;
import estaticas.colas.ColaPI;
import estaticas.conjuntos.ConjuntoA;

/*A partir del TDA Pila, escribir distintos métodos externos que permitan:
a) Comprobar si una Pila P es capicúa (el elemento del tope es igual al de la base,
el segundo igual al anteúltimo, etc.)
b) Eliminar de una Pila P las repeticiones de elementos, dejando un representante
de cada uno de los elementos presentes originalmente. Se deberá respetar el
orden original de los elementos, y en el caso de los repetidos se conservará el
primero que haya ingresado en P.
c) Repartir una Pila P en dos mitades M1 y M2 de elementos consecutivos,
respetando el orden. Asumir que la Pila P contiene un número par de elementos.
d) Generar el conjunto de elementos que se repiten en una Pila. */

public class TP3_1_pilas {
    public static boolean esCapicua(PilaTDA p){
        PilaTDA pAux = new PilaTF();
        pAux.inicializarPila();
        ColaTDA cAux = new ColaPI();
        cAux.inicializarCola();

        boolean capicua = true;
        while(!p.pilaVacia()){
            int elemento = p.tope();
            pAux.apilar(elemento);
            cAux.acolar(elemento);
            p.desapilar();
        }
        while(!pAux.pilaVacia() && capicua){
            if(pAux.tope() == cAux.primero()){
                p.apilar(cAux.primero());
                pAux.desapilar();
                cAux.desacolar();
            }else{
                capicua = false;
            }
        }
        while(!cAux.colaVacia()){
            p.apilar(cAux.primero());
            cAux.desacolar();
        }

        return capicua;
    }

    public static void eliminarRepetidos(PilaTDA p){
        PilaTDA pAux = new PilaTF();
        pAux.inicializarPila();
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();

        while(!p.pilaVacia()){
            int elemento = p.tope();
            if(!c.pertenece(elemento)){
                c.agregar(elemento);
                pAux.apilar(elemento);
            }
            p.desapilar();
        }
        while(!pAux.pilaVacia()){
            p.apilar(pAux.tope());
            pAux.desapilar();
        }
    }

    public static void dividirPila(PilaTDA p, PilaTDA M1, PilaTDA M2){
        PilaTDA pAux = new PilaTF();
        pAux.inicializarPila();

        int contador = 0;
        while(!p.pilaVacia()){
            pAux.apilar(p.tope());
            p.desapilar();
            contador++;
        }
        
        if(contador % 2 != 0){
            while(!pAux.pilaVacia()){
                p.apilar(pAux.tope());
                pAux.desapilar();
            }
            System.out.println("LA PILA NO TIENE CANTIDAD PAR DE ELEMENTOS");
            return;
        }

        int mitad = contador / 2;
        contador = 0;

        while(contador < mitad){
            int elemento = pAux.tope();
            M1.apilar(elemento);
            pAux.desapilar();
            contador++;
        }
        while(!pAux.pilaVacia()){
            int elemento = pAux.tope();
            M2.apilar(elemento);
            pAux.desapilar();
        }
    }

    public static ConjuntoTDA juntarRepetidos(PilaTDA p){
        PilaTDA pAux = new PilaTF();
        pAux.inicializarPila();
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();
        ConjuntoTDA r = new ConjuntoA();
        r.inicializarConjunto();

        while(!p.pilaVacia()){
            int elemento = p.tope();
            if(!c.pertenece(elemento)){
                c.agregar(elemento);
            } else {
                r.agregar(elemento);
            }
            pAux.apilar(elemento);
            p.desapilar();
        }

        while(!pAux.pilaVacia()){
            int elemento = pAux.tope();
            p.apilar(elemento);
            pAux.desapilar();
        }

        return r;
    }

    public static void main(String[] args) {
        PilaTDA pila1 = new PilaTF();
        pila1.inicializarPila();
        pila1.apilar(1);
        pila1.apilar(2);
        pila1.apilar(3);
        pila1.apilar(2);
        pila1.apilar(1);
        
        System.out.print("PILA: ");
        pila1.imprimirPila();

        if(esCapicua(pila1)){ // a)
            System.out.println("LA PILA ES CAPICUA");
        }else{
            System.out.println("LA PILA NO ES CAPICUA");
        }

        eliminarRepetidos(pila1); // b)
        System.out.print("PILA SIN ELEMENTOS REPETIDOS: ");
        pila1.imprimirPila();

        PilaTDA pila2 = new PilaTF();
        PilaTDA pila3 = new PilaTF();

        pila2.inicializarPila();
        pila3.inicializarPila();

        pila1.apilar(4);

        dividirPila(pila1, pila2, pila3); // c)

        System.out.print("PILA M1: ");
        pila2.imprimirPila();
        
        System.out.print("PILA M2: ");
        pila3.imprimirPila();

        pila1.apilar(1);
        pila1.apilar(2);
        pila1.apilar(3);
        pila1.apilar(2);
        pila1.apilar(1);

        ConjuntoTDA repetidos = juntarRepetidos(pila1); // d) 
        System.out.print("ELEMENTOS REPETIDOS: ");
        repetidos.imprimirConjunto();
    }
}
