package modelosDeExamen.parcial1.parcial1tema2;

public class DiccionarioSimple implements DiccionarioSimpleTDA{
	private class NodoClave{
		Empleado valor;
		NodoClave sigClave;
	}
	private NodoClave origen;

	public void InicializarDiccionario() {
		origen = null;
	}
	public void Agregar(int legajo, String nombre, double sueldo ) {
		NodoClave nc = Clave2NodoClave(legajo);
		if (nc == null) {
			nc = new NodoClave();
			nc.valor.legajo = legajo;
			nc.sigClave = origen;
			origen = nc;
		}
		nc.valor.nombre = nombre;
		nc.valor.sueldo = sueldo;
	}
	public void Eliminar(int legajo) {
		if (origen != null) {
			if (origen.valor.legajo == legajo) {
				origen = origen.sigClave;
			}
			else {
				NodoClave aux = origen;
				while(aux.sigClave != null && aux.sigClave.valor.legajo != legajo) {
					aux = aux.sigClave;
				}
				if (aux.sigClave != null) {
					aux.sigClave = aux.sigClave.sigClave;
				}
			}
		}
	}
	public Empleado Recuperar(int legajo) {
		NodoClave nc= Clave2NodoClave(legajo);
		return nc.valor;
	}

	public ConjuntoTDA Claves() {
		ConjuntoTDA c = new Conjunto();
		c.InicializarConjunto();
		NodoClave aux = origen;
		while (aux != null) {
			c.Agregar(aux.valor.legajo);
			aux = aux.sigClave;
		}
		return c;
	}
	private NodoClave Clave2NodoClave(int legajo) {
		NodoClave aux = origen;
		while (aux != null && aux.valor.legajo != legajo) {
			aux = aux.sigClave;
		}
		return aux;
	}
}
