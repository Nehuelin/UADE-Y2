package estaticas.colas;
import tdas.ColaTDA;
 
public class ColaPI implements ColaTDA {
    int[] arr;
    int inx;
    
    public void inicializarCola(){
        arr = new int[100];
        inx = 0;
    }

    public void acolar(int x){
        arr[inx] = x;
        inx++;
    }

    public void desacolar(){
        for(int i = 0; i < inx - 1; i++){
            arr[i] = arr[i + 1];
        }
        inx--;
    }

    public boolean colaVacia(){
        return (inx == 0);
    }

    public int primero(){
        return arr[0];
    }

    public void imprimirCola(){
        ColaTDA cAux = new ColaPI();
        cAux.inicializarCola();

        System.out.print("[");
        while(!this.colaVacia()){
            int elemento = this.primero();
            this.desacolar();
            if(!this.colaVacia()){
                System.out.print(elemento+", ");
            }else{
                System.out.print(elemento);
            }
            cAux.acolar(elemento);
        }
        System.out.print("]\n");

        while(!cAux.colaVacia()){
            this.acolar(cAux.primero());
            cAux.desacolar();
        }
    }
}
