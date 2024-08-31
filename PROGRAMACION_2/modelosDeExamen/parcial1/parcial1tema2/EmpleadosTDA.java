package modelosDeExamen.parcial1.parcial1tema2;
// interfaz de empleados.
public interface EmpleadosTDA {
	String mostrarSueldo (int legajo);
	void listarEmpleados ();
	void agregarEmpleado (Empleado empleado);
	void quitarEmpleado (int legajo);
}
