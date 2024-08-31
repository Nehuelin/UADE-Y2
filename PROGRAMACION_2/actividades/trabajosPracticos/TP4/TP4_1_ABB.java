package actividades.trabajosPracticos.TP4;

import tdas.TDAABB;
import tdas.ConjuntoTDA;
import arboles.ABB;
import estaticas.conjuntos.ConjuntoA;
import java.util.Random;
import java.util.Scanner;

/*
A partir del TDA ABB, escribir métodos externos que resuelvan los siguientes problemas:
a) Dado un elemento, determinar si está o no en un ABB.
b) Dado un elemento, determinar si es una hoja de un ABB.
c) Dado un elemento, calcular su profundidad en el ABB.
d) Obtener el valor del menor elemento de un ABB.
e) Calcular la cantidad de elementos que contiene un ABB.
f) Calcular la suma de los elementos que contiene un ABB.
g) Calcular la cantidad de hojas de un ABB
h) Calcular la altura de un ABB.
i) Comprobar si dos ABBs tienen la misma forma.
j) Comprobar si dos ABBs son iguales.
k) Contar la cantidad de elementos que están en un cierto nivel N.
l) Mostrar por pantalla todos los elementos que contiene un ABB
i.In-orden
ii.Pre-orden
iii.Post-orden
m) Dado un valor k, arme un conjunto con todos los elementos del ABB que son
mayores que k.
n) Dado un elemento de valor v (que está presente en el ABB), obtener el elemento
del árbol que es inmediatamente anterior (en valor)
 */
public class TP4_1_ABB {
    public static boolean pertenece(TDAABB arbol, int x){
        if (arbol.ArbolVacio()) {
            return false;
        } else if (arbol.Raiz() == x){
            return true;
        } else if (arbol.Raiz() > x){
            return pertenece(arbol.HijoIzq(), x);
        } else {
            return pertenece(arbol.HijoDer(), x);
        }
    }   

    public static boolean esHoja(TDAABB arbol, int x){
        if (arbol.ArbolVacio()) {
            return false;
        } else if (arbol.Raiz() == x && arbol.HijoIzq() == null && arbol.HijoDer() == null){
            return true;
        } else if (arbol.Raiz() > x){
            return pertenece(arbol.HijoIzq(), x);
        } else {
            return pertenece(arbol.HijoDer(), x);
        }
    }   

    public static int calcularProfundidad(TDAABB arbol, int x){
        if (arbol.ArbolVacio()) {
            return 0;
        } else if (arbol.Raiz() == x) {
            return 0;
        } else if (arbol.Raiz() > x) {
            return (1 + calcularProfundidad(arbol.HijoIzq(), x));
        } else {
            return (1 + calcularProfundidad(arbol.HijoDer(), x));
        }
    }

    public static int menorElemento(TDAABB arbol){
        if (arbol.ArbolVacio()){
            return 0;
        } else if (arbol.HijoIzq().ArbolVacio()){
            return arbol.Raiz();
        } else {
            return menorElemento(arbol.HijoIzq());
        }
    }

    public static int cantidadElementos(TDAABB arbol){
        if(arbol.ArbolVacio()){
            return 0;
        } else {
            return (1 + cantidadElementos(arbol.HijoIzq()) + cantidadElementos(arbol.HijoDer()));
        }
    }

    public static int sumarElementos(TDAABB arbol){
        if(arbol.ArbolVacio()){
            return 0;
        } else {
            return (arbol.Raiz() + sumarElementos(arbol.HijoIzq()) + sumarElementos(arbol.HijoDer()));
        }
    }

    public static int cantidadHojas(TDAABB arbol){
        if(arbol.ArbolVacio()){
            return 0;
        } else if (arbol.HijoIzq().ArbolVacio() && arbol.HijoDer().ArbolVacio()){
            return (1 + cantidadHojas(arbol.HijoIzq()) + cantidadHojas(arbol.HijoDer()));
        } else {
            return (cantidadHojas(arbol.HijoIzq()) + cantidadHojas(arbol.HijoDer()));
        }
    }

