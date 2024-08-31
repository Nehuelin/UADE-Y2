package dinamicas.listas;

public class EjemploRecorrido {
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

        recorrerLista(n1, 5);
    }

    public static void recorrerLista(Nodo origen, int numero) {
        Nodo aux = new Nodo();
        aux = origen;
        int i = 1;
        while (aux.sig != null && aux.info != numero){
            aux = aux.sig;
            i++;
        }
        System.out.println("Numero "+numero+" encontrado en el nodo "+i);
    }
}
