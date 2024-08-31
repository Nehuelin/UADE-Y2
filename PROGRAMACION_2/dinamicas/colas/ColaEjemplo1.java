package dinamicas.colas;
import tdas.ColaTDA;

public class ColaEjemplo1 {
    public void pasarElementos(ColaTDA origen, ColaTDA destino){
        destino.acolar(origen.primero());
        origen.desacolar();
    }
}
