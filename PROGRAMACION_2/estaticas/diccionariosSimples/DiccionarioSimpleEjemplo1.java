package estaticas.diccionariosSimples;

import tdas.DiccionarioSimpleTDA;
import tdas.ConjuntoTDA;
import tdas.PilaTDA;
import estaticas.pilas.PilaTF;

public class DiccionarioSimpleEjemplo1 {
    
    public static void pasaje(DiccionarioSimpleTDA dic, PilaTDA valores){
        ConjuntoTDA claves;
        claves = dic.claves();
        while(!claves.conjuntoVacio()){
            int x = claves.elegir();
            valores.apilar(dic.recuperar(x));
            claves.sacar(x);
        }
    }

    public static void main(String[] args) {
        DiccionarioSimpleTDA d = new DiccionarioSimpleA();
        d.inicializarDiccionario();
        d.agregar(1, 100);
        d.agregar(2, 200);
        d.agregar(4, 400);
        PilaTDA valores = new PilaTF();
        valores.inicializarPila();
        pasaje(d, valores);
    }
}
