package actividades.trabajosPracticos.TP3;

import tdas.*;
import estaticas.diccionariosSimples.DiccionarioSimpleA;
import estaticas.conjuntos.ConjuntoA;
import estaticas.diccionariosMultiples.DiccionarioMultipleA;

/*Dado un Diccionario Simple D, que representa el concepto clásico de diccionario: la
clave representa una palabra y el valor su significado. Generar un Diccionario Múltiple DS
que a partir de un significado s, vincule todas las palabras que tienen dicho significado, es
decir que son sinónimos. Cada clave s será un significado y los valores asociados
(sinónimos) aquellas claves de D que tenían asociado el valor s


NOTA A MI MISMO: Lo voy a hacer con numeros en vez de palabras (no tengo ganas de crear un nuevo TDA desde cero xd)
 
Diccionario Simple --> numero : valor
Diccionario Multiple --> valor : todos los numeros con ese valor
*/

public class TP3_5_2_diccionariosSimples {
    public static DiccionarioMultipleTDA generarDiccionario(DiccionarioSimpleTDA D){
        DiccionarioMultipleTDA DS = new DiccionarioMultipleA();
        DS.inicializarDiccionario();

        ConjuntoTDA claves = D.claves();
        ConjuntoTDA valores = new ConjuntoA();
        valores.inicializarConjunto();

        while(!claves.conjuntoVacio()){
            int clave = claves.elegir();
            valores.agregar(D.recuperar(clave));
            claves.sacar(clave); 
        }

        while(!valores.conjuntoVacio()){
            claves = D.claves();
            int valor  = valores.elegir();
            while(!claves.conjuntoVacio()){
                int clave = claves.elegir();
                if(valor == D.recuperar(clave)){
                    DS.agregar(valor, clave);
                }
                claves.sacar(clave);
            }
            valores.sacar(valor);
        }

        return DS;
    } 

    public static void main(String[] args) {
        DiccionarioSimpleTDA diccionario = new DiccionarioSimpleA();
        diccionario.inicializarDiccionario();

        diccionario.agregar(1, 1);
        diccionario.agregar(2, 2);
        diccionario.agregar(3, 1);
        diccionario.agregar(4, 3);
        diccionario.agregar(5, 2);
        diccionario.agregar(6, 4);
        diccionario.agregar(7, 1);

        System.out.println("\nDICCIONARIO SIMPLE: ");
        diccionario.imprimirDiccionario();
        
        DiccionarioMultipleTDA diccionarioMultiple = generarDiccionario(diccionario);
        System.out.println("\nDICCIONARIO MULTIPLE: ");
        diccionarioMultiple.imprimirDiccionario();
    }
}
