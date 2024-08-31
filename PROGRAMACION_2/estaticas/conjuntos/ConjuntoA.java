package estaticas.conjuntos;
import tdas.ConjuntoTDA;
 
public class ConjuntoA implements ConjuntoTDA{
    private int[] a;
    private int cant;

    public void inicializarConjunto(){
        a = new int[100];
        cant = 0;
    }

    public void agregar(int x){
        if (!this.pertenece(x)) {
            a[cant] = x;
            cant++;
        }
    }

    public boolean conjuntoVacio(){
        return(cant == 0);
    }

    public int elegir(){
        return a[cant - 1];
    }

    public boolean pertenece(int x){
        int  i = 0;
        while(i < cant && a[i] != x){
            i++;
        }
        return(i < cant);
    }

    public void sacar(int x){
        int i = 0;
        while(i < cant && a[i] != x){
            i++;
        }
        if (i < cant) {
            a[i] = a[cant - 1];
            cant--;
        } 
    }

    public void imprimirConjunto(){
        ConjuntoTDA conjAux = new ConjuntoA();
        conjAux.inicializarConjunto();
        System.out.print("[");
        while(!this.conjuntoVacio()){
            int elemento = this.elegir();
            conjAux.agregar(elemento);
            this.sacar(elemento);
            if(!this.conjuntoVacio()){
                System.out.print(elemento+", ");
            }else{
                System.out.print(elemento);
            }
        }
        System.out.print("]\n");
        while(!conjAux.conjuntoVacio()){
            int elemento = conjAux.elegir();
            this.agregar(elemento);
            conjAux.sacar(elemento);
        }
    }
}
