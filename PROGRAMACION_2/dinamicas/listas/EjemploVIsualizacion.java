package dinamicas.listas;

public class EjemploVIsualizacion {
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
        n4.sig = null; 

        mostrarLista1(n1);
        System.out.println();
        mostrarLista2(n1);
    }

    // ESTRATEGIA 1
    public static void mostrarLista1(Nodo u) { 
        Nodo aux = new Nodo(); // Nodo Auxiliar
        aux = u;
        System.out.print("["); 
        while(aux != null){ // Mientras no se llegue al final...
            System.out.print(aux.info);
            aux = aux.sig; // Imprimo el numero y avanzo al siguiente nodo
            if (aux != null){ // Si no se llega al final, se agrega una coma
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }
 
    // ESTRATEGIA 2 (RECURSIVIDAD)
    public static void mostrarLista2(Nodo u) { 
        System.out.print("["); 
        if (u != null){ // Si no se llega al final...
            System.out.print(u.info+"] --> " ); // Se imprime la info
            mostrarLista2(u.sig); // Y se invoca la funcion con el nodo que le sigue
        } else {
            System.out.print("]"); // Hasta que llega el ultimo nodo
        }
    }
}
