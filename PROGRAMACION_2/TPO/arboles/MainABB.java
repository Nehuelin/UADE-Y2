package arboles;

public class MainABB {
    public static int calcularAltura(TDAABB t) {
        if (t.ArbolVacio()) {
            return 0;
        }
        int alturaIzq = calcularAltura(t.HijoIzq());
        int alturaDer = calcularAltura(t.HijoDer());
        return Math.max(alturaIzq, alturaDer) + 1;
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


    public static void main(String[] args) {
        TDAABB arbol = new ABB();
        arbol.AgregarElem(16);
        arbol.AgregarElem(12);
        arbol.AgregarElem(14);
        arbol.AgregarElem(9);
        arbol.AgregarElem(5);
        arbol.AgregarElem(10);
        arbol.AgregarElem(1);
        arbol.AgregarElem(4);
        arbol.AgregarElem(8);
        arbol.AgregarElem(6);
        arbol.AgregarElem(99);
        
        
        System.out.println("COMO INTERPRETAR REPRESENTACION: \nR --> RAIZ \n/ --> HIJO DERECHO \n\\ --> HIJO IZQUIERDO \n");
        representarArbol(arbol);
        
        int altura = calcularAltura(arbol);
        System.out.println("\nALTURA DEL ARBOL: "+altura);      

        System.out.printf("PROFUNDIDAD DEL ELEMENTO 10: " +arbol.calcularProfundidad(arbol, 10));
    }
}

