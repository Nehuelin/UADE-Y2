package estaticas.colas;
import tdas.ColaTDA;
 
public class ColaPU implements ColaTDA {
    int[] arr;
    int inx;

    public void inicializarCola(){
        arr = new int[100];
        inx = 0;
    }

    public void acolar(int x){
        for (int i = inx - 1; i >= 0; i--){
            arr[i + 1] = arr[i];
        }
        arr[0] = x;
        inx++;
    }

    public void desacolar(){
        inx--;
    }

    public boolean colaVacia(){
        return (inx == 0);
    }

    public int primero(){
        return arr[inx - 1];
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
