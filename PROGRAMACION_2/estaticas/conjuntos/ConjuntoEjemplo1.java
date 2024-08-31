package estaticas.conjuntos;
import tdas.ConjuntoTDA;
 
public class ConjuntoEjemplo1 {
    
    public static boolean incluye(ConjuntoTDA conj1, ConjuntoTDA conj2){
        boolean incluye = true;
        while(!conj2.conjuntoVacio() && incluye){
            int x = conj2.elegir();
            if (!conj1.pertenece(x)) {
                incluye = false;
            } else {
                conj2.sacar(x);
            }
        }
        return incluye;
    }

    public static void main(String[] args) {
        ConjuntoTDA conj1 = new ConjuntoA();
        conj1.inicializarConjunto();
        conj1.agregar(7); 
        conj1.agregar(5); 
        conj1.agregar(2);
        
        ConjuntoTDA conj2 = new ConjuntoA();
        conj2.inicializarConjunto();
        conj2.agregar(7);
        // conj2.agregar(0); // <-- Anular para que el resultado sea TRUE
        conj2.agregar(2);

        System.out.println(incluye(conj1, conj2));
    }
}
