package actividades.introduccion.TP2;

public class TP2_7 {
    public static void main(String[] args) {
        System.out.println("Escribir el procedimiento imprimirSimbolo, el cual debe imprimir por consola n veces un caracter en la misma linea. \nTanto n como el caracter se reciben como parametro.\nEJEMPLO: Se invoca imprimirSimbolo(5,'#'), imprime #####");
    
        int iteraciones = 5;
        char simbolo = '#';

        imprimirSimbolo(iteraciones, simbolo);
    }

    static void imprimirSimbolo(int n, char caracter){
        for(int i = 1; i <= n; i++){
            System.out.print(caracter);
        }
    }
}
