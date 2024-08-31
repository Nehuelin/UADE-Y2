package dinamicas.listas;

public class EjemploEliminacion {
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

        System.out.println();

        eliminar(n1, 12);
        mostrarLista1(n1);
    }

    public static Nodo eliminar(Nodo u, int numero){
        if (u != null){
            if(u.info == numero){
                u = u.sig;
            } else {
                Nodo aux = new Nodo();
                aux = u;
                while(aux.sig != null && aux.sig.info != numero){
                    aux = aux.sig;
                }   
                if (aux.sig != null){
                    aux.sig = aux.sig.sig;
                }
            }
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
