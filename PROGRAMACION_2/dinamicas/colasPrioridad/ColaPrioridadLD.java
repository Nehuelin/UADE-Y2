package dinamicas.colasPrioridad;
import tdas.ColaPrioridadTDA;

public class ColaPrioridadLD implements ColaPrioridadTDA{
    class NodoPrioridad{
        int info;
        int prioridad;
        NodoPrioridad sig;
    }

    NodoPrioridad primero;

    public void inicializarCola(){
        primero = null;
    }

    public void acolarPrioridad(int x, int prioridad){
        NodoPrioridad nuevo = new NodoPrioridad();
        nuevo.info = x;
        nuevo.prioridad = prioridad;
        if (primero == null || primero.prioridad < prioridad){
            nuevo.sig = primero;
            primero = nuevo;
        } else {
            NodoPrioridad aux = primero;
            while (aux.sig != null && aux.sig.prioridad > prioridad){
                aux = aux.sig;
            }
            nuevo.sig = aux.sig;
            aux.sig = nuevo;
        }
    }

    public void desacolar() {
        primero = primero.sig;
    }

    public boolean colaVacia() {
        return (primero == null);
    }

    public int primero(){
        return primero.info;
    }

    public int prioridad(){
        return primero.prioridad;
    }

    public void imprimirCola(){
        ColaPrioridadTDA cAux = new ColaPrioridadLD();
        cAux.inicializarCola();

        System.out.print("[");
        while(!this.colaVacia()){
            int elemento = this.primero();
            int prioridad = this.prioridad();
            this.desacolar();
            if(!this.colaVacia()){
                System.out.print(elemento+" (P: "+prioridad+")"+", ");
            }else{
                System.out.print(elemento+" (P: "+prioridad+")");
            }
            cAux.acolarPrioridad(elemento, prioridad);
        }
        System.out.print("]\n");

        while(!cAux.colaVacia()){
            this.acolarPrioridad(cAux.primero(), cAux.prioridad());
            cAux.desacolar();
        }
    }
}

