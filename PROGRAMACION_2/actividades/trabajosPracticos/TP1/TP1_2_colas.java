package actividades.trabajosPracticos.TP1;
import tdas.ColaTDA;
import tdas.PilaTDA;
import estaticas.colas.ColaPI;
import estaticas.pilas.PilaTI;

/*4) A partir del TDA Cola definido, escribir distintos métodos que permitan
a) Pasar una Cola a otra
b) Invertir el contenido de una Cola (pueden usarse Pilas auxiliares)
c) Invertir el contenido de una Cola (NO pueden usarse Pilas auxiliares)
d) Determinar si el final de la Cola C1 coincide o no con la Cola C2.
e) Determinar si una Cola es capicúa o no. Para ser capicúa debe cumplir
que el primer elemento es igual al último, el segundo igual al penúltimo, etc.
f) Determinar si la Cola C1 es la inversa de la Cola C2. Dos Colas serán
inversas, si tienen los mismos elementos pero en orden inverso. */

public class TP1_2_colas {
    public static void pasarCola(ColaTDA colaOrigen, ColaTDA colaDestino){
        while(!colaOrigen.colaVacia()){
            colaDestino.acolar(colaOrigen.primero());
            colaOrigen.desacolar();
        }
    }

    public static void invertirCola1(ColaTDA cola){
        PilaTDA pilaAux = new PilaTI();
        pilaAux.inicializarPila();
        while(!cola.colaVacia()){
            pilaAux.apilar(cola.primero());
            cola.desacolar();
        }
        while(!pilaAux.pilaVacia()){
            cola.acolar(pilaAux.tope());
            pilaAux.desapilar();
        }
    }

    public static void invertirCola2(ColaTDA cola) {
        if(!cola.colaVacia()) {
			int x = cola.primero();
			cola.desacolar();
			invertirCola2(cola);
			cola.acolar(x);
		}
	}

    public static boolean coincideFinal(ColaTDA colaA, ColaTDA colaB){
        invertirCola1(colaA);
        invertirCola1(colaB);
        boolean iguales = colaA.primero() == colaB.primero(); 
        invertirCola1(colaA);
        invertirCola1(colaB);
        return iguales;
    }

    public static boolean esCapicua(ColaTDA cola){
        ColaTDA colaCopia = new ColaPI();
        ColaTDA colaAux = new ColaPI();
        colaCopia.inicializarCola();
        colaAux.inicializarCola();
        pasarCola(cola, colaAux);
        while(!colaAux.colaVacia()){
            cola.acolar(colaAux.primero());
            colaCopia.acolar(colaAux.primero());
            colaAux.desacolar();
        }
        invertirCola1(colaCopia);
        boolean capicua = true;
        while(!colaCopia.colaVacia()){
            if (colaCopia.primero() == cola.primero()){
                colaAux.acolar(cola.primero());
                cola.desacolar();
                colaCopia.desacolar();
            } else {
                capicua = false;
                break;
            }
        }
        pasarCola(colaAux, cola);
        return capicua;
    }

    public static boolean esInverso(ColaTDA colaA, ColaTDA colaB){
        invertirCola1(colaB);
        ColaTDA colaAux1 = new ColaPI();
        ColaTDA colaAux2 = new ColaPI();
        colaAux1.inicializarCola();
        colaAux2.inicializarCola();
        boolean inverso = true;
        while(!colaA.colaVacia()){
            if(colaA.primero() == colaB.primero()){
                colaAux1.acolar(colaA.primero());
                colaAux2.acolar(colaB.primero());
                colaA.desacolar();
                colaB.desacolar();
            }else{
                inverso = false;
                break;
            }
        }
        pasarCola(colaAux1, colaA);
        pasarCola(colaAux2, colaB);
        return inverso;
    }

    public static void main(String[] args) {
        ColaTDA cola1 = new ColaPI();
        ColaTDA cola2 = new ColaPI();
        cola1.inicializarCola();
        cola2.inicializarCola();
        cola1.acolar(1);
        cola1.acolar(2);
        cola1.acolar(3);
        cola1.acolar(4);
        cola1.acolar(5);
        cola1.acolar(6);
        pasarCola(cola1, cola2); // A)

        System.out.println();
        
        invertirCola1(cola2); // B)

        System.out.println();

        invertirCola2(cola2); // C)

        System.out.println();

        cola1.acolar(1);
        cola1.acolar(2);
        cola1.acolar(3);
        cola1.acolar(4);
        cola1.acolar(5);
        cola1.acolar(6);

        boolean coinciden = coincideFinal(cola1, cola2); // D)
        if(coinciden){
            System.out.println("LOS ULTIMOS ELEMENTOS DE AMBAS COLAS COINCIDEN");
        }else{
            System.out.println("LOS ULTIMOS ELEMENTOS DE AMBAS COLAS NO COINCIDEN");
        }
            
        ColaTDA cola3 = new ColaPI();
        cola3.inicializarCola();
        cola3.acolar(1);
        cola3.acolar(2);
        cola3.acolar(3);
        cola3.acolar(3);
        cola3.acolar(2);
        cola3.acolar(1);
        
        boolean es_capicua = esCapicua(cola3); // E)
        if(es_capicua){
            System.out.println("LA COLA ES CAPICUA");
        }else{
            System.out.println("LA COLA NO ES CAPICUA");
        }

        ColaTDA cola4 = new ColaPI();
        cola4.inicializarCola();
        cola4.acolar(1);
        cola4.acolar(2);
        cola4.acolar(3);

        ColaTDA cola5 = new ColaPI();
        cola5.inicializarCola();
        cola5.acolar(3);
        cola5.acolar(2);
        cola5.acolar(1);

        boolean es_inversa = esInverso(cola4, cola5); // E)
        if(es_inversa){
            System.out.println("LA COLA ES INVERSA");
        }else{
            System.out.println("LA COLA NO ES INVERSA");
        }
    }
}
