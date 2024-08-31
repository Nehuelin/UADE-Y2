package modelosDeExamen.parcial1.parcial1tema2;
// clase concreta de empleado.

public class Empleado implements EmpleadoTDA{
	int legajo;
	String nombre;
	double sueldo;
	
	public int getLegajo() {
		return legajo;
	
	}
	public String getNombre() {
		return nombre;
	}
	public double getSueldoACobrar() {
		return sueldo;
	}
	public String toString() {
		return "Legajo: " + legajo + "; Nombre: " + nombre + "; Sueldo: " + sueldo;
		
	}
}
