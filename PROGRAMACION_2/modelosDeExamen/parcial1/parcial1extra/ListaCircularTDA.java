package modelosDeExamen.parcial1.parcial1extra;

public interface ListaCircularTDA {
    void InicializarLista();
    void Agregar(int x);
    void Eliminar(int x);
    boolean ListaVacia();
    boolean Existe(int x);
    String MostrarLista();
}
