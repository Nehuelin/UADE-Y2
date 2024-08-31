package actividades.trabajosPracticos.TP3;
import tdas.*;
import estaticas.conjuntos.ConjuntoA;
import estaticas.diccionariosMultiples.DiccionarioMultipleA;
import java.util.Random;

/*Dados dos DiccionarioMultipleTDA D1 y D2, generar un DiccionarioMultipleTDA que
contenga:
a) las claves presentes en D1 y D2, con todos los elementos asociados a cada clave.
b) las claves presentes en D1 y D2, con todos los elementos comunes a las claves
coincidentes en ambos.
c) las claves comunes de D1 y D2, con todos los elementos asociados a cada clave.
d) las claves comunes de D1 y D2, con todos los elementos comunes a las claves
coincidentes en ambos */

public class TP3_5_1_diciconariosMultiples {
    public static DiccionarioMultipleA generarDiccionario1(DiccionarioMultipleTDA D1, DiccionarioMultipleTDA D2){
        DiccionarioMultipleA D3 = new DiccionarioMultipleA();
        D3.inicializarDiccionario();

        ConjuntoTDA claves1 = D1.claves();
        ConjuntoTDA claves2 = D2.claves();

        while(!claves1.conjuntoVacio()){
            int clave = claves1.elegir();
            ConjuntoTDA valores = D1.recuperar(clave);
            while(!valores.conjuntoVacio()){
                int valor = valores.elegir();
                D3.agregar(clave, valor);
                valores.sacar(valor);
            }
            claves1.sacar(clave);
        }

        while(!claves2.conjuntoVacio()){
            int clave = claves2.elegir();
            ConjuntoTDA valores = D2.recuperar(clave);
            while(!valores.conjuntoVacio()){
                int valor = valores.elegir();
                D3.agregar(clave, valor);
                valores.sacar(valor);
            }
            claves2.sacar(clave);
        }

        return D3;
    }

    public static DiccionarioMultipleTDA generarDiccionario2(DiccionarioMultipleTDA D1, DiccionarioMultipleTDA D2){
        DiccionarioMultipleTDA D3 = new DiccionarioMultipleA();
        D3.inicializarDiccionario();

        ConjuntoTDA todasLasClaves = union(D1.claves(), D2.claves());

        ConjuntoTDA claves1 = D1.claves();
        ConjuntoTDA claves2 = D2.claves();

        while (!todasLasClaves.conjuntoVacio()) {
            int clave = todasLasClaves.elegir();
            todasLasClaves.sacar(clave);
            
            ConjuntoTDA valoresD1 = claves1.pertenece(clave) ? D1.recuperar(clave) : new ConjuntoA();
            ConjuntoTDA valoresD2 = claves2.pertenece(clave) ? D2.recuperar(clave) : new ConjuntoA();
            
            ConjuntoTDA valoresResultado = new ConjuntoA();
            valoresResultado.inicializarConjunto();
            
            if (claves1.pertenece(clave) && claves2.pertenece(clave)) {
                while (!valoresD1.conjuntoVacio()) {
                    int valor = valoresD1.elegir();
                    valoresD1.sacar(valor);
                    
                    if (valoresD2.pertenece(valor)) {
                        valoresResultado.agregar(valor);
                    }
                }
            } else if (claves1.pertenece(clave)) {
                while (!valoresD1.conjuntoVacio()) {
                    int valor = valoresD1.elegir();
                    valoresD1.sacar(valor);
                    valoresResultado.agregar(valor);
                }
            } else if (claves2.pertenece(clave)) {
                while (!valoresD2.conjuntoVacio()) {
                    int valor = valoresD2.elegir();
                    valoresD2.sacar(valor);
                    valoresResultado.agregar(valor);
                }
            }
            
            while (!valoresResultado.conjuntoVacio()) {
                int valor = valoresResultado.elegir();
                valoresResultado.sacar(valor);
                D3.agregar(clave, valor);
            }
        }
        
        return D3;
    }

    public static DiccionarioMultipleA generarDiccionario3(DiccionarioMultipleTDA D1, DiccionarioMultipleTDA D2){
        DiccionarioMultipleA D3 = new DiccionarioMultipleA();
        D3.inicializarDiccionario();

        ConjuntoTDA clavesComunes = intersección(D1.claves(), D2.claves());

        while(!clavesComunes.conjuntoVacio()){
            int clave = clavesComunes.elegir();
            ConjuntoTDA valores = D1.recuperar(clave);
            while(!valores.conjuntoVacio()){
                int valor = valores.elegir();
                D3.agregar(clave, valor);
                valores.sacar(valor);
            }
            clavesComunes.sacar(clave);
        }

        clavesComunes = intersección(D1.claves(), D2.claves());

        while(!clavesComunes.conjuntoVacio()){
            int clave = clavesComunes.elegir();
            ConjuntoTDA valores = D2.recuperar(clave);
            while(!valores.conjuntoVacio()){
                int valor = valores.elegir();
                D3.agregar(clave, valor);
                valores.sacar(valor);
            }
            clavesComunes.sacar(clave);
        }

        return D3;
    }

