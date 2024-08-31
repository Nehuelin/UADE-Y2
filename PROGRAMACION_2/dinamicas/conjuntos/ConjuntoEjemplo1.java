package dinamicas.conjuntos;
import tdas.ConjuntoTDA;

public class ConjuntoEjemplo1 {
    public static boolean incluye(ConjuntoTDA conj1, ConjuntoTDA conj2){
        boolean incluye = true;
        while (!conj2.conjuntoVacio() && incluye){
            int x = conj2.elegir();
            if (!conj1.pertenece(x)){
                incluye = false;
            } else {
                conj2.sacar(x);
            }
        }
        return incluye;
    }
} 