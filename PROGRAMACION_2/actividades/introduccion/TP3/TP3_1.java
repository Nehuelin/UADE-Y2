package actividades.introduccion.TP3;
import java.util.Scanner;

public class TP3_1 { // ARREGLOS UNIDIMENSIONALES
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingresar numero de actividad (1 A 15): ");
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

    static void actividad_1(){
        System.out.println("Crear un array con un tamaño de 5, asignarle los valores numericos ingresador por teclado y mostrarlos por pantalla");

        Scanner scanner = new Scanner(System.in);
        
        int[] arreglo = new int[5];
        for(int i = 0; i < arreglo.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(arreglo.length - i)+"): ");
            arreglo[i] = scanner.nextInt();
        }

        System.out.println("VALORES INGRESADOS: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
        }

        scanner.close();
    }

    static void actividad_2(){
        System.out.println("Desarrollar un algoritmo que permita mostrar un arreglo de enteros con sus valores a la mitad. \nEJEMPLO: Arreglo {1,2,3,4}, se muestra 0.5 1.0 1.5 2.0");
        
        Scanner scanner = new Scanner(System.in);

        int[] arreglo = new int[4];
        for(int i = 0; i < arreglo.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(arreglo.length - i)+"): ");
            arreglo[i] = (scanner.nextInt());
        }
        
        System.out.print("\nVALORES INGRESADOS: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
        }

        System.out.print("\nLISTA RESULTADO: ");
        for(int elemento : arreglo){
            double mitad = elemento / 2.0;
            System.out.print(mitad+" ");
        }

        scanner.close();
    }

    static void actividad_3(){
        System.out.println("Desarrollar un algoritmo que permita mostrar un arreglo de enteros con sus valores a la mitad. \nEJEMPLO: Arreglo {'A','V','A','J'}, se muestra 'J','A','V','A'.");

        Scanner scanner = new Scanner(System.in);

        char[] arreglo = new char[4];
        for (int i = 0; i < arreglo.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(arreglo.length - i)+"): ");
            arreglo[i] = (scanner.next().charAt(0));
        }
        
        System.out.print("\nVALORES INGRESADOS: ");
        for(char caracter : arreglo){
            System.out.print(caracter+" ");
        }

        char[] arregloInverso = new char[4];
        for(int i = 0; i < arreglo.length; i++){
            arregloInverso[arreglo.length - 1 - i] = arreglo[i];
        }

        System.out.print("\nLISTA RESULTANTE: ");
        for(char caracter : arregloInverso){
            System.out.print(caracter+" ");
        }
        
        scanner.close();
    }

    static void actividad_4(){
        System.out.println("Crea un array con un tamaño de 10, insertar los valors numericos de cualquier manera vista y mostrar por pantalla la media de los valores (promedio) del array. \nNOTA: Puedes utilizar el metodo random de la clase Math para generar numeros aleatorios al generar el array.");

        int[] arreglo = new int[10];

        for(int i = 0; i < arreglo.length; i++){
            double numeroRandom = Math.random()*11;
            arreglo[i] = (int) numeroRandom;
        }

        double total = 0;
        double cantidad = 0;

        System.out.print("LISTA: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
            total += elemento;
            cantidad++;
        }

        System.out.println("\nPROMEDIO: "+(total/cantidad));
    }

    static void actividad_5(){
        System.out.println("Crear un arreglo de n posiciones y llenarlos con nombres de personas");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar cantidad de posiciones: ");
        int n = scanner.nextInt();

        String[] personas = new String[n];

        for(int i = 0; i < personas.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(personas.length - i)+"): ");
            personas[i] = scanner.next(); 
        }

        System.out.print("\nLISTA RESULTANTE: ");
        for(String persona : personas){
            System.out.print(persona+" ");
        }

        scanner.close();
    }

    static void actividad_6(){  
        System.out.println("Crear un arreglo de n posiciones y llenarlos con los numeros que el usuario desee. \nLuego, busque en el array un numero ingresado por teclado.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar cantidad de posiciones: ");
        int n = scanner.nextInt();

        int[] numeros = new int[n];

        for(int i = 0; i < numeros.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(numeros.length - i)+"): ");
            numeros[i] = scanner.nextInt(); 
        }       

        System.out.print("\nLISTA RESULTANTE: ");
        for(int numero : numeros){
            System.out.print(numero+" ");
        }

        System.out.print("\nIngresar valor a buscar: ");
        int numeroObjetivo = scanner.nextInt();

        boolean integraLista = false;
        for(int numero : numeros){
            if(numero == numeroObjetivo){
                integraLista = true;
                break;
            }
        }

        if(integraLista){
            System.out.println("El numero "+numeroObjetivo+" integra la lista");
        }else{
            System.out.println("El numero "+numeroObjetivo+" NO integra la lista");
        }
        
        scanner.close();
    }

    static void actividad_7(){
        System.out.println("Desarrollar un algoritmo que permita pedir al usuario un numero entero T y otro M. \nLa computadora debe crear un arreglo de enteros de T posiciones, cargados con los multiplos de M y mostrarlos por pantalla. \nEJEMPLO: Se ingresa 4 y 6, la computadora muestra 0 6 12 18");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar cantidad de posiciones: ");
        int t = scanner.nextInt();

        System.out.print("Ingresar valor a multiplicar: ");
        int m = scanner.nextInt();

        int[] arreglo = new int[t];
        for(int i = 0; i < arreglo.length; i++){
            arreglo[i] = m * i;
        }

        System.out.print("LISTA RESULTANTE: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
        }

        scanner.close();
    }

    static void actividad_8(){
        System.out.println("Desarrollar un algoritmo que permita ingresar 5 numeros pertenecientes al arreglo A y otros 5 numeros pertenecientes al arreglo B. \nLa computadora debe crear y mostrar un arreglo C, donde cada posicion es el resultado de la suma del numero de la misma posicion en el arreglo A con el numero en la mismo posicion en el arreglo B. \nEJEMPLO: Se ingresa 1 2 3 4 5 y 4 7 1 3 6, la computadora muestra 5 9 4 7 11.");
    
        Scanner scanner = new Scanner(System.in);

        int[] arregloA = new int[5];
        int[] arregloB = new int[5];
        int[] arregloC = new int[5];

        for(int i = 0; i < arregloA.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(arregloA.length - i)+"): ");
            arregloA[i] = scanner.nextInt(); 
        }

        for(int i = 0; i < arregloB.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(arregloB.length - i)+"): ");
            arregloB[i] = scanner.nextInt(); 
        }

        for(int i = 0; i < arregloC.length; i++){
            arregloC[i] = arregloA[i] + arregloB[i];
        }

        System.out.print("LISTA RESULTANTE: ");
        for(int elemento : arregloC){
            System.out.print(elemento+" ");
        }

        scanner.close();
    }

    static void actividad_9(){
        System.out.println("Llenar un vector con numeros enteros (numeros positivos o negativos). Mostrar la cantidad de numeros positivos y la cantidad de numeros negativos que hay en dicho arreglo.");

        int[] arreglo = new int[10];

        for(int i = 0; i < arreglo.length; i++){
            double numeroAleatorio = -10 + (Math.random() * (10 - (-10) + 1));
            arreglo[i] = (int) numeroAleatorio;
        }

        int positivos = 0;
        int negativos = 0;

        System.out.print("LISTA RESULTANTE: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
            if (elemento > 0) {
                positivos++;
            } else if (elemento < 0){
                negativos++;
            }
        }

        System.out.println("\nNUMEROS POSITIVOS: "+positivos);
        System.out.println("NUMEROS NEGATIVOS: "+negativos);
    }

    static void actividad_10(){
        System.out.println("Almacenar en un arreglo de n posiciones nombres de paises. \nImplementar una opcion que al digitar una posicion muestre el dato que contiene.");

        Scanner scanner = new Scanner(System.in);

        String[] paises = new String[5];

        for(int i = 0; i < paises.length; i++){
            System.out.print("Ingresar valor (VALORES RESTANTES -> "+(paises.length - i)+"): ");
            paises[i] = scanner.next();
        }

        System.out.print("PAISES: ");
        for(String pais : paises){
            System.out.print(pais+" ");
        }

        System.out.print("\nIngresar posicion para recuperar dato: ");
        int index = scanner.nextInt();

        System.out.println("VALOR OBTENIDO: "+paises[index]);

        scanner.close();
    }

    static void actividad_11(){
        System.out.println("Cargar un vector con numeros aleatorios y poner en blanco una posicion determinada por el usuario");

        Scanner scanner = new Scanner(System.in);

        int[] arreglo = new int[5];

        for(int i = 0; i < arreglo.length; i++){
            double numeroAleatorio = Math.random()*10;
            arreglo[i] = (int) numeroAleatorio;
        }

        System.out.print("LISTA RESULTANTE: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
        }

        System.out.print("\nIngresar posicion para vaciar espacio: ");
        int index = scanner.nextInt();

        arreglo[index] = 0;

        System.out.print("LISTA RESULTANTE: ");
        for(int elemento : arreglo){
            System.out.print(elemento+" ");
        }
        
        scanner.close();
    }

    static void actividad_12(){
        System.out.println("Crear un array el cual su tamaño es indicado por teclado, y crear una funcion que rellener el array o arreglo con los multiplos de un numero pedido por teclado. Mostrarlos por pantalla usando otra funcion distinta.");
        
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar tamaño del arreglo: ");
        int tamano = scanner.nextInt();

        int[] arreglo = new int[tamano];
    
        System.out.print("Ingresar numero: ");
        int numero = scanner.nextInt();

        arreglo = rellenarArreglo(arreglo, numero);

        System.out.print("\nLISTA RESULTANTE: ");
        imprimirArreglo(arreglo);

        scanner.close();
    }

    static void actividad_13(){
        System.out.println("Busca los dos mayores de un array de N datos");

        double n = Math.random()*10;
        int[] arreglo = new int[(int) n];

        for (int i = 0; i < arreglo.length; i++){
            double numero = Math.random()*30;
            arreglo[i] = (int) numero;
        }

        System.out.print("\nLISTA RESULTANTE: ");
        imprimirArreglo(arreglo);

        int maximo = 0;
        for (int elemento : arreglo){
            if (elemento > maximo){
                maximo = elemento;
            }
        }

        int segundoMaximo = 0;
        for (int elemento : arreglo){
            if (elemento > segundoMaximo && elemento != maximo){
                segundoMaximo = elemento;
            }
        }

        System.out.println("\nMAXIMO: "+maximo+"\nSEGUNDO MAXIMO: "+segundoMaximo);
    }

    static void actividad_14(){
        System.out.println("Buscar el mayor valor de un array de N datos utilizando un bucle for mejorado");
        
        double n = Math.random()*10;
        int[] arreglo = new int[(int) n];
    
        for (int i = 0; i < arreglo.length; i++){
            double numero = Math.random()*30;
            arreglo[i] = (int) numero;
        }

        System.out.print("\nLISTA RESULTANTE: ");
        imprimirArreglo(arreglo);

        int maximo = 0;
        for (int elemento : arreglo){
            if (elemento > maximo){
                maximo = elemento;
            }
        }

        System.out.println("\nMAXIMO: "+maximo);
    }

    static void actividad_15(){
        System.out.println("Escribir un programa para realizar la busqueda del nombre de un cliente en un vector que contiene 5 clientes en total. \nEl cliente a buscar sera ingresado por teclado por el usuario. \nEl algoritmo debera devolver, en caso de que ese nombre exista, la posicion en donde se encuentra dicho cliente dentro del vector");
    
        Scanner scanner = new Scanner(System.in);

        String[] clientes = {"Lorena", "Nehuel", "Nayla", "Ariel", "Lola"};

        System.out.print("Ingresar cliente a buscar: ");
        String clienteObjetivo = scanner.next();

        for(int i = 0; i < clientes.length; i++){
            if (clientes[i].equals(clienteObjetivo)){
                System.out.println("El cliente "+clienteObjetivo+" se encuentra en la posicion "+i);
                break;
            }
        }

        scanner.close();
    }

    // VVV FUNCIONES DEL EJERCICIO 12 VVV 
    static int[] rellenarArreglo(int[] arr, int x){
        for(int i = 0; i < arr.length; i++){
            arr[i] = x * (i+1);
        }
        return arr;
    }

    static void imprimirArreglo(int[] arr){
        for(int elemento : arr){
            System.out.print(elemento+" ");
        }
    }
}