    public static int calcularAltura(TDAABB arbol) {
        if (arbol.ArbolVacio()) {
            return 0;
        }
        int alturaIzq = calcularAltura(arbol.HijoIzq());
        int alturaDer = calcularAltura(arbol.HijoDer());
        return Math.max(alturaIzq, alturaDer) + 1;
    }

    public static boolean tienenMismaForma(TDAABB arbol1, TDAABB arbol2){
        if(arbol1.ArbolVacio() && arbol2.ArbolVacio()){
            return true;
        } else if (arbol1.ArbolVacio() || arbol2.ArbolVacio()){
            return false;
        } else {
            return tienenMismaForma(arbol1.HijoIzq(), arbol2.HijoIzq()) && tienenMismaForma(arbol1.HijoDer(), arbol2.HijoDer());
        }        
    }

    public static boolean sonIguales(TDAABB arbol1, TDAABB arbol2){
        if(arbol1.ArbolVacio() && arbol2.ArbolVacio()){
            return true;
        } else if (arbol1.ArbolVacio() || arbol2.ArbolVacio()){
            return false;
        } else if (arbol1.Raiz() != arbol2.Raiz()){
            return false;
        } else {
            return sonIguales(arbol1.HijoIzq(), arbol2.HijoIzq()) && sonIguales(arbol1.HijoDer(), arbol2.HijoDer()); 
        }
    }

    public static int cantidadElementosEnNivel(TDAABB arbol, int nivel){
        return cantidadElementosEnNivel(arbol, 0, nivel);
    }
    
    private static int cantidadElementosEnNivel(TDAABB arbol, int nivelActual, int nivelObjetivo){
        if(arbol.ArbolVacio()){
            return 0;
        } else if (nivelActual == nivelObjetivo){
            return 1;
        } else {
            return cantidadElementosEnNivel(arbol.HijoIzq(), nivelActual + 1, nivelObjetivo) + cantidadElementosEnNivel(arbol.HijoDer(), nivelActual + 1, nivelObjetivo);
        }
    }

    public static void imprimirElementos(TDAABB arbol){
        System.out.print("ELEMENTOS EN PRE-ORDER: [");
        preOrder(arbol); // i)
        System.out.print("]\n");

        System.out.print("ELEMENTOS EN IN-ORDER: [");
        inOrder(arbol); // ii)
        System.out.print("]\n");

        System.out.print("ELEMENTOS EN POST-ORDER: [");
        postOrder(arbol); // iii)
        System.out.print("]\n");
    }

    private static void preOrder(TDAABB a) {
        if (!a.ArbolVacio()) {
            System.out.print(a.Raiz()+", ");
            preOrder(a.HijoIzq());
            preOrder(a.HijoDer());
        }
    }

    private static void inOrder(TDAABB a) {
        if (!a.ArbolVacio()) {
            inOrder(a.HijoIzq());
            System.out.print(a.Raiz()+", ");
            inOrder(a.HijoDer());
        }
    }

    private static void postOrder(TDAABB a) {
        if (!a.ArbolVacio()) {
            postOrder(a.HijoIzq());
            postOrder(a.HijoDer());
            System.out.print(a.Raiz()+", ");
        }
    }

    public static ConjuntoTDA elementosMayoresQueK(TDAABB arbol, int k){
        ConjuntoTDA elementos = new ConjuntoA();
        elementos.inicializarConjunto();
        elementosMayoresQueK(arbol, k, elementos);
        return elementos;
    }

    private static void elementosMayoresQueK(TDAABB arbol, int k, ConjuntoTDA elementos){
        if (arbol.ArbolVacio()){
            return;
        } else if (arbol.Raiz() > k){
            elementos.agregar(arbol.Raiz());
        } 
        elementosMayoresQueK(arbol.HijoIzq(), k, elementos);
        elementosMayoresQueK(arbol.HijoDer(), k, elementos);
        
    }
    
    public static int anterior(TDAABB arbol, int v){
        int anterior = -1;
        return anterior(arbol, v, anterior);
    }

