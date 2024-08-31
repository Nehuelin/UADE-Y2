package estaticas.diccionariosMultiples;

import tdas.DiccionarioMultipleTDA;
import tdas.ConjuntoTDA;
import estaticas.conjuntos.ConjuntoA;

public class DiccionarioMultipleA implements DiccionarioMultipleTDA {
    class Elemento{
        int clave;
        int[] valores;
        int cantidadValores;
    }

    private Elemento[] elementos;
    private int cantidadClaves;

    public void inicializarDiccionario(){
        elementos = new Elemento[100];
        cantidadClaves = 0;
    }

    public void agregar(int clave, int valor){
        int posicionClave = clave2Indice(clave);
        if (posicionClave == -1){
            posicionClave = cantidadClaves;
            elementos[posicionClave] = new Elemento();
            elementos[posicionClave].clave = clave;
            elementos[posicionClave].cantidadValores = 0;
            elementos[posicionClave].valores = new int[100];
            cantidadClaves++;
        }
        Elemento e = elementos[posicionClave];
        int posicionValor = valor2Indice(e, valor);
        if (posicionValor == -1){
            e.valores[e.cantidadValores] = valor;
            e.cantidadValores++;
        }
    }

    public void eliminar(int clave){
        int posicionClave = clave2Indice(clave);
        if (posicionClave != -1) {
            elementos[posicionClave] = elementos[cantidadClaves - 1];
            cantidadClaves--;
        }
    }

    public void eliminarValor(int clave, int valor){
        int posicionClave = clave2Indice(clave);
        if (posicionClave != -1) {
            Elemento e = elementos[posicionClave];
            int posicionValor = valor2Indice(e, valor);
            if (posicionValor == -1){
                e.valores[posicionValor] = e.valores[e.cantidadValores - 1];
                e.cantidadValores--;
            }
            if (e.cantidadValores == 0){
                eliminar(clave);
            }    
        }
    }

    private int clave2Indice(int clave){
        int i = cantidadClaves - 1;
        while (i >= 0 && elementos[i].clave != clave){
            i--;
        }
        return i;
    }

    private int valor2Indice(Elemento e, int valor){
        int i = e.cantidadValores - 1;
        while (i >= 0 && e.valores[i] != valor){
            i--;
        }
        return i;
    }

    public ConjuntoTDA recuperar(int clave){
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();
        int posicionClave = clave2Indice(clave);
        if (posicionClave != -1) {
            Elemento e = elementos[posicionClave];
            for(int i = 0; i < e.cantidadValores; i++){
                c.agregar(e.valores[i]);
            }
        } 
        return c;
    }

    public ConjuntoTDA claves(){
        ConjuntoTDA c = new ConjuntoA();
        c.inicializarConjunto();
        for(int i = 0; i < cantidadClaves; i++){
            c.agregar(elementos[i].clave);
        }
        return c;
    }

    public void imprimirDiccionario(){
        ConjuntoTDA claves = this.claves();
        while(!claves.conjuntoVacio()){
            int clave = claves.elegir();
            ConjuntoTDA valores = this.recuperar(clave);
            System.out.print(clave +": ");
            valores.imprimirConjunto();
            claves.sacar(clave);
        }
    }
}
