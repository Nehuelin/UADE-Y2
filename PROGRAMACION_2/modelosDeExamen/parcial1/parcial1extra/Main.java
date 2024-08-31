package modelosDeExamen.parcial1.parcial1extra;

public class Main {
    public static void main(String[] args) {
        ListaCircularTDA lista1 = new ListaCircularLD();
    
        lista1.InicializarLista();
        lista1.Agregar(1);
        lista1.Agregar(2);
        lista1.Agregar(3);
        lista1.Agregar(4);
        lista1.Agregar(5);
        
        if (lista1.ListaVacia()){
            System.out.println("LISTA VACIA");
        } else {
            if (lista1.Existe(1)){
                System.out.println("EXISTE");
            } else {
                System.out.println("NO EXISTE");
            }

            if (lista1.Existe(5)){
                System.out.println("EXISTE");
            } else {
                System.out.println("NO EXISTE");
            }

            lista1.Eliminar(3);

            lista1.Eliminar(5);

            String lista = lista1.MostrarLista();
            System.out.println(lista);
        }
    }
}
