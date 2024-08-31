package dinamicas.colasPrioridad;
import tdas.ColaPrioridadTDA;
import tdas.ColaTDA;

// Pasar los valores de una cola con PRIORIDAD a una cola de VALORES, y el numero de prioridad a una cola de PRIORIDADES 
public class ColaPrioridadEjemplo1 {
    public static void pasarElementos(ColaPrioridadTDA origen, ColaTDA valores, ColaTDA prioridades){
        while (origen.colaVacia() != true){
            valores.acolar(origen.primero());
            prioridades.acolar(origen.prioridad());
            origen.desacolar();
        }
    }
}
