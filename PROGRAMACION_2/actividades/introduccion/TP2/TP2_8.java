package actividades.introduccion.TP2;

public class TP2_8 {
    public static void main(String[] args) {
        System.out.println("Definir la funcion azar, la cual devuelve un numero entero aleatorio entre 0 y n (recibido por parametro), sin incluir este ultimo. \nEJEMPLO: Se invoca azar(10), devulevle un numero entre 0 y 9.");

        int numero = 10;

        System.out.println("NUMERO ALEATORIO ENTRE 0 Y "+(numero - 1)+": "+azar(numero));
    }

    static int azar(int n){
        double randomDecimal = Math.random()*n;
        return (int) randomDecimal;
    }
}
