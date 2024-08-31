package actividades.introduccion.TP2;

public class TP2_6 {
    public static void main(String[] args) {
        System.out.println("Crear una funcion mayorDeTres que reciba tres numeros enteros y devuelva el mayor valor de los tres. Por ejemplo, para los numeros 5, 7, 5, la funcion devuelve 7");
    
        int numeroA = 5;
        int numeroB = 7;
        int numeroC = 5;

        System.out.println("El mayor de "+numeroA+", "+numeroB+" y "+numeroC+" es "+mayorDeTres(numeroA, numeroB, numeroC));
    }

    static int mayorDeTres(int x, int y, int z){
        int maximo = Math.max(y, z);
        return Math.max(x, maximo);
    }
}
