package actividades.trabajosPracticos.TP3;
import tdas.*;
import estaticas.conjuntos.ConjuntoA;
import estaticas.pilas.PilaTI;
import estaticas.colas.ColaPI;

/*a) Calcular la diferencia simétrica entre dos conjuntos A y B sin utilizar las operaciones unión, intersección y diferencia.
b) Calcular la diferencia simétrica entre dos conjuntos A y B utilizando las operaciones unión, intersección y diferencia.
c) Determinar si dos conjuntos son iguales.
d) Calcular la cardinalidad (cantidad de elementos) de un conjunto.
e) Generar el conjunto de elementos que están tanto en la Pila P y en la Cola C.
f) Determinar si los elementos de una Pila P son los mismos que los de una Cola
C. No interesa el orden ni si están repetidos o no. */

public class TP3_3_conjuntos {
    private static ConjuntoTDA union(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
        ConjuntoTDA conjunto3 = new ConjuntoA();
        conjunto3.inicializarConjunto();

        while(!conjunto1.conjuntoVacio()){
            int elemento = conjunto1.elegir();
            conjunto3.agregar(elemento);
            conjunto1.sacar(elemento);
        }
        while(!conjunto2.conjuntoVacio()){
            int elemento = conjunto2.elegir();
            conjunto3.agregar(elemento);
            conjunto2.sacar(elemento);
        }

        return conjunto3;
    }

    private static ConjuntoTDA intersección(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
        ConjuntoTDA conjunto3 = new ConjuntoA();
        conjunto3.inicializarConjunto();

        while(!conjunto1.conjuntoVacio()){
            int elemento = conjunto1.elegir();
            if (conjunto2.pertenece(elemento)){
                conjunto3.agregar(elemento);
                conjunto2.sacar(elemento);
            }
            conjunto1.sacar(elemento);
        }
        while(!conjunto2.conjuntoVacio()){
            conjunto2.sacar(conjunto2.elegir());
        }

        return conjunto3;
    }
    
    private static ConjuntoTDA diferencia(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
        ConjuntoTDA conjunto3 = new ConjuntoA();
        conjunto3.inicializarConjunto();

        while(!conjunto1.conjuntoVacio()){
            int elemento1 = conjunto1.elegir();
            if (!conjunto2.pertenece(elemento1)){
                conjunto3.agregar(elemento1);
            }      
            conjunto1.sacar(elemento1);
            conjunto2.sacar(elemento1);
        }

        return conjunto3;
    }

    public static ConjuntoTDA diferenciaSimetrica1(ConjuntoTDA c1, ConjuntoTDA c2){
        ConjuntoTDA c3 = new ConjuntoA();
        c3.inicializarConjunto();
        while(!c1.conjuntoVacio()){
            int elemento1 = c1.elegir();
            int elemento2 = c2.elegir();
            if(!c2.pertenece(elemento1)){
                c3.agregar(elemento1);
                c3.agregar(elemento2);
            }
            c1.sacar(elemento1);
            c2.sacar(elemento2);
        }
        return c3;
    }

    public static ConjuntoTDA diferenciaSimetrica2(ConjuntoTDA c1, ConjuntoTDA c2){
        ConjuntoTDA c3 = union(diferencia(c1, c2), diferencia(c2, c1));
        return c3;
    }

    public static boolean sonConjuntosIguales(ConjuntoTDA c1, ConjuntoTDA c2){
        ConjuntoTDA c1Aux = new ConjuntoA();
        c1Aux.inicializarConjunto();
        ConjuntoTDA c2Aux = new ConjuntoA();
        c2Aux.inicializarConjunto();
        boolean conjuntosIguales = true;

        while(!c1.conjuntoVacio() && conjuntosIguales == true){
            int elemento1 = c1.elegir();
            int elemento2 = c2.elegir();
            if(c1.pertenece(elemento2) && c2.pertenece(elemento1)){
                c1Aux.agregar(elemento1);
                c2Aux.agregar(elemento2);
                c1.sacar(elemento1);
                c2.sacar(elemento1);
                c1.sacar(elemento2);
                c2.sacar(elemento2);
            } else {
                conjuntosIguales = false;
            }
        }
        while(!c1Aux.conjuntoVacio()){
            int elemento = c1Aux.elegir();
            c1.agregar(elemento);
            c1Aux.sacar(elemento);
        }
        while(!c2Aux.conjuntoVacio()){
            int elemento = c2Aux.elegir();
            c2.agregar(elemento);
            c2Aux.sacar(elemento);
        }

        return conjuntosIguales;
    }

    public static int cardinalidad(ConjuntoTDA c){
        ConjuntoTDA cAux = new ConjuntoA();
        cAux.inicializarConjunto();
        int cantidad = 0;
        
        while(!c.conjuntoVacio()){
            int elemento = c.elegir();
            cAux.agregar(elemento);
            c.sacar(elemento);
            cantidad++;
        }

        return cantidad;
    }

    public static ConjuntoTDA juntarPilaCola(PilaTDA p, ColaTDA cola){
        ConjuntoTDA c1 = new ConjuntoA();
        c1.inicializarConjunto();
        ConjuntoTDA c2 = new ConjuntoA();
        c2.inicializarConjunto();

        while(!p.pilaVacia()){
            int elemento = p.tope();
            c1.agregar(elemento);
            p.desapilar();
        }
        while(!cola.colaVacia()){
            int elemento = cola.primero();
            c2.agregar(elemento);
            cola.desacolar();
        }
        return intersección(c1, c2);
    }

