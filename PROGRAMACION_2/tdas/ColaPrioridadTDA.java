package tdas;

public interface ColaPrioridadTDA {
    void inicializarCola();
    void acolarPrioridad(int x, int prioridad);
    void desacolar();
    boolean colaVacia();
    int primero();
    int prioridad();
    void imprimirCola();
}
