package estaticas.colas;
import tdas.ColaTDA;
 
public class ColaPU2 implements ColaTDA{
    int[] arr;

    public void inicializarCola(){
        arr = new int[100];
        arr[0] = 0;
    }

    public void acolar(int x){
        for (int i = arr[0]; i > 0; i--){
            arr[i + 1] = arr[i];
        }
        arr[1] = x;
        arr[0]++;
    }

    public void desacolar(){
        arr[0]--;
    }

    public boolean colaVacia(){
        return (arr[0] == 0);
    }

    public int primero(){
        return arr[arr[0]];
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
