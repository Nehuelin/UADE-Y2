package estaticas.pilas;
import estaticas.colas.ColaPI;
import tdas.ColaTDA;
import tdas.PilaTDA;

public class PilaTF implements PilaTDA{
    int[] arr;
    int inx;

    public void inicializarPila(){
        arr = new int[100];
        inx = 0;
    }

    public void apilar(int x){
        arr[inx] = x;
        inx++;
    }

    public void desapilar(){
        inx--;
    }

    public boolean pilaVacia(){
        return (inx == 0);
    }

    public int tope(){
        return (arr[inx - 1]);
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
