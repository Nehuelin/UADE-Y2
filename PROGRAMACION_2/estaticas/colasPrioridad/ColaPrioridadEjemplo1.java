package estaticas.colasPrioridad;
import estaticas.colas.*;
import tdas.ColaPrioridadTDA;
import tdas.ColaTDA;
 
public class ColaPrioridadEjemplo1 {
    public static void pasaje(ColaPrioridadTDA origen, ColaTDA valores, ColaTDA prioridades){
        while(!origen.colaVacia()){
            valores.acolar(origen.primero());
            prioridades.acolar(origen.prioridad());
            origen.desacolar();
        }
    }

    public static void imprimirCola(ColaTDA cola) {
        ColaTDA copia = new ColaPI();
        copia.inicializarCola();

        while (!cola.colaVacia()) {
            int valor = cola.primero();
            System.out.print(valor + " ");
            copia.acolar(valor);
            cola.desacolar();
        }

        System.out.println();

        // Restaurar la cola original
        while (!copia.colaVacia()) {
            int valor = copia.primero();
            cola.acolar(valor);
            copia.desacolar();
        }
    }

    public static void main(String[] args) {
        ColaPrioridadTDA origen = new ColaPrioridadDA();
        ColaTDA valores = new ColaPI();
        ColaTDA prioridades = new ColaPI();
        origen.inicializarCola();
        origen.acolarPrioridad(1, 6);
        origen.acolarPrioridad(6, 2);
        origen.acolarPrioridad(54, 9);
        origen.acolarPrioridad(7, 4);
        valores.inicializarCola();
        prioridades.inicializarCola();
        pasaje(origen, valores, prioridades);

        System.out.println("Contenido de la cola valores:");
        imprimirCola(valores);
        System.out.println("Contenido de la cola prioridades:");
        imprimirCola(prioridades);
    }
}
