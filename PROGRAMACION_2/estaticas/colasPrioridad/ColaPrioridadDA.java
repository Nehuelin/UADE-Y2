package estaticas.colasPrioridad;
import tdas.ColaPrioridadTDA;
 
public class ColaPrioridadDA implements ColaPrioridadTDA {
    int[] elementos; // valores de la cola
    int[] prioridades; // prioridades de la cola
    int indice; // cantidad de elementos

    public void inicializarCola(){
        elementos = new int[100];
        prioridades = new int[100];
        indice = 0;
    }

    public void acolarPrioridad(int x, int prioridad){
        int j = indice;
        while(j > 0 && prioridades[j - 1] > prioridad){
            elementos[j] = elementos[j - 1]; // desplazamiento paralelo
            prioridades[j] = prioridades[j - 1]; // desplazamiento paralelo
            j--;
        }
        elementos[j] = x;
        prioridades[j] = prioridad;
        indice++;
    }

    public void desacolar(){
        indice--;
    }

    public boolean colaVacia(){
        return (indice == 0);
    }

    public int primero(){
        return elementos[indice - 1];
    }

    public int prioridad(){
        return prioridades[indice - 1];
    }

    public void imprimirCola(){
        ColaPrioridadTDA cAux = new ColaPrioridadDA();
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
