package actividades.introduccion.TP1;
import java.util.Scanner;

public class TP1_2 { // ESTRUCTURAS CONDICIONALES, SELECTIVAS, OPERADORES LOGICOS Y RELACIONALES
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingresar numero de actividad (7 a 15): ");
        int actividad = entrada.nextInt();

        switch(actividad){
            case 7:
                actividad_7();
                break;
            case 8:
                actividad_8();
                break;
            case 9:
                actividad_9();
                break;
            case 10:
                actividad_10();
                break;
            case 11:
                actividad_11();
                break;
            case 12:
                actividad_12();
                break;
            case 13:
                actividad_13();
                break;
            case 14:
                actividad_14();
                break;
            case 15:
                actividad_15();
                break;
        }
        entrada.close();
    }

    public static void actividad_7(){
        System.out.println("Codifique un programa en Java que permita saber si un numero ingresado por teclado es par o impar");
    
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingresar numero: ");
        int numero = scanner.nextInt();

        if (numero % 2 == 0){
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }

        scanner.close();
    }
    
    public static void actividad_8(){
        System.out.println("Desarrollar un algoritmo que, dada la edad de una persona (entre 1 y 120 años) y su genero ('F' para mujeres, 'M' para hombres), la computadora indique si esta en edad de jubilarse. \nNOTA: las mujeres se jubilan con 60 años o mas, los hombres con 65 años o mas.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar edad de la persona: ");
        int edad = scanner.nextInt();
        
        System.out.print("Ingresar genero de la persona (F para mujer, M para hombre): ");
        char genero = scanner.next().toUpperCase().charAt(0);

        if (genero == 'F') {
            if (edad >= 60) {
                System.out.println("Esta persona se jubila");
            } else {
                System.out.println("Esta persona NO se jubila");
            }
        } else if (genero == 'M') {
            if (edad >= 65) {
                System.out.println("Esta persona se jubila");
            } else {
                System.out.println("Esta persona NO se jubila");
            }
        }

        scanner.close();
    }

    public static void actividad_9(){
        System.out.println("Desarrollar un algoritmo que, dada la cantidad de alumnos de un curso y la cantidad de sillas disponibles, la computadora indique si alcanzan las sillas, en caso contrario, indique cuantas sillas faltan para que todo el alumnado tenga asiento.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar cantidad de alumnos: ");
        int alumnos = scanner.nextInt();

        System.out.print("Ingresar cantidad de sillas: ");
        int sillas = scanner.nextInt();

        if (sillas >= alumnos){
            System.out.println("Alcanzan las sillas");
        } else {
            int faltantes = alumnos - sillas;
            System.out.println("Faltan "+faltantes+" Sillas para sentar a todo el alumnado");
        }

        scanner.close();
    }

    public static void actividad_10(){
        System.out.println("Desarrollar un algoritmo que, dados dos numeros enteros entre 0 y 100, la computadora indique si el mayor es divisible por el menor. \nEJEMPLO: ingresar 4 y 28, debe imprimir '28 es divisible por 4'. \nSe debera validar que los numeros ingresados se encuentren entre 0 y 100");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero A: ");
        int numeroA = scanner.nextInt(); 
        while (numeroA < 0 || numeroA > 100){
            System.out.println("ERROR: El numero debe estar entre 0 y 100.");
            System.out.print("Ingresar numero A: ");
            numeroA = scanner.nextInt(); 
        }
        
        System.out.print("Ingresar numero B: ");
        int numeroB = scanner.nextInt(); 
        while (numeroB < 0 || numeroB > 100){
            System.out.println("ERROR: El numero debe estar entre 0 y 100.");
            System.out.print("Ingresar numero B: ");
            numeroB = scanner.nextInt(); 
        }
        
        int mayor = Math.max(numeroA, numeroB);
        int menor = Math.min(numeroA, numeroB);

        if (mayor % menor == 0){
            System.out.println(mayor+" es divisible por "+menor);
        } else {
            System.out.println(mayor+" NO es divisible por "+menor);
        }
        
        scanner.close();
    }

    public static void actividad_11(){
        System.out.println("Desarrollar un algoritmo que permita ingresar los lados A, B y C de un triangulo. \nLa computadora informara si el triangulo es o no valido. \nEn caso afirmativo, ademas informar si es equilatero, isosceles o escaleno.");
        System.out.println("CONSEJO: Segun el teorema de desigualdad triangular, un triangulo es valido si se cumple que cada uno de los lados no puede ser mas largo que la suma de los otros dos.\nUn triangulo EQUILATERO es aquel que tiene sus tres lados iguales. \nUn triangulo ISOSCELES es aquel que tiene dos de sus lados iguales. \nUn triangulo ESCALENO es aquel que tiene sus tres lados desiguales.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar lado A: ");
        int ladoA = scanner.nextInt();

        System.out.print("Ingresar lado B: ");
        int ladoB = scanner.nextInt();

        System.out.print("Ingresar lado C: ");
        int ladoC = scanner.nextInt();

        boolean esTriangulo = ladoA <= (ladoB + ladoC) && ladoB <= (ladoA + ladoC) && ladoC <= (ladoA + ladoB);
        
        if (esTriangulo){
            if (ladoA == ladoB && ladoB == ladoC){
                System.out.println("Es un triangulo Equilatero");
            } else if (ladoA == ladoB || ladoB == ladoC || ladoA == ladoC){
                System.out.println("Es un triangulo Isosceles");
            } else {
                System.out.println("Es un triangulo Escaleno");
            }
        } else {
            System.out.println("NO es un triangulo");
        }

        scanner.close();
    }

    public static void actividad_12(){
        System.out.println("Desarrollar un algoritmo que permita ingresar un caracter. \nLa computadora indica si es o no una letra vocal (utilizar switch-case)");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar caracter: ");
        char caracter = scanner.next().toLowerCase().charAt(0);

        boolean esVocal;

        switch (caracter) {
            case 'a':
                esVocal = true;
                break;
            case 'e':
                esVocal = true;
                break;
            case 'i':
                esVocal = true;
                break;
            case 'o':
                esVocal = true;
                break;
            case 'u':
                esVocal = true;
                break;
            default:
                esVocal = false;
                break;
        }

        if (esVocal) {
            System.out.println("El caracter es una vocal");
        } else {
            System.out.println("El caracter NO es una vocal");
        }

        scanner.close();
    }

    public static void actividad_13(){
        System.out.println("Desarrollar un algoritmo que pida al usuario un numero entre 1 y 12. \nLa computadora muestra por pantalla el mes al que pertenece tal numero. \nSi se ingrea un numero fuera de rango, mostrar un error. \nEJEMPLO: se ingresa un 4, la computadora muestra: 'ABRIL' (utilizar switch-case)");
    
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero entre 1 y 12: ");
        int numero = scanner.nextInt();

        switch (numero) {
            case 1:
                System.out.println("ENERO");
                break;
            case 2:
                System.out.println("FEBRERO");
                break;
            case 3:
                System.out.println("MARZO");
                break;
            case 4:
                System.out.println("ABRIL");
                break;
            case 5:
                System.out.println("MAYO");
                break;
            case 6:
                System.out.println("JUNIO");
                break;
            case 7:
                System.out.println("JULIO");
                break;
            case 8:
                System.out.println("AGOSTO");
                break;
            case 9:
                System.out.println("SEPTIEMBRE");
                break;
            case 10:
                System.out.println("OCTUBRE");
                break;
            case 11:
                System.out.println("NOVIEMBRE");
                break;
            case 12:
                System.out.println("DICIEMBRE");
                break;
            default:
                System.out.println("Termino no valido");
                break;
        }
        
        scanner.close();
    }

    public static void actividad_14(){
        System.out.println("Desarrollar un algoritmo que permita el ingreso de una letra, correspondiente a un digito del sistema de numeracion romano. \nLa computadora debe mostrar su correspondiente valor decimal. \nSi se ingresa una letra inexistente, la computadora informara que no existe tal digito. \nEJEMPLO: Se ingresa 'D', se muestra 500");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar letra: ");
        char letra = scanner.next().toUpperCase().charAt(0);

        switch (letra) {
            case 'I':
                System.out.println("1");
                break;
            case 'V':
                System.out.println("5");
                break;
            case 'X':
                System.out.println("10");
                break;
            case 'L':
                System.out.println("50");
                break;
            case 'C':
                System.out.println("100");
                break;
            case 'D':
                System.out.println("500");
                break;
            case 'M':
                System.out.println("1000");
                break;
            default:
                System.out.println("Valor invalido");
                break;
        }

        scanner.close();
    }

    public static void actividad_15(){
        System.out.println("Desarrollar un algoritmo que simule una calculadora basica que realice operaciones de suma, resta, multiplicacion y division. \nSe deben recibir como entrada dos numeros reales y un operador, que puede ser '+', '-', '*' o '/'. \nLa salida del programa debe ser el resultado de la operacion. \nCONSEJO: prever que se puede llegar a intentar hacer una division por 0");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar primer numero: ");
        double numeroA = scanner.nextDouble();

        System.out.print("Ingresar segundo numero: ");
        double numeroB = scanner.nextDouble();

        System.out.print("Ingresar operacion a realizar ('+' para suma, '-' para resta, '*' para multiplicacion, '/' para division): ");
        char operador = scanner.next().charAt(0);

        switch (operador) {
            case '+':
                System.out.println("La suma da: "+(numeroA + numeroB));
                break;
            case '-':
                System.out.println("La resta da: "+(numeroA - numeroB));
                break;
            case '*':
                System.out.println("La multiplicacion da: "+(numeroA * numeroB));
                break;
            case '/':
                if(numeroB != 0){
                    System.out.println("La division da: "+(numeroA / numeroB));
                } else {
                    System.out.println("ERROR: No se puede dividir por 0");
                }
                break;
            default:
                System.out.println("Valor invalido");
                break;
        }

        scanner.close();
    }
}
