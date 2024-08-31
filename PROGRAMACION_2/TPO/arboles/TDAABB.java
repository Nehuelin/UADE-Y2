package arboles;

public interface TDAABB {
    int Raiz();
    TDAABB HijoIzq();
    TDAABB HijoDer();
    boolean ArbolVacio();
    void InicializarArbol();
    void AgregarElem(int x);
    void EliminarElem(int x);
    int calcularProfundidad(TDAABB t, int x);
}
