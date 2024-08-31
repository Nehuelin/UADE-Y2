package modelosDeExamen.parcial1.parcial1tema1.p2;

public class Main {

    public static void main(String[] args) {
        ConjuntoModTDA conjunto1 = new ConjuntoLD();
        ConjuntoModTDA conjunto2 = new ConjuntoLD();

        conjunto1.inicializarConjunto();
        conjunto2.inicializarConjunto();

        conjunto1.agregar(1);
        conjunto1.agregar(2);
        conjunto1.agregar(3);
        conjunto1.agregar(4);
        conjunto1.agregar(5);
        conjunto1.agregar(6);

        conjunto2.agregar(4);
        conjunto2.agregar(5);
        conjunto2.agregar(2);

        if(conjunto1.todosPertenecen(conjunto2)){
            System.out.println("ALELUYA");
        }

        conjunto1.sacarTodos(conjunto2);

        System.err.println();
    }
}
