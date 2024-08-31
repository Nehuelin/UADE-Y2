package modelosDeExamen.parcial1.parcial1tema2;

// clase concreta de empleados.
public class Empleados implements EmpleadosTDA {
	private DiccionarioSimple diccionarioEmpleados;
	
	public String mostrarSueldo(int legajo) {
		Empleado aux = diccionarioEmpleados.Recuperar(legajo);
		if (aux != null) {
			return "Nombre: " + aux.getNombre() + "; Sueldo: " + aux.getSueldoACobrar(); 

		}
		else {
			return "Empleado no encontrado.";
		}
	}
	public void listarEmpleados() {
		ConjuntoTDA legajos = diccionarioEmpleados.Claves();
		legajos.InicializarConjunto();
		while (!legajos.ConjuntoVacio()) {
			int legajo = legajos.Elegir();
			Empleado aux = diccionarioEmpleados.Recuperar(legajo);
			System.out.println(aux.toString());
			legajos.Sacar(legajo);
			
		}
		
	}
	public void agregarEmpleado(Empleado empleado) {
		diccionarioEmpleados.Agregar(empleado.getLegajo(), empleado.getNombre(), empleado.getSueldoACobrar());
		
	}
	public void quitarEmpleado (int legajo) {
		diccionarioEmpleados.Eliminar(legajo);
	}
}
