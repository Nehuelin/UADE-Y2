package actividades.introduccion.TP1;

import java.util.Scanner;

public class TP1_3 { // ESTRUCTURAS ITERATIVAS
        public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingresar numero de actividad (16 a 30): ");
        int actividad = entrada.nextInt();

        switch(actividad){
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
            case 20:
                actividad_20();
                break;
            case 21:
                actividad_21();
                break;
            case 22:
                actividad_22();
                break;
            case 23:
                actividad_23();
                break;
            case 24:
                actividad_24();
                break;
            case 25:
                actividad_25();
                break;
            case 26:
                actividad_26();
                break;
            case 27:
                actividad_27();
                break;
            case 28:
                actividad_28();
                break;
            case 29:
                actividad_29();
                break;
            case 30:
                actividad_30();
                break;
        }
        entrada.close();
    }

    public static void actividad_16(){
        System.out.println("Codifique un programa en Java que permita el ingreso de un numero, y a partir de ellos, mostrar los diez numeros siguientes al mismo. \nResolver el ejercicio con las estructuras iterativas for, while y do-while");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero: ");
        int numero = scanner.nextInt();

        
        System.out.print("\n(FOR) NUMEROS SIGUIENTES A "+numero+": ");
        int copia = numero;
        for (int i = 0; i < 10; i++){
            copia++;
            System.out.print(copia+" ");
        }

        System.out.print("\n(WHILE) NUMEROS SIGUIENTES A "+numero+": ");
        copia = numero;
        int i = 0;
        while (i != 10){
            copia++;
            System.out.print(copia+" ");
            i++;
        }

        System.out.print("\n(DO WHILE) NUMEROS SIGUIENTES A "+numero+": ");
        copia = numero;
        i = 0;
        do{
            copia++;
            System.out.print(copia+" ");
            i++;
        }while(i != 10);

        scanner.close();
    }
    
    public static void actividad_17(){
        System.out.println("Ingresar por teclado 1 numero entero y mostarr por pantalla su tabla de multiplicar entre 1 y 10 (usando la instruccion for).");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero: ");
        int numero = scanner.nextInt();

        int factor = 0;
        for (int i = 0; i < 10; i++){
            factor++;
            System.out.println(numero+"x"+factor+" = "+(numero*factor));
        }

        scanner.close();
    }
    
    public static void actividad_18(){
        System.out.println("Ingresar por teclado 1 numero entero y mostarr por pantalla su tabla de multiplicar entre 1 y 10 (usando la instruccion while).");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero: ");
        int numero = scanner.nextInt();

        int factor = 0;
        while (factor != 10){
            factor++;
            System.out.println(numero+"x"+factor+" = "+(numero*factor));
        }

        scanner.close();
    }

    public static void actividad_19(){
        System.out.println("Crear un programa que muestre en pantalla una escalera inversa de asteriscos. \nLa cantidad de filas de la escalera se ingresa por teclado. \nUtilizar la instruccion for.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar cantidad de filas: ");
        int cantidadFilas = scanner.nextInt();

        for (int fila = cantidadFilas; fila >= 1; fila--){
            for (int asterisco = 0; asterisco < fila; asterisco++) {
                System.out.print("*");
            }
            for (int espacio = 0; espacio < cantidadFilas - fila; espacio++) {
                System.out.print(" ");
            }
            System.out.println();
        }

        scanner.close();
    }

    public static void actividad_20(){
        System.out.println("Desarrollar un algoritmo que permita ingresar un numero N. \nLuego, permitir ingresar N numeros enteros, correspondientes a las notas de un curso. \nLa computadora tendra que mostrar el promedio de las notas ingresadas. \nEJEMPLO: Se ingresa 4, luego 4 7 3 9, la computadora muestra 5.75");
        
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar cantidad de notas: ");
        int cantidadNotas = scanner.nextInt();

        int nota;
        int total = 0;

        for (int i = 0; i < cantidadNotas; i++){
            System.out.print("Ingresar nota: ");
            nota = scanner.nextInt();
            total += nota; 
        }

        double promedio = (double) total / cantidadNotas;
        System.out.println("PROMEDIO: "+promedio);

        scanner.close();
    }

    public static void actividad_21(){
        System.out.println("Desarrollar un algoritmo que permita ingresar un numero natural. \nLa computadora debe mostrar el factorial del numero. \nEJEMPLO: se ingresa 5, la computadora muestra 120");
    
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero natural: ");
        int numero = scanner.nextInt();

        int factorial = 1;

        for (int i = 1; i <= numero; i++){
            factorial *= i;
        }

        System.out.println("FACTORIAL DE "+numero+" = "+factorial);

        scanner.close();
    }

    public static void actividad_22(){
        System.out.println("Crear un programa que muestre en pantalla una escalera de asteriscos. \nLa cantidad de filas de la escalera debera ser una constante. \nUtilizar la instruccion while.");
        
        int cantidadFilas = 5;
        int i = 1;
        int j;

        while (i != cantidadFilas + 1){
            j = 0;
            while(j != i){
                System.out.print("*");
                j++;
            }
            i++;
            System.out.println(); 
        }
    }

    public static void actividad_23(){
        System.out.println("Ingresar por teclado numeros enteros, la carga finaliza cuando se ingresa un cero. \nSe pide calcular y mostrar el numero de valor maximo y el minimo (utilizar do-while)");
        
        Scanner scanner = new Scanner(System.in);

        int numero;
        int maximo = 0;
        int minimo = 1000000000;
        
        do{
            System.out.print("Ingresar numero (0 para terminar): ");
            numero = scanner.nextInt();
            if (numero != 0){
                if (numero > maximo){
                    maximo = numero;
                } else if (numero < minimo){
                    minimo = numero;
                }   
            }
        } while(numero != 0);

        System.out.println("VALOR MAXIMO INGRESADO: "+maximo);
        System.out.println("VALOR MINIMO INGRESADO: "+minimo);

        scanner.close();
    }

    public static void actividad_24(){
        System.out.println("Ingresar por teclado los pesos (en Kg) de los alumnos de un curso. \nLa carga finaliza cuando el peso ingresado es igual a 0. \nSe pide averiguar cual es el promedio de los pesos y mostrarlo con 2 decimales. Utilizar instruccion do-while");
    
        Scanner scanner = new Scanner(System.in);

        int peso;
        float total = 0;
        int i = 0;

        do{
            System.out.print("Ingresar peso (0 para terminar): ");
            peso = scanner.nextInt();
            if (peso != 0){
                total += peso;
                i++;
            } 
        }while(peso != 0);

        float promedio = total / i;

        System.out.println("PROMEDIO: "+promedio);

        scanner.close();
    }

    public static void actividad_25(){
        System.out.println("Teniendo en cuenta que la clave es 'eureka', escribir un algoritmo que pida una clave. \nSolo se otorgan 3 intentos para acertar, si se fallan los 3 intentos se mostrara un mensaje indicando que se agotaron esos 3 intentos. \nSi se acierta la clave, se sale directamente del programa. Usar la instruccion while");

        Scanner scanner = new Scanner(System.in);

        int cantidadIntentos = 3;
        String clave = "eureka";

        while(cantidadIntentos != 0){
            System.out.print("INTENTOS RESTANTES: "+cantidadIntentos+"\nIngresar clave: ");
            String intento = scanner.next();
            
            if(intento.equals(clave)){
                System.out.println("CLAVE CORRECTA! TERMINANDO PROGRAMA");
                break;
            }
            
            cantidadIntentos--;
        } 

        if (cantidadIntentos == 0){
            System.out.println("SE TERMINARON LOS INTENTOS");
        }

        scanner.close();
    }

    public static void actividad_26(){
        System.out.println("Realizar un programa que lea numeros enteros hasta ingresar 0, y muestre el maximo, el minimo (sin considerar el 0) y la media (promedio) de todos ellos.\nUsar la intruccion while");

        Scanner scanner = new Scanner(System.in);

        int total = 0;
        int i = 0;
        int maximo = -1000000000;
        int minimo = 1000000000;
        
        System.out.print("Ingresar numero: ");
        int numero = scanner.nextInt();
        while(numero != 0){
            if (numero != 0){
                total += numero;
                i++;
                if (numero > maximo){
                    maximo = numero;
                } else if (numero < minimo){
                    minimo = numero;
                }
            }
            System.out.print("Ingresar numero: ");
            numero = scanner.nextInt();
        }

        float promedio = (float) total / i; 

        System.out.println("VALOR MAXIMO: "+maximo+"\nVALOR MINIMO: "+minimo+"\nPROMEDIO: "+promedio);

        scanner.close();
    }

    public static void actividad_27(){
        System.out.println("Desarrollar un algoritmo que permita al usuario 12 vaolres, de a uno por vez, pertenecientes a sus sueldos mensuales durante un año. \nLa computadora debe mostrar su sueldo anual. \nSi durante la carga de los sueldos mensuales se detecta un valor negativo, esto indica que aun no se ha cobrado el mes en curso, por lo tanto, deben dejar de ingresarse datos y la computadora debe mostrar la sumatoria de sueldos que se llevan combrados hasta dicho mes");

        Scanner scanner = new Scanner(System.in);

        int sueldoMensual;
        int total = 0;

        for(int i = 1; i < 13; i++){
            System.out.print("Ingresar sueldo del mes "+i+":");
            sueldoMensual = scanner.nextInt();
            if (sueldoMensual < 0){
                System.out.println("NO SE COBRO EL SUELDO DEL MES "+i);
                System.out.println("SUELDO TOTAL ACTUAL: "+total);
                break;
            }
            total += sueldoMensual;
            if (i == 12){
                System.out.println("SUELDO ANUAL: "+total);
            }
        }

        scanner.close();
    }

    public static void actividad_28(){
        System.out.println("Crear un programa que pida al usuario un usuario y una contraseña. \nDebera repetirse hasta que el usuario sea 'admin' y la contraseña sea '1234'");
        
        Scanner scanner = new Scanner(System.in);

        String usuario;
        int contraseña;

        while(true){
            System.out.print("Ingresar usuario: ");
            usuario = scanner.next();

            System.out.print("Ingresar contraseña: ");
            contraseña = scanner.nextInt();

            if(usuario.equals("admin") && contraseña == 1234){
                System.out.println("VALORES CORRECTOS! TERMINANDO PROGRAMA");
                break;
            }

            System.out.println("Usuario o Contraseña incorrectas");
        }
        
        scanner.close();
    }

    public static void actividad_29(){
        System.out.println("Crear un programa que permita calcular la suma de pares de numeros. \nSe deben pedir dos numeros al usuario y se mostrara su suma, volviendo a repetir hasta que ambos numeros introducidos sean 0");

        Scanner scanner = new Scanner(System.in);

        int numeroA;
        int numeroB;

        System.out.print("Ingresar numero A (0 para terminar): ");
        numeroA = scanner.nextInt();

        System.out.print("Ingresar numero B (0 para terminar): ");
        numeroB = scanner.nextInt();

        while(true){
            System.out.println(numeroA+"+"+numeroB+" = "+(numeroA+numeroB));

            System.out.print("Ingresar numero A (0 para terminar): ");
            numeroA = scanner.nextInt();
    
            System.out.print("Ingresar numero B (0 para terminar): ");
            numeroB = scanner.nextInt();

            if (numeroA == 0 && numeroB == 0){
                break;
            }
        }

        scanner.close();
    }

    public static void actividad_30(){
        System.out.println("Realice un programa que divida dos numeros que introduzca el usuario. \nSi el segundo numero es cero, se le debera avisar y volver a pedir tantas veces como sea necesario, hasta que introduzca un numero distinto de cero, momento en que se calculara y mostrara el resultado de la division");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar numero A: ");
        int numeroA = scanner.nextInt();

        System.out.print("Ingresar numero B: ");       
        int numeroB = scanner.nextInt();

        while(numeroB == 0){
            System.out.println("ERROR: Division por 0");
            System.out.print("Ingresar numero B: ");       
            numeroB = scanner.nextInt();           
        }

        System.out.println(numeroA+"/"+numeroB+" = "+(numeroA/numeroB));

        scanner.close();
    }
}
