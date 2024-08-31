package dinamicas.listas;

public class EjemploInsercion {
    public static void main(String[] args) {
        Nodo n1 = new Nodo();
        Nodo n2 = new Nodo();
        Nodo n3 = new Nodo();
        Nodo n4 = new Nodo();
        Nodo n5 = new Nodo();
        Nodo n6 = new Nodo();
        
        n1.info = 1; 
        n2.info = 3; 
        n3.info = 5; 
        n4.info = 7; 
        n5.info = 9; 
        n6.info = 12; 

        n1.sig = n2;
        n2.sig = n3;
        n3.sig = n4;
        n4.sig = n5;  
        n5.sig = n6;  
        n6.sig = null;  

        mostrarLista1(n1);

        Nodo nuevoNodo1 = new Nodo(); 
        nuevoNodo1 = agregarInicio(n1, 0);       
        agregarFinal(nuevoNodo1, 15);   
        agregarOrdenado(nuevoNodo1, 6);    

        System.out.println();
        mostrarLista1(nuevoNodo1);
    }

    public static Nodo agregarInicio(Nodo u, int numero){
        Nodo nuevo = new Nodo();
        nuevo.info = numero;
        nuevo.sig = u;
        return nuevo;
    }

    public static Nodo agregarFinal(Nodo u, int numero){
        Nodo nuevo = new Nodo();
        nuevo.info = numero;
        nuevo.sig = null;
        if (u == null) {
           u = nuevo;
        } else {
            Nodo aux = new Nodo();
            aux = u;
            while (aux.sig != null) {
                aux = aux.sig;
            }
            aux.sig = nuevo;
        }
        return u;
    }

    public static Nodo agregarOrdenado(Nodo u, int numero){
        Nodo nuevo = new Nodo();
        nuevo.info = numero;
        nuevo.sig = null;
        if (u == null) {
           u = nuevo;
        } else if (u.info > numero) {
            nuevo.sig = u;
            u = nuevo;
        } else {
            Nodo aux = new Nodo();
            aux = u;
            while (aux != null && aux.sig.info < numero){
                aux = aux.sig;
            }
            nuevo.sig = aux.sig;
            aux.sig = nuevo;
        }
        return u;
    }

    public static void mostrarLista1(Nodo u) { 
        Nodo aux = new Nodo(); 
        aux = u;
        System.out.print("["); 
        while(aux != null){ 
            System.out.print(aux.info);
            aux = aux.sig; 
            if (aux != null){ 
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }
}
