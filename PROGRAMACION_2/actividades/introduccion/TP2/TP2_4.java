package actividades.introduccion.TP2;

public class TP2_4 {
    public static void main(String[] args) {
        System.out.println("Crear una funcion cubo que reciba un numero y lo devuelva elevado al cubo");

        int numero = 2;

        System.out.println("El cubo de "+numero+" es "+cubo(numero));
    }

    static int cubo(int x){
        return((int) Math.pow(x, 3));
    }
}
