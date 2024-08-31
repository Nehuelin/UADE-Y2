package actividades.introduccion.TP2;
import java.util.Scanner;

public class TP2_2 {
    public static void main(String[] args) {
        System.out.println("Codifique un programa que permita ingresar dos numeros. \nSe le preguntara al usuario si dichos numeros quiere sumarlos o restarlos. \nSi se ingresa 'S' dichos numeros se sumaran; si ingresa 'R' se restaran. \nLa suma y la resta de dichos numeros se debera hacer con dos funciones. \nEn el caso de la suma, dicho metodo recibira como parametros los dos numeros ingresados y devolvera la suma de los dos numeros. \nEn el caso de la resta se procedera de la misma manera, pero el metodo devolvera la resta de los mismos.");
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar opcion 'S' o 'R': ");
        char opcion = scanner.next().toUpperCase().charAt(0);

        System.out.print("Ingresar primer numero: ");
        int numeroA = scanner.nextInt();

        System.out.print("Ingresar segundo numero: ");
        int numeroB = scanner.nextInt();

        switch (opcion) {
            case 'S':
                System.out.println(numeroA+" + "+numeroB+" = "+suma(numeroA, numeroB));
                break;
            case 'R':
                System.out.println(numeroA+" - "+numeroB+" = "+resta(numeroA, numeroB));
                break;
        }

        scanner.close();
    }

    static int suma(int x, int y){
        return (x + y);
    }

    static int resta(int x, int y){
        return (x - y);
    }
}
