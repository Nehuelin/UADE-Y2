package modelosDeExamen.parcial1.parcial1tema1.p1;

public class ListaDoblementeEnlazada {
            
    public static void main(String[] args) {
        NodoListaDE n1 = new NodoListaDE();
        NodoListaDE n2 = new NodoListaDE();
        NodoListaDE n3 = new NodoListaDE();
        NodoListaDE n4 = new NodoListaDE();

        n1.valor = 1;
        n2.valor = 2;
        n3.valor = 3;
        n4.valor = 4;

        n1.sig = n2;
        n2.sig = n3;
        n3.sig = n4;
        n4.sig = null;

        n1.prev = null;
        n2.prev = n1;
        n3.prev = n2;
        n4.prev = n3;

        NodoListaDE n0 = new NodoListaDE(); 
        n0 = Agregar(n1, n4, 0);
        Eliminar(n0, n4, 2);

        System.out.println();
    }
    
    public static NodoListaDE Agregar(NodoListaDE cabeza, NodoListaDE cola, int num){    
        NodoListaDE nuevo = new NodoListaDE();
        nuevo.valor = num;
        nuevo.sig = cabeza;
        cabeza.prev = nuevo;
        return nuevo;
    }

    public static void Eliminar(NodoListaDE cabeza, NodoListaDE cola, int num){
        NodoListaDE aux = new NodoListaDE();
        aux = cabeza;
        while (aux != null){
            if (aux.valor == num){ // Si coincide el numero y... 
                if(aux.prev == null){ // Si es cabeza...
                    aux.sig = null; // La conexion de aux se anula
                    aux.sig.prev = null; // Y la conexion de retorno del siguiente de aux se anula 
                    break;
                }else if(aux.sig == null){ // Si es cola...
                        aux.sig.prev = null; // La conexion del previo de aux se anula 
                        aux.prev = null; // Y la conexion de retorno de aux se anula
                        break;
                } else { // No es ninguno de los extremos...
                    aux.prev.sig = aux.sig; // Conectamos el previo de aux con el siguiente de aux
                    aux.sig.prev = aux.prev; // Conectamos el retorno del siguiente de aux con el previo de aux
                    break;
                }    
            } else { // Si no se encuentra el valor, se sigue con el siguiente
                aux = aux.sig;
            }            
        }
        aux.sig = null; // No se si es necesario pero ya fue xd
        aux.prev = null;
    }
}
