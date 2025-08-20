package Clase1Java;

public class Labels {

    public static void main(String[] args) {
        // Etiquetas Labels

        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break;
            }
        }
        inicio:
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 != 0) {
                continue inicio; // Vamos a la siguiente iteración                
            }
            System.out.println("contando = " + contando);
        }
    }
}
