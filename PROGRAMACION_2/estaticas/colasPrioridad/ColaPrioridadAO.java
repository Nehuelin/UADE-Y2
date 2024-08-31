package estaticas.colasPrioridad;
import tdas.ColaPrioridadTDA;
 
public class ColaPrioridadAO implements ColaPrioridadTDA {
    Elemento[] elementos;
    int indice;
    
    public void inicializarCola(){
        elementos = new Elemento[100];
        indice = 0;
    }
    
    public void acolarPrioridad(int x, int prioridad){
        int j = indice;
        while(j > 0 && elementos[j - 1].prioridad > prioridad){
            elementos[j] = elementos[j - 1];
            j--;
        }
        elementos[j] = new Elemento();
        elementos[j].valor = x;
        elementos[j].prioridad = prioridad;
        indice++;
    }

    public void desacolar(){
        indice--;
    }

    public boolean colaVacia(){
        return(indice == 0);
    }

    public int primero(){
        return elementos[indice - 1].valor;
    }

    public int prioridad(){
        return elementos[indice - 1].prioridad;
    }

    public void imprimirCola(){
        ColaPrioridadTDA cAux = new ColaPrioridadAO();
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
