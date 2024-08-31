package dinamicas.diccionariosMultiples;

import tdas.DiccionarioSimpleTDA;
import tdas.DiccionarioMultipleTDA;
import tdas.ConjuntoTDA;

public class DiccionarioMultipleEjemplo1 {
    public void pasaje(DiccionarioSimpleTDA dicSim, DiccionarioMultipleTDA dicMul){
        ConjuntoTDA claves;
        claves = dicSim.claves();
        while (!claves.conjuntoVacio()){
            int clave = claves.elegir();
            int valor = dicSim.recuperar(clave);
            dicMul.agregar(clave, valor);
            claves.sacar(clave);
        }
    }
}
