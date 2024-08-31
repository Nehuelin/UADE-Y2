package actividades.trabajosPracticos.TP1;
import estaticas.colasPrioridad.ColaPrioridadAO;
import tdas.ColaPrioridadTDA;

/*6) A partir del TDA Cola con prioridades definido, escribir un método que permita
a) Combinar dos colas con prioridades CP1 y CP2, generando una nueva
cola con prioridades. Considerar que a igual prioridad, los elementos de la CP1
son más prioritarios que los de la CP2.
b) Determinar si dos Colas con prioridad son idénticas */
public class TP1_3_colasPrioridad {
    public static ColaPrioridadTDA combinarColasPrioridad(ColaPrioridadTDA colaPA, ColaPrioridadTDA colaPB){
        ColaPrioridadTDA nuevaColaP = new ColaPrioridadAO();
        nuevaColaP.inicializarCola();
        while(!colaPA.colaVacia()){
            nuevaColaP.acolarPrioridad(colaPA.primero(), colaPA.prioridad());
            colaPA.desacolar();
        }
        while(!colaPB.colaVacia()){
            nuevaColaP.acolarPrioridad(colaPB.primero(), colaPB.prioridad());
            colaPB.desacolar();
        }
        return nuevaColaP;
    }

    public static boolean sonIdenticas(ColaPrioridadTDA colaPA, ColaPrioridadTDA colaPB){
        ColaPrioridadTDA colaPAux1 = new ColaPrioridadAO();
        ColaPrioridadTDA colaPAux2 = new ColaPrioridadAO();
        colaPAux1.inicializarCola();
        colaPAux2.inicializarCola();
        boolean iguales = true;
        while(!colaPA.colaVacia() && iguales == true){
            if(colaPA.primero() == colaPB.primero() && colaPA.prioridad() == colaPB.prioridad()){
                colaPAux1.acolarPrioridad(colaPA.primero(), colaPA.prioridad());
                colaPA.desacolar();
                colaPAux2.acolarPrioridad(colaPB.primero(), colaPB.prioridad());
                colaPB.desacolar();
            } else 
                iguales = false;
        }
        while(!colaPAux1.colaVacia()){
            colaPA.acolarPrioridad(colaPAux1.primero(), colaPAux1.prioridad());
            colaPAux1.desacolar();
        }
        while(!colaPAux2.colaVacia()){
            colaPB.acolarPrioridad(colaPAux2.primero(), colaPAux2.prioridad());
            colaPAux2.desacolar();
        }

        return iguales;
    } 

    public static void main(String[] args) {
        ColaPrioridadTDA CP1 = new ColaPrioridadAO();
        ColaPrioridadTDA CP2 = new ColaPrioridadAO();
        CP1.inicializarCola();
        CP2.inicializarCola();

        CP1.acolarPrioridad(1, 1);
        CP1.acolarPrioridad(2, 2);
        CP1.acolarPrioridad(3, 3);
        CP1.acolarPrioridad(4, 4);
        CP1.acolarPrioridad(5, 5);
        CP1.acolarPrioridad(6, 6);

        CP2.acolarPrioridad(7, 1);
        CP2.acolarPrioridad(8, 2);
        CP2.acolarPrioridad(9, 3);
        CP2.acolarPrioridad(10, 4);
        CP2.acolarPrioridad(11, 5);
        CP2.acolarPrioridad(12, 6);

        ColaPrioridadTDA CP3 = new ColaPrioridadAO();
        CP3.inicializarCola();
        CP3 = combinarColasPrioridad(CP1, CP2); // A)

        System.out.println();

        CP1.acolarPrioridad(1, 1);
        CP1.acolarPrioridad(2, 2);
        CP1.acolarPrioridad(3, 3);
        CP1.acolarPrioridad(4, 4);
        CP1.acolarPrioridad(5, 5);
        CP1.acolarPrioridad(6, 6);

        CP2.acolarPrioridad(1, 1);
        CP2.acolarPrioridad(2, 2);
        CP2.acolarPrioridad(3, 3);
        CP2.acolarPrioridad(4, 4);
        CP2.acolarPrioridad(5, 5);
        CP2.acolarPrioridad(6, 6);

        boolean son_identicas = sonIdenticas(CP1, CP2); // B)

        if (son_identicas)
            System.out.println("LAS COLAS SON IDENTICAS");
        else
            System.out.println("LAS COLAS NO SON IDENTICAS");
    }
}
