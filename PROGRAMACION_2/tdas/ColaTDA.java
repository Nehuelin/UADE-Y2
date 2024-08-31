package tdas;

public interface ColaTDA {
    void inicializarCola();
    void acolar(int x);
    void desacolar();
    boolean colaVacia();
    int primero();
    void imprimirCola();
}
