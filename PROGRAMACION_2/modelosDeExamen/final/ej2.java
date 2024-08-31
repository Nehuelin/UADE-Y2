import tdas.*;
import dinamicas.diccionariosMultiples.DiccionarioMultipleLD;
import java.util.Random;

public class ej2{
public static DiccionarioMultipleTDA obtenerClavesComunes(DiccionarioMultipleTDA D1, DiccionarioMultipleTDA D2){
    DiccionarioMultipleTDA D3 = new DiccionarioMultipleLD();
    D3.inicializarDiccionario();
    ConjuntoTDA claves1 = D1.claves();
    while(!claves1.conjuntoVacio()){
        int cl1 = claves1.elegir();
        claves1.sacar(cl1);
        ConjuntoTDA claves2 = D2.claves();
        while(!claves2.conjuntoVacio()){
            int cl2 = claves2.elegir();
            claves2.sacar(cl2);
            if(cl1 == cl2){
                ConjuntoTDA valores1 = D1.recuperar(cl1);
                ConjuntoTDA valores2 = D2.recuperar(cl2);
                while(!valores1.conjuntoVacio()){
                    int valor = valores1.elegir();
                    valores1.sacar(valor);
                    D3.agregar(cl1, valor);    
                }
                while(!valores2.conjuntoVacio()){
                    int valor = valores2.elegir();
                    valores2.sacar(valor);
                    D3.agregar(cl1, valor);    
                }
            }
        }
    }

    return D3;
}
    public static void main(String[] args) {
        Random random = new Random();

        DiccionarioMultipleTDA dicA = new DiccionarioMultipleLD();
        dicA.inicializarDiccionario();
        int cantidadClaves = random.nextInt(20);
        for(int i = 0; i < cantidadClaves; i++){
            dicA.agregar(random.nextInt(10), random.nextInt(10));
        }

        System.out.println("DICCIONARIO 1: ");
        dicA.imprimirDiccionario();

        DiccionarioMultipleTDA dicB = new DiccionarioMultipleLD();
        dicB.inicializarDiccionario();
        cantidadClaves = random.nextInt(20);
        for(int i = 0; i < cantidadClaves; i++){
            dicB.agregar(random.nextInt(10), random.nextInt(10));
        }

        System.out.println("\nDICCIONARIO 2: ");
        dicB.imprimirDiccionario();

        DiccionarioMultipleTDA dicC = obtenerClavesComunes(dicA, dicB);
        System.out.println("\nDICCIONARIO 3: ");
        dicC.imprimirDiccionario();
    }
}

