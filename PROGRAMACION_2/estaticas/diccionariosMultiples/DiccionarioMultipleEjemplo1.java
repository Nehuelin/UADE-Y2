package estaticas.diccionariosMultiples;

import tdas.DiccionarioMultipleTDA;
import tdas.DiccionarioSimpleTDA;
import tdas.ConjuntoTDA;
import estaticas.conjuntos.ConjuntoA;

public class DiccionarioMultipleEjemplo1 {
    public void pasaje(DiccionarioSimpleTDA dicSim, DiccionarioMultipleTDA dicMul){
        ConjuntoTDA claves = new ConjuntoA();
        claves = dicSim.claves();
        while (!claves.conjuntoVacio()){
            int clave = claves.elegir();
            int valor = dicSim.recuperar(clave);
            dicMul.agregar(clave, valor);
            claves.sacar(clave);
        }
    }
}
