package caja;

import java.util.Scanner;

/**
 *
 * @author garod
 */
public class PruebaCajaScanner {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("=== Cálculo del Volumen de la caja ===");

        // solicitamos al usuario los valores
        System.out.println("Ingrese el ancho: ");
        double ancho = entrada.nextDouble();

        System.out.println("Ingrese el alto: ");
        double alto = entrada.nextDouble();

        System.out.println("Ingrese la profundidad: ");
        double profundidad = entrada.nextDouble();

        // Creamos el objeto con valores ingresados
        Caja caja1 = new Caja(ancho, alto, profundidad);

        // Calculamos el volumen
        double volumen = caja1.calcularVolumen();

        System.out.println("El volumen de la caja es : " + volumen);
    }

}
