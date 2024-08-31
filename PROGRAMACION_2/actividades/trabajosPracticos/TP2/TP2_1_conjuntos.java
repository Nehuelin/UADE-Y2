package actividades.trabajosPracticos.TP2;
import estaticas.conjuntos.ConjuntoA;
import tdas.ConjuntoTDA;

public class TP2_1_conjuntos {
/*6) Escribir los métodos externos al TDA que implementan las operaciones intersección, unión y
diferencia */
    public static ConjuntoTDA intersección(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
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

    public static ConjuntoTDA union(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
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

    public static ConjuntoTDA diferencia(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
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

    public static void main(String[] args) {
        ConjuntoTDA conj1 = new ConjuntoA();
        ConjuntoTDA conj2 = new ConjuntoA();
        conj1.inicializarConjunto();
        conj2.inicializarConjunto();
        conj1.agregar(1);
        conj1.agregar(2);
        conj1.agregar(3);
        conj1.agregar(4);
        conj1.agregar(5);

        conj2.agregar(1);
        conj2.agregar(6);
        conj2.agregar(3);
        conj2.agregar(9);
        conj2.agregar(5);

        System.out.print("CONJUNTO 1: "); 
        conj1.imprimirConjunto();
        System.out.print("CONJUNTO 2: "); 
        conj2.imprimirConjunto();

        ConjuntoTDA conjInterseccion = new ConjuntoA();
        conjInterseccion = intersección(conj1, conj2);
        System.out.print("INTERSECCION: "); 
        conjInterseccion.imprimirConjunto();

        conj1.agregar(1);
        conj1.agregar(2);
        conj1.agregar(3);
        conj1.agregar(4);
        conj1.agregar(5);

        conj2.agregar(1);
        conj2.agregar(6);
        conj2.agregar(3);
        conj2.agregar(9);
        conj2.agregar(5);

        ConjuntoTDA conjUnion = new ConjuntoA();
        conjUnion = union(conj1, conj2);
        System.out.print("UNION: "); 
        conjUnion.imprimirConjunto();
        
        conj1.agregar(1);
        conj1.agregar(2);
        conj1.agregar(3);
        conj1.agregar(4);
        conj1.agregar(5);

        conj2.agregar(1);
        conj2.agregar(6);
        conj2.agregar(3);
        conj2.agregar(9);
        conj2.agregar(5);

        ConjuntoTDA conjDiferencia = new ConjuntoA();
        conjDiferencia = diferencia(conj1, conj2);
        System.out.print("DIFERENCIA: "); 
        conjDiferencia.imprimirConjunto();
    }
}
