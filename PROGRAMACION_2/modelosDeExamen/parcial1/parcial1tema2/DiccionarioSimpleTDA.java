package modelosDeExamen.parcial1.parcial1tema2;
// interfaz del diccionario simple.
public interface DiccionarioSimpleTDA {
	void InicializarDiccionario();
	void Agregar(int legajo, String nombre, double sueldo);
	void Eliminar(int legajo);
	Empleado Recuperar(int legajo);
	ConjuntoTDA Claves();
}