    private static int anterior(TDAABB arbol, int v, int anterior){
        if(arbol.ArbolVacio()){
            return anterior;
        } else if (arbol.Raiz() >= v){
            return anterior(arbol.HijoIzq(), v, anterior);
        } else {
            anterior = arbol.Raiz();
            return anterior(arbol.HijoDer(), v, anterior);
        }
    }

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        TDAABB arbol = new ABB();
        arbol.InicializarArbol();

        int cantidad = random.nextInt(40);
        for(int i = 0; i < cantidad; i++){
            arbol.AgregarElem(random.nextInt(100));
        }

        representarArbol(arbol);

        if (pertenece(arbol, 3)){ // A)
            System.out.println("EL ELEMENTO "+3+" PERTENECE AL ARBOL");
        } else {
            System.out.println("EL ELEMENTO "+3+" NO PERTENECE AL ARBOL");
        }

        if (esHoja(arbol, 3)){ // B)
            System.out.println("EL ELEMENTO "+3+" ES HOJA DEL ARBOL");
        } else {
            System.out.println("EL ELEMENTO "+3+" NO ES HOJA DEL ARBOL");
        }

        System.out.print("Ingresar valor para calcular profundidad: ");
        int valor = scanner.nextInt();

        System.out.println("PROFUNDIDAD DEL ELEMENTO "+valor+": "+calcularProfundidad(arbol, valor)); // C)

        int menor = menorElemento(arbol); // D)
        System.out.println("EL MENOR ELEMENTO DEL ARBOL ES: "+menor);

        int cant = cantidadElementos(arbol); // E)
        System.out.println("CANTIDAD DE ELEMENTOS: "+cant);

        int total = sumarElementos(arbol); // F)
        System.out.println("SUMATORIA DE ELEMENTOS: "+total);

        int hojas = cantidadHojas(arbol); // G)
        System.out.println("CANTIDAD DE HOJAS: "+hojas);

        int altura = calcularAltura(arbol); // H)
        System.out.println("ALTURA DEL ARBOL: "+altura);

        
        TDAABB arbol2 = new ABB();
        arbol2.InicializarArbol();

        cantidad = random.nextInt(40);
        for(int i = 0; i < cantidad; i++){
            arbol2.AgregarElem(random.nextInt(100));
        }

        representarArbol(arbol2);

        if(tienenMismaForma(arbol, arbol2)){ // I) 
            System.out.println("LOS DOS ARBOLES TIENEN LA MISMA FORMA");
        } else {
            System.out.println("LOS DOS ARBOLES TIENEN FORMAS DISTINTAS");
        }

        if(sonIguales(arbol, arbol2)){ // J) 
            System.out.println("LOS DOS ARBOLES SON IGUALES");
        } else {
            System.out.println("LOS DOS ARBOLES NO SON IGUALES");
        }

        System.out.print("Ingresar nivel para calcular cantidad de elementos: ");
        int nivel = scanner.nextInt();

        System.out.println("CANTIDAD DE ELEMENTOS EN EL NIVEL "+nivel+": "+cantidadElementosEnNivel(arbol, nivel)); // K)

        imprimirElementos(arbol); // L)

        ConjuntoTDA elementosMayores = elementosMayoresQueK(arbol, 20); // M)
        System.out.print("ELEMENTOS MAYORES A 20: ");
        elementosMayores.imprimirConjunto();

        System.out.print("Ingresar elemento para calcular su valor anterior en el arbol: ");
        valor = scanner.nextInt();

        System.out.println("VALOR ABSOLUTO ANTERIOR AL NUMERO "+valor+": "+anterior(arbol, valor)); // N)

        scanner.close();
    }

    public static void representarArbol(TDAABB arbol) {
        if (arbol.ArbolVacio()) {
            System.out.println("El árbol está vacío.");
            return;
        }
        representarArbolRec(arbol, 0, "R");
    }

    private static void representarArbolRec(TDAABB arbol, int nivel, String indicador) {
        if (arbol.ArbolVacio()) {
            return;
        }

        representarArbolRec(arbol.HijoDer(), nivel + 1, "/--");

        for (int i = 0; i < nivel; i++) {
            System.out.print("        ");
        }
        System.out.println(indicador + " " + arbol.Raiz());

        representarArbolRec(arbol.HijoIzq(), nivel + 1, "\\--");
    }
}
