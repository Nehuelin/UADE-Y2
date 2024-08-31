package actividades.introduccion.TP1;
import java.util.Scanner;

public class TP1_1{ // VARIABLES, CONSTANTES, TIPOS DE DATOS, OBJETO SCANNER, OPERADORES URINARIOS, BINARIOS Y MATEMATICOS, CASTING
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingresar numero de actividad: ");
        int actividad = entrada.nextInt();

        switch(actividad){
            case 1:
                actividad_1();
                break;
            case 2:
                actividad_2();
                break;
            case 3:
                actividad_3();
                break;
            case 4:
                actividad_4();
                break;
            case 5:
                actividad_5();
                break;
            case 6:
                actividad_6();
                break;
        }
        entrada.close();
    }

    public static void actividad_1(){
        System.out.println("Ingresar el area de un cuadrado por teclado utilizando un objeto Scanner. \nCalcular e imprimir el valor del perimetro. \nEJEMPLO: Ingresa 25, debe devolver 20\n");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresar area del cuadrado");
        double area = scanner.nextInt();

        double lado = Math.sqrt(area);
        double perimetro = lado*4;

        System.out.println("PERIMETRO: "+perimetro);
        scanner.close();
    }

    public static void actividad_2(){
        System.out.println("Desarrollar un algoritmo que permita ingresar dos numeros enteros por teclado utilizando un objeto Scanner. \nLa computadora debera mostrar su cociente entero. \nEl resto se debera mostrar en otra linea. \nEJEMPLO: Ingresa 23 y 5, debe devolver 4 y, en otra linea, 3.\n");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresar primer numero: ");
        int numero1 = scanner.nextInt();
        
        System.out.print("Ingresar segundo numero: ");
        int numero2 = scanner.nextInt();

        int cociente = numero1 / numero2;
        int resto = numero1 % numero2;
        
        System.out.print("COCIENTE: "+cociente+"\nRESTO: "+resto);
        scanner.close();
    }

    public static void actividad_3(){
        System.out.println("Desarrollar un algoritmo que permita ingresar dos numeros enteros por teclado. La computadora debera mostrar su cociente con decimales. \nCONSEJO: utilizar casting\n");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresar primer numero: ");
        int numero1 = scanner.nextInt();

        System.out.print("Ingresar segundo numero: ");
        int numero2 = scanner.nextInt();

        double cociente = (double) numero1 / numero2;
        System.out.print("COCIENTE CON DECIMALES: "+cociente);  
        scanner.close();
    }

    public static void actividad_4(){
        System.out.println("Ingresar por teclado el diametro (int) de un circulo y calcular su perimetro, pero solo debera mostrar la parte entera del resultado. \nDefina el valor de pi como una constante con valor 3.14.\nEJEMPLO: Ingresa 10, debe devolver 31. \nRealice casting para obtener la parte entera del resultado\n");
        
        double pi = 3.14;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese valor del diametro: ");
        int diametro = scanner.nextInt();

        double perimetro = pi * diametro;

        int parteEntera = (int) perimetro;
        System.out.println("PERIMETRO = "+parteEntera);
        scanner.close();
    }

    public static void actividad_5(){
        System.out.println("Ingresar por teclado el radio (int) de un circulo y calcular su perimetro y superficie (ambos double). \nUtilize la clase Math para obtener el valor de PI. \nEJEMPLO: Ingresa 5, debe devolver perimetro = 31.41592654 y superficie = 78.53981634\n");
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese valor del radio: ");
        int radio = scanner.nextInt();
        double pi = Math.PI;

       double perimetro = 2 * pi * radio;
       double superficie = pi * Math.pow(radio, 2);
       
       System.out.println("PERIMETRO = "+perimetro+"\nSUPERFICIE = "+superficie);
       scanner.close();
    }

    public static void actividad_6(){
        System.out.println("Ingresar por teclado los lados de un triangulo rectangulo (todos int) y calcular el perimetro y su superficie. \nPara la raiz cuadrada de la hipotenusa debera utilizar la clase Math. \nLa superficie es (base * altura) / 2 y el perimetro de base + altura + hipotenusa. \nHipotenusa = sqrt(base^2 + altura^2)");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar base y altura del triangulo: ");
        int base = scanner.nextInt(); 
        int altura = scanner.nextInt(); 

        double hipotenusa = Math.sqrt(Math.pow(base, 2) + Math.pow(altura, 2));
        
        double superficie = (base * altura) / 2;
        double perimetro = base + altura + hipotenusa;

        System.out.println("SUPERFICIE = "+superficie+ "\nPERIMETRO = "+perimetro);
        scanner.close();
    }

}