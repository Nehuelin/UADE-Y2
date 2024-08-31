package estaticas.colas;
import tdas.ColaTDA;
 
// pasar todos los elemento de una cola origen a otra cola llamada destino
public class ColaEjemplo1 {
    public static void pasarCola(ColaTDA origen, ColaTDA destino){
        while (!origen.colaVacia()){
            destino.acolar(origen.primero());
            origen.desacolar();
        }
    }

    public static void main(String[] args) {
        ColaTDA origen = new ColaPU();
        ColaTDA destino = new ColaPU();
        origen.inicializarCola();
        origen.acolar(1);
        origen.acolar(2);
        origen.acolar(3);
        destino.inicializarCola();
        pasarCola(origen, destino);
    }
}
