package modelosDeExamen.parcial1.parcial1tema1.p2;


public class ConjuntoLD implements ConjuntoModTDA {
    private class Nodo {
        int info;
        Nodo sig;
    }

    private Nodo c;

    public void inicializarConjunto(){
        c = null;
    }

    public int elegir(){
        return c.info;
    }

    public void sacar(int x){
        if (c != null){
            if (c.info == x){ // Es el primero
                c = c.sig;
            } else { // buscamos otro
                Nodo aux = c;   
                while (aux.sig != null && aux.sig.info != x){ 
                    aux = aux.sig;
                }
                if (aux.sig != null) {
                    aux.sig = aux.sig.sig;
                }
            }
        }
    }

    public void agregar(int x) {
        if (!this.pertenece(x)) { // Se verifica pertenencia
            Nodo nuevo = new Nodo(); // Creamos nodo que se agregara
            nuevo.info = x; 
            nuevo.sig = c;
            c = nuevo;
        }
    }

    public boolean pertenece(int x) {
        Nodo aux = c;
        while (aux != null && aux.info != x) {
            aux = aux.sig;
        }
        return (aux != null);
    }

    public boolean conjuntoVacio(){
        return (c == null);
    }

    public boolean todosPertenecen(ConjuntoModTDA x) {
        ConjuntoModTDA conjCopia = new ConjuntoLD();
        boolean incluidos = true;

        while(!x.conjuntoVacio() && incluidos){
            int valor = x.elegir();
            if(this.pertenece(valor)){
                conjCopia.agregar(valor);
                x.sacar(valor);
            } else {
                incluidos = false;
                break;
            }
        }

        while(!conjCopia.conjuntoVacio()){
            int elemento = conjCopia.elegir(); 
            x.agregar(elemento);
            conjCopia.sacar(elemento);
        }

        return (incluidos);
    }

    public void sacarTodos(ConjuntoModTDA x) {
        ConjuntoModTDA aux = new ConjuntoLD();
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
