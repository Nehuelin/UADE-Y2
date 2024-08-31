package tdas;
import tdas.ConjuntoTDA;

@SuppressWarnings("unused")
public interface DiccionarioSimpleTDA {
    void inicializarDiccionario();
    void agregar(int clave, int valor);
    void eliminar(int clave);
    int recuperar(int clave);
    ConjuntoTDA claves();
    void imprimirDiccionario();
}
