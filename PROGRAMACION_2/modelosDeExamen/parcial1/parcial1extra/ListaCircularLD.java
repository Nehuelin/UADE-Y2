package modelosDeExamen.parcial1.parcial1extra;

public class ListaCircularLD implements ListaCircularTDA{

    private class Nodo{
        int info;
        Nodo sig;
    }

    private Nodo ultimo;

    public void InicializarLista() {
        ultimo = null;
    }


    public void Agregar(int x) {
        Nodo nuevo = new Nodo();
        nuevo.info = x;
        if (ultimo == null){
            nuevo.sig = nuevo;
        } else {
            nuevo.sig = ultimo.sig;
            ultimo.sig = nuevo;
        }
        ultimo = nuevo;
    }

  
    public void Eliminar(int x) { 
        Nodo aux = new Nodo();
        if(ultimo.sig == ultimo){
            if(ultimo.info == x){
                ultimo = null;
            } 
        }else {
            aux = ultimo.sig;
            while (aux.sig != ultimo && aux.sig.info != x){
                aux = aux.sig;
            }   
            if (aux.sig != ultimo){
                aux.sig = aux.sig.sig;
            } else {
                aux.sig = ultimo.sig;
                ultimo = aux;
            }
        }
    }

   
    public boolean ListaVacia() {
        return (ultimo == null);
    }

    
    public boolean Existe(int x) {
        boolean encontrado = false;
        if(ultimo.sig == ultimo){
            if(ultimo.info == x){
                encontrado = true;
            }
        } else {
            Nodo aux = new Nodo();
            aux = ultimo.sig;
            while(aux != ultimo){
                if(aux.info == x){
                    encontrado = true;
                    break;
                }
                aux = aux.sig;
            }
            if(!encontrado && ultimo.info == x){
                encontrado = true;
            }
        }
        return encontrado;
    }

    
    public String MostrarLista() {
        String lista = "";
        if (ultimo.sig == ultimo){
            lista = "["+ultimo.info+"]";
        } else {
            Nodo aux = new Nodo();
            aux = ultimo.sig;
            lista += "[";
            while(aux != ultimo){
                lista += aux.info+", ";
                aux = aux.sig;
            }
            lista += ultimo.info+"]";
        }
        return lista;
    }

}
