package actividades.introduccion.TP2;

public class TP2_5 {
    public static void main(String[] args) {
        System.out.println("Crear una funcion cantidadDeDivisores que reciba un numero entero y devuelva la cantidad de divisores que tiene. EJEMPLO: Recibe como parametro 16, debe devolver 5. \nAYUDA: Un numero es multiplo de otro cuando al dividir los numeros obtengo resto 0");

        int numero = 16;

        System.out.println("El numero "+numero+" tiene "+cantidadDeDivisores(numero)+" divisores");
    }

    static int cantidadDeDivisores(int x){
        int divisores = 0;
        
        for(int i = 1; i <= x; i++){
            if (x % i == 0){
                divisores++;
            }
        }

        return divisores;
    }
}
