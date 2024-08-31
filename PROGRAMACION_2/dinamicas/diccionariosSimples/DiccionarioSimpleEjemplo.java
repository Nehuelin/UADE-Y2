package dinamicas.diccionariosSimples;
import tdas.DiccionarioSimpleTDA;
import tdas.PilaTDA;
import tdas.ConjuntoTDA;

// pasar todos los valores de un diccionario simple DIC a una pila valores
public class DiccionarioSimpleEjemplo {
    public static void pasaje(DiccionarioSimpleTDA dic, PilaTDA valores){
        ConjuntoTDA claves;
        claves = dic.claves();
        while (!claves.conjuntoVacio()){
            int x = claves.elegir();
            valores.apilar(dic.recuperar(x));
            claves.sacar(x);
        }
    }
}
