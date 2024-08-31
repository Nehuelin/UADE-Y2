package estaticas.pilas;
import estaticas.colas.ColaPI;
import tdas.ColaTDA;
import tdas.PilaTDA;

public class PilaTF2 implements PilaTDA{
    int[] arr;

    public void inicializarPila(){
        arr = new int[100];
        arr[0] = 0;
    }

    public void apilar(int x){
        arr[arr[0] + 1] = x;
        arr[0]++;
    }

    public void desapilar(){
        arr[0]--;
    }

    public boolean pilaVacia(){
        return(arr[0] == 0);
    }

    public int tope() {
        return arr[arr[0]];
    }

    public void imprimirPila(){
        ColaTDA cola = new ColaPI();
        cola.inicializarCola();

        System.out.print("[");
        while(!this.pilaVacia()){
            int elemento = this.tope();
            this.desapilar();
            if(!this.pilaVacia()){
                System.out.print(elemento+", ");
            }else{
                System.out.print(elemento);
            }
            cola.acolar(elemento);
        }
        System.out.print("]\n");

        while(!cola.colaVacia()){
            this.apilar(cola.primero());
            cola.desacolar();
        }
    }
}