    public static boolean tienenMismosElementos(PilaTDA p, ColaTDA cola){
        ConjuntoTDA c1 = new ConjuntoA();
        c1.inicializarConjunto();
        ConjuntoTDA c2 = new ConjuntoA();
        c2.inicializarConjunto();
        PilaTDA pAux = new PilaTI();
        pAux.inicializarPila();
        ColaTDA colaAux = new ColaPI();
        colaAux.inicializarCola();

        while(!p.pilaVacia()){
            int elemento = p.tope();
            c1.agregar(elemento);
            pAux.apilar(elemento);
            p.desapilar();
        }
        while(!cola.colaVacia()){
            int elemento = cola.primero();
            c2.agregar(elemento);
            colaAux.acolar(elemento);
            cola.desacolar();
        }

        boolean mismosElementos = sonConjuntosIguales(c1, c2);

        while(!pAux.pilaVacia()){
            p.apilar(pAux.tope());
            pAux.desapilar();
        }
        while(!colaAux.colaVacia()){
            cola.acolar(colaAux.primero());
            colaAux.desacolar();
        }

        return mismosElementos;
    }
    public static void main(String[] args) {
        ConjuntoTDA conj1 = new ConjuntoA();
        conj1.inicializarConjunto();
        ConjuntoTDA conj2 = new ConjuntoA();
        conj2.inicializarConjunto();

        conj1.agregar(1);
        conj1.agregar(2);
        conj1.agregar(3);
        conj1.agregar(4);
        conj1.agregar(5);

        conj2.agregar(1);
        conj2.agregar(7);
        conj2.agregar(9);
        conj2.agregar(4);
        conj2.agregar(5);

        System.out.print("CONJUNTO 1: ");
        conj1.imprimirConjunto();
        System.out.print("CONJUNTO 2: ");
        conj2.imprimirConjunto();

        ConjuntoTDA conjDS1 = diferenciaSimetrica1(conj1, conj2); // a)
        System.out.print("DIFERENCIA SIMETRICA: ");
        conjDS1.imprimirConjunto();
        
        conj1.agregar(1);
        conj1.agregar(2);
        conj1.agregar(3);
        conj1.agregar(4);
        conj1.agregar(5);

        conj2.agregar(1);
        conj2.agregar(7);
        conj2.agregar(9);
        conj2.agregar(4);
        conj2.agregar(5);

        ConjuntoTDA conjDS2 = diferenciaSimetrica2(conj1, conj2); // b)
        System.out.print("DIFERENCIA SIMETRICA: ");
        conjDS2.imprimirConjunto();
        
        conj1.agregar(1);
        conj1.agregar(2);
        conj1.agregar(3);
        conj1.agregar(4);
        conj1.agregar(5);

        conj2.agregar(1);
        conj2.agregar(2);
        conj2.agregar(3);
        conj2.agregar(4);
        conj2.agregar(5);

        System.out.print("CONJUNTO 1: ");
        conj1.imprimirConjunto();
        System.out.print("CONJUNTO 2: ");
        conj2.imprimirConjunto();

        boolean iguales = sonConjuntosIguales(conj1, conj2); // c)
        if(iguales){
            System.out.println("LOS CONJUNTOS SON IGUALES");
        }else{
            System.out.println("LOS CONJUNTOS NO SON IGUALES");
        }

        int cantidadElementos = cardinalidad(conj1); // d)
        System.out.println("CARDINALIDAD DEL CONJUNTO 1: " + cantidadElementos);

        PilaTDA pila = new PilaTI();
        pila.inicializarPila();
        pila.apilar(1);
        pila.apilar(2);
        pila.apilar(3);
        pila.apilar(4);
        pila.apilar(5);
        System.out.print("PILA: ");
        pila.imprimirPila();

        ColaTDA cola = new ColaPI();
        cola.inicializarCola();
        cola.acolar(1);
        cola.acolar(5);
        cola.acolar(3);
        System.out.print("COLA: ");
        cola.imprimirCola();

        ConjuntoTDA pilaAndCola = juntarPilaCola(pila, cola); // e)
        System.out.print("CONJUNTO DE ELEMENTO EN PILA Y COLA: ");
        pilaAndCola.imprimirConjunto();

        pila.apilar(1);
        pila.apilar(2);
        pila.apilar(3);
        pila.apilar(4);
        pila.apilar(5);
        System.out.print("PILA: ");
        pila.imprimirPila();

        cola.acolar(1);
        cola.acolar(2);
        cola.acolar(3);
        cola.acolar(4);
        cola.acolar(5);
        System.out.print("COLA: ");
        cola.imprimirCola();

        boolean coinciden = tienenMismosElementos(pila, cola); // f)
        if(coinciden){
            System.out.println("LA PILA Y LA COLA COMPARTEN LOS MISMOS ELEMENTOS");
        }else{
            System.out.println("LA PILA Y LA COLA NO COMPARTEN LOS MISMOS ELEMENTOS");
        }

    }
}

