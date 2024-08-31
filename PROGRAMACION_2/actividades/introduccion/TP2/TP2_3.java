package actividades.introduccion.TP2;

public class TP2_3 {
    public static void main(String[] args) {
        System.out.println("Crear una funcion esPar que devuelva el valor logico true o false segun si el numero que se indica como parametro es par o no.");

        boolean valorPar = esPar(2);

        if (valorPar){
            System.out.println("El valor es par.");
        } else {
            System.out.println("El valor es impar.");
        }
    }

    static boolean esPar(int valor){
        return (valor % 2 == 0);
    }
}
