package actividades.introduccion.TP2;

public class TP2_9 {
    public static void main(String[] args) {
        System.out.println("Escribir la funcion esVocal, la cual debe devolver true o false segun si un caracter recibido como parametro es vocal (contemplar mayusculas y minusculas). \nEJEMPLO: Se invoca esVocal('a', devuelve true)");

        char caracter = 'a';

        System.out.print("La letra "+caracter);

        if(esVocal(caracter)){
            System.out.print(" es vocal");
        } else {
            System.out.print(" NO es vocal");
        }
    }

    static boolean esVocal(char c){
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
