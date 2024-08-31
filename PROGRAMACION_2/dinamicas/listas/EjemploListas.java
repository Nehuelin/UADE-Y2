package dinamicas.listas;

public class EjemploListas {
    public static void main(String[] args) {
        Nodo n1 = new Nodo();
        Nodo n2 = new Nodo();
        Nodo n3 = new Nodo();
        Nodo n4 = new Nodo();
        
        n1.info = 1; 
        n2.info = 3; 
        n3.info = 5; 
        n4.info = 7; 

        n1.sig = n2;
        n2.sig = n3;
        n3.sig = n4;
        n4.sig = null; // El ultimo convenientemente tiene que tener NULL
    }
}
