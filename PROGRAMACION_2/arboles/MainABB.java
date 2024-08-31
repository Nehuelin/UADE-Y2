package arboles;
import tdas.TDAABB;
import tdas.ConjuntoTDA;
import dinamicas.conjuntos.ConjuntoLD;

public class MainABB {
    // RECORRIDOS EN ABB
    public void preOrder(TDAABB a) {
        if (!a.ArbolVacio()) {
            System.out.println(a.Raiz());
            preOrder(a.HijoIzq());
            preOrder(a.HijoDer());
        }
    }

    public void inOrder(TDAABB a) {
        if (!a.ArbolVacio()) {
            inOrder(a.HijoIzq());
            System.out.println(a.Raiz());
            inOrder(a.HijoDer());
        }
    }

    public void postOrder(TDAABB a) {
        if (!a.ArbolVacio()) {
            postOrder(a.HijoIzq());
            postOrder(a.HijoDer());
            System.out.println(a.Raiz());
        }
    }

    // EJEMPLOS EJERCICIOS 
    // Ejercicio 1: Contar la cantidad de nodos de un ABB
    public int contar(TDAABB a) {
        if (a.ArbolVacio()) {
            return 0;
        } else {
            return (1 + contar(a.HijoIzq()) + contar(a.HijoDer()));
        }
    }

    // Ejercicio 2: Dado un elemento y un ABB, calcular su profundidad en el arbol
    public int calcularProfundidad(TDAABB t, int x) {
        if (t.ArbolVacio()) {
            return 0;
        } else if (t.Raiz() == x) {
            return 0;
        } else if (t.Raiz() > x) {
            return (1 + this.calcularProfundidad(t.HijoIzq(), x));
        } else {
            return (1 + this.calcularProfundidad(t.HijoIzq(), x));
        }
    }

    // Ejercicio 3: Dado un elemento, determinar si está o no en un ABB
    public boolean existeElementoEnABB(TDAABB t, int x){
        if (t.ArbolVacio()) {
            return false;
        } else if (t.Raiz() == x){
            return true;
        } else if (t.Raiz() > x){
            return this.existeElementoEnABB(t.HijoIzq(), x);
        } else {
            return this.existeElementoEnABB(t.HijoDer(), x);
        }
    }

    // Ejercicio 4: Dado un arbol TDAABB a, devolver todos los nodos pares del mismo
    public ConjuntoTDA nodosPares(TDAABB a){
        ConjuntoTDA r = new ConjuntoLD();
        r.inicializarConjunto();
        if (!a.ArbolVacio()) {
            if (a.Raiz() % 2 == 0) {
                r.agregar(a.Raiz());
            } 
            ConjuntoTDA rI = nodosPares(a.HijoIzq());
            ConjuntoTDA rD = nodosPares(a.HijoDer());
            while (!rI.conjuntoVacio()){
                int x = rI.elegir();
                r.agregar(x);
                rI.sacar(x);
            }
            while (!rD.conjuntoVacio()){
                int x = rD.elegir();
                r.agregar(x);
                rD.sacar(x);
            }
        }
        return r;
    }
}
