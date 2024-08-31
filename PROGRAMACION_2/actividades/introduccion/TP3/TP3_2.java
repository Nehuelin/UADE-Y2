package actividades.introduccion.TP3;
import java.util.Scanner;

public class TP3_2 { // ARREGLOS MULTIDIMENSIONALES
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingresar numero de actividad (16 a 19): ");
        int actividad = entrada.nextInt();

        switch (actividad) {
            case 16:
                actividad_16();
                break;
            case 17:
                actividad_17();
                break;
            case 18:
                actividad_18();
                break;
            case 19:
                actividad_19();
                break;
        }

        entrada.close();
    }

    static void actividad_16(){
        System.out.println("Llenar una matriz de 3x3 completamente de numeros aleatorios entre 0 y 9");

        int[][] matriz = new int[3][3];
        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[i].length; j++){
                double numero = Math.random()*10;
                matriz[i][j] = (int) numero;
            }
        }

        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[i].length; j++){
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }
    }

    static void actividad_17(){
        System.out.println("Crear una matriz de NxN y llenarla con los numeros que el usuario desee. \nSume todos los numeros que componga la columna 1 y muestre el resultado por pantalla.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar tamaño de la matriz: ");
        int n = scanner.nextInt();

        int[][] matriz = new int[n][n];
        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[i].length; j++){
                double numero = Math.random()*10;
                matriz[i][j] = (int) numero;
            }
        }

        int total = 0;

        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[i].length; j++){
                if (j == 1){
                    total += matriz[i][j];
                }
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }

        System.out.println("SUMA TOTAL DE LA COLUMNA 1 (base0): "+total);

        scanner.close();
    }

    static void actividad_18(){
        System.out.println("Diseñar un algoritmo que recorra las butacas de una sala de cine y determine cuantas butacas desocupadas hay en la sala. \nSuponga que inicialmente tiene un array con valores booleanos que si es verdadero implica que esta ocupada y si es falso la butaca esta desocupada. \nTenga en cuenta que el array debera ser creado e inicializado al principio del algoritmo.\n");
    
        char[][] sala = new char[30][15];

        boolean butacaOcupada;
        
        for(int i = 0; i < sala.length; i++){
            for(int j = 0; j < sala[i].length; j++){
                butacaOcupada = butacaRandomizer();
                if(butacaOcupada){
                    sala[i][j] = 'X';
                }else{
                    sala[i][j] = 'o';
                }
            }
        }

        int desocupadas = 0;

        for(int i = 0; i < sala.length; i++){
            for(int j = 0; j < sala[i].length; j++){
                if(sala[i][j] == 'o'){
                    desocupadas ++;
                }
                System.out.print(sala[i][j]+" ");
            }
            System.out.println();
        }

        System.out.println("BUTACAS DESOCUPADAS: "+desocupadas);
    }   

    static void actividad_19(){
        System.out.println("Una escuela tiene un total de 3 aulas con la siguiente capacidad: \nAZUL: 40 bancos \nVERDE: 35 bancos \nAMARILLO: 30 bancos \nSabiendo la cantidad de bancos de cada aula, el usuario debera ingresar la cantidad de alumnos inscriptos para cursar tercers grado y el sistema debera determinar que aula es la indicada para la cantidad ingresada. \nLa escuela ya sabe que la maxima capacidad sus aulas es de 40 alumnos, por lo tanto, la cantidad de alumnos inscriptos que ingresa el usuario siempre tendra que ser un numero menor o igual a 40. \nSe espera que el aula ingresada sea la que deje menos bancos libres.");
    
        Scanner scanner = new Scanner(System.in);

        // int capacidadAzul = 40;
        int capacidadVerde = 35;
        int capacidadAmarillo = 30;


        System.out.print("Ingrese la cantidad de alumnos inscritos para tercer grado (máximo 40): ");
        int alumnosInscritos = scanner.nextInt();


        if (alumnosInscritos > 40 || alumnosInscritos < 0) {
            System.out.println("La cantidad de alumnos ingresada no es válida.");
            scanner.close();
            return; 
        }

        String aulaIndicada = "";
        if (alumnosInscritos > capacidadAmarillo){
            if (alumnosInscritos > capacidadVerde){
                aulaIndicada = "AZUL";
            } else {
                aulaIndicada = "VERDE";
            }
        } else {
            aulaIndicada = "AMARILLO";
        }

        System.out.println("El aula indicada para " + alumnosInscritos + " alumnos es: " + aulaIndicada);

        scanner.close();
    }

    // vv FUNCIONES EJERCICIO 18 vv
    static boolean butacaRandomizer(){
        double chance = Math.random();
        if (chance >= 0.5){
            return true;
        } else {
            return false;
        }   
    }
}
