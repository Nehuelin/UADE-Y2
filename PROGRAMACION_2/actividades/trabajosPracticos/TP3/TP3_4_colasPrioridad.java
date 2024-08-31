package actividades.trabajosPracticos.TP3;

import tdas.*;
import estaticas.diccionariosMultiples.DiccionarioMultipleA;
import estaticas.colasPrioridad.ColaPrioridadAO;
import java.util.Random;

/*a) Escribir un método externo que permita generar un Diccionario Múltiple que
permita, para cada valor presente en la ColaPrioridad C recuperar todas las
prioridades que tiene asociadas en C */
public class TP3_4_colasPrioridad {
    public static DiccionarioMultipleTDA generarDiccionario(ColaPrioridadTDA C){
        DiccionarioMultipleTDA dm = new DiccionarioMultipleA();
        dm.inicializarDiccionario();
        ColaPrioridadTDA CAux = new ColaPrioridadAO();
        CAux.inicializarCola();
        while(!C.colaVacia()){
            CAux.acolarPrioridad(C.primero(), C.prioridad());
            dm.agregar(C.primero(), C.prioridad());
            C.desacolar();
        }
        while(!CAux.colaVacia()){
            C.acolarPrioridad(CAux.primero(), CAux.prioridad());
            CAux.desacolar();
        }
        return dm;
    }

    public static void main(String[] args) {
        Random random = new Random();

        ColaPrioridadTDA cola = new ColaPrioridadAO();
        cola.inicializarCola();

        for(int i = 0; i < random.nextInt(30) ; i++){
            cola.acolarPrioridad(random.nextInt(30), random.nextInt(10));
        }

        System.out.print("COLA PRIORIDAD: ");
        cola.imprimirCola();

        DiccionarioMultipleTDA diccionario = generarDiccionario(cola);

        ColaPrioridadTDA CAux = new ColaPrioridadAO();
        CAux.inicializarCola();

        System.out.println("DICCIONARIO: ");

        System.out.println("{");
        while(!cola.colaVacia()){
            ConjuntoTDA valores = diccionario.recuperar(cola.primero());
            System.out.print("    "+cola.primero()+" : ");
            valores.imprimirConjunto();
            CAux.acolarPrioridad(cola.primero(), cola.prioridad());
            cola.desacolar();
        }
        System.out.println("}");
        while(!CAux.colaVacia()){
            cola.acolarPrioridad(CAux.primero(), CAux.prioridad());
            CAux.desacolar();
        }
    }
}
