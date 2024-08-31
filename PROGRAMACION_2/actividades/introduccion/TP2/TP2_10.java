package actividades.introduccion.TP2;

public class TP2_10 {
    public static void main(String[] args) {
        System.out.println("Escribir la funcion obtenerMesEnTexto, la cual debe devolver una cadena de caracteres que representa un mes expresado en letras segun un numero entero entre 1 y 12, recibido como parametro. \nSi el parametro no es valido, devolver una cadena vacia. \nEJEMPLO: Se invoca obtenerMesEnTexto(4), devuelve 'Abril'.");
    
        int numero = 4;

        System.out.println("El mes "+numero+" es "+obtenerMesEnTexto(numero));
    }

    static String obtenerMesEnTexto(int x){
        String mes = "";
        switch (x) {
            case 1:
                mes = "Enero";
                break;
            case 2:
                mes = "Febrero";
                break;
            case 3:
                mes = "Marzo";
                break;
            case 4:
                mes = "Abril";
                break;
            case 5:
                mes = "Mayo";
                break;
            case 6:
                mes = "Junio";
                break;
            case 7:
                mes = "Julio";
                break;
            case 8:
                mes = "Agosto";
                break;
            case 9:
                mes = "Septiembre";
                break;
            case 10:
                mes = "Octubre";
                break;
            case 11:
                mes = "Noviembre";
                break;
            case 12:
                mes = "Diciembre";
                break;
            default:
                break;
        }
        return mes;
    }
}
