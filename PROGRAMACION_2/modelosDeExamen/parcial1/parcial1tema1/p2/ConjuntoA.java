package modelosDeExamen.parcial1.parcial1tema1.p2;
 
public class ConjuntoA implements ConjuntoModTDA{
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

    public boolean todosPertenecen(ConjuntoModTDA x) {
        ConjuntoModTDA aux = new ConjuntoA();
        boolean incluidos = true;
        
        while(!x.conjuntoVacio() && incluidos){
            int valor = x.elegir();
            if(this.pertenece(valor)){
                aux.agregar(valor);
                x.sacar(valor);
            } else {
                incluidos = false;
                break;
            }
        }

        while(!aux.conjuntoVacio()){
            int elemento = aux.elegir(); 
            x.agregar(elemento);
            aux.sacar(elemento);
        }

        return (incluidos);
    }

    public void sacarTodos(ConjuntoModTDA x) {
        ConjuntoModTDA aux = new ConjuntoA();
        aux.inicializarConjunto();
    
        while (!x.conjuntoVacio() && !this.conjuntoVacio()) {
            int valor = x.elegir();
            this.sacar(valor);
            x.sacar(valor);
            aux.agregar(valor);  
        }

        while (!aux.conjuntoVacio()) {
            int valor = aux.elegir();
            x.agregar(valor);
            aux.sacar(valor);
        }
    }
}