    public static DiccionarioMultipleTDA generarDiccionario4(DiccionarioMultipleTDA D1, DiccionarioMultipleTDA D2) {
        DiccionarioMultipleTDA D3 = new DiccionarioMultipleA();
        D3.inicializarDiccionario(); 
        
        ConjuntoTDA clavesD1 = D1.claves(); 
        ConjuntoTDA clavesD2 = D2.claves(); 
        
        while (!clavesD1.conjuntoVacio()) {
            int clave = clavesD1.elegir(); 
            clavesD1.sacar(clave); 
            
            if (clavesD2.pertenece(clave)) { 
                ConjuntoTDA valoresD1 = D1.recuperar(clave); 
                ConjuntoTDA valoresD2 = D2.recuperar(clave); 
                
                
                while (!valoresD1.conjuntoVacio()) {
                    int valor = valoresD1.elegir(); 
                    valoresD1.sacar(valor); 
                    
                    if (valoresD2.pertenece(valor)) { 
                        D3.agregar(clave, valor); 
                    }
                }
            }
        }
        
        return D3; 
    }
    
    private static ConjuntoTDA union(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
        ConjuntoTDA conjunto3 = new ConjuntoA();
        conjunto3.inicializarConjunto();

        while(!conjunto1.conjuntoVacio()){
            int elemento = conjunto1.elegir();
            conjunto3.agregar(elemento);
            conjunto1.sacar(elemento);
        }
        while(!conjunto2.conjuntoVacio()){
            int elemento = conjunto2.elegir();
            conjunto3.agregar(elemento);
            conjunto2.sacar(elemento);
        }

        return conjunto3;
    }

    private static ConjuntoTDA intersección(ConjuntoTDA conjunto1, ConjuntoTDA conjunto2){
        ConjuntoTDA conjunto3 = new ConjuntoA();
        conjunto3.inicializarConjunto();

        while(!conjunto1.conjuntoVacio()){
            int elemento = conjunto1.elegir();
            if (conjunto2.pertenece(elemento)){
                conjunto3.agregar(elemento);
                conjunto2.sacar(elemento);
            }
            conjunto1.sacar(elemento);
        }
        while(!conjunto2.conjuntoVacio()){
            conjunto2.sacar(conjunto2.elegir());
        }

        return conjunto3;
    }

    public static void main(String[] args) {
        Random random = new Random();

        DiccionarioMultipleTDA dicA = new DiccionarioMultipleA();
        dicA.inicializarDiccionario();
        int cantidadClaves = random.nextInt(20);
        for(int i = 0; i < cantidadClaves; i++){
            dicA.agregar(random.nextInt(10), random.nextInt(10));
        }

        System.out.println("DICCIONARIO 1: ");
        dicA.imprimirDiccionario();

        DiccionarioMultipleTDA dicB = new DiccionarioMultipleA();
        dicB.inicializarDiccionario();
        cantidadClaves = random.nextInt(20);
        for(int i = 0; i < cantidadClaves; i++){
            dicB.agregar(random.nextInt(10), random.nextInt(10));
        }

        System.out.println("\nDICCIONARIO 2: ");
        dicB.imprimirDiccionario();

        DiccionarioMultipleTDA dicC = generarDiccionario1(dicA, dicB); // A)
        
        System.out.println("\nDICCIONARIO 3: ");
        dicC.imprimirDiccionario();

        DiccionarioMultipleTDA dicD = generarDiccionario2(dicA, dicB); // B)
        
        System.out.println("\nDICCIONARIO 4: ");
        dicD.imprimirDiccionario();

        DiccionarioMultipleTDA dicE = generarDiccionario3(dicA, dicB); // C)
        
        System.out.println("\nDICCIONARIO 5: ");
        dicE.imprimirDiccionario();

        DiccionarioMultipleTDA dicF = generarDiccionario4(dicA, dicB); // D)
        
        System.out.println("\nDICCIONARIO 6: ");
        dicF.imprimirDiccionario();
    }
}

