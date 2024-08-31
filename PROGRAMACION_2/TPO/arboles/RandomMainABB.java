package arboles;

import java.util.Random;
import java.util.Scanner;

public class RandomMainABB {
        public static int calcularAltura(TDAABB t) {
        if (t.ArbolVacio()) {
            return 0;
        }
        int alturaIzq = calcularAltura(t.HijoIzq());
        int alturaDer = calcularAltura(t.HijoDer());
        return Math.max(alturaIzq, alturaDer) + 1;
    }

    public static void representarArbol(TDAABB arbol) {
        if (arbol == null || arbol.ArbolVacio()) {
            System.out.println("El árbol está vacío.");
            return;
        }
        representarArbolRec(arbol, 0, "R");
    }

    private static void representarArbolRec(TDAABB arbol, int nivel, String indicador) {
        if (arbol == null || arbol.ArbolVacio()) {
            return;
        }

        representarArbolRec(arbol.HijoDer(), nivel + 1, "/--");

        for (int i = 0; i < nivel; i++) {
            System.out.print("        ");
        }
        System.out.println(indicador + " " + arbol.Raiz());

        representarArbolRec(arbol.HijoIzq(), nivel + 1, "\\--");
    }


    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        TDAABB arbol = new ABB();

        int cantidad = random.nextInt(40);
        for(int i = 0; i < cantidad; i++){
            arbol.AgregarElem(random.nextInt(100));
        }
        
        System.out.println("COMO INTERPRETAR REPRESENTACION: \nR --> RAIZ \n/ --> HIJO DERECHO \n\\ --> HIJO IZQUIERDO \n");
        representarArbol(arbol);
        
        int altura = calcularAltura(arbol);
        System.out.println("\nALTURA DEL ARBOL: "+altura);      


        System.out.print("\nIngresar valor para calcular profundidad: ");
        int valor = scanner.nextInt();

        System.out.printf("PROFUNDIDAD DEL ELEMENTO "+valor+": "+arbol.calcularProfundidad(arbol, valor));
        
        scanner.close();
    }
}
