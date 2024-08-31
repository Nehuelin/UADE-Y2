import tdas.TDAABB;
import arboles.ABB;
import java.util.Random;
import java.util.Scanner;

public class ej3 {
    public static int obtenerHijoIzquierdo(TDAABB arbol, int x){
        if(arbol.Raiz() == x && !arbol.HijoIzq().ArbolVacio()){
            return arbol.HijoIzq().Raiz();
        } else if (arbol.Raiz() == x && arbol.HijoIzq().ArbolVacio()){
            return -1;
        } else if (arbol.Raiz() > x){
            return obtenerHijoIzquierdo(arbol.HijoIzq(), x);
        } else {
            return obtenerHijoIzquierdo(arbol.HijoDer(), x);
        }
    }

    public static int obtenerPadre(TDAABB arbol, int x){
        if (arbol.ArbolVacio()) {
            return -1;
        }
        if (arbol.Raiz() == x) {
            return -1;
        }
        if (!arbol.HijoIzq().ArbolVacio() && arbol.HijoIzq().Raiz() == x) {
            return arbol.Raiz();
        }
        if (!arbol.HijoDer().ArbolVacio() && arbol.HijoDer().Raiz() == x) {
            return arbol.Raiz();
        }
        if (arbol.Raiz() > x) {
            return obtenerPadre(arbol.HijoIzq(), x);
        } else {
            return obtenerPadre(arbol.HijoDer(), x);
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

        int x = scanner.nextInt();
        int hijoIzquierdo = obtenerHijoIzquierdo(arbol, x);
        System.out.println("HIJO IZQUIERDO DE "+x+": "+hijoIzquierdo);
        
        x = scanner.nextInt();
        int padre = obtenerPadre(arbol, x);
        System.out.println("NODO PADRE DE "+x+": "+padre);

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
