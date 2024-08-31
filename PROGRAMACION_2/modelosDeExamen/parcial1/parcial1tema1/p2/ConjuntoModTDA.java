package modelosDeExamen.parcial1.parcial1tema1.p2;

public interface ConjuntoModTDA {
    void inicializarConjunto();
    void agregar(int x);
    int elegir();
    boolean conjuntoVacio();
    void sacar(int x);
    boolean pertenece(int x);
    boolean todosPertenecen(ConjuntoModTDA x);
    void sacarTodos(ConjuntoModTDA x);
}