/*Ejercicio 7:Pedir numeros hasta que se introduzca uno negativo
 *y calcular la media
  Utilizando clase scaner y JOption*/
package Clase4;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class EjercicioCiclos7 {

    public static void main(String[] args) {
        int numero, contador = 0, suma = 0;
        float media;
        boolean continuar = true;

        //  para poder cerrar salida de la consola al final
        Scanner entrada = new Scanner(System.in);

        //Mostrar  el mensaje de lo que debe hacer  en la consola
        System.out.println("Digite numeros para calcular su media.\nPara finalizar, digite un numero negativo.");

        do {

            // Pedir al usuario que digite un numero usando JOptionPane
            String input = JOptionPane.showInputDialog(null, "Digite un numero:");

            // Convierte la entrada de texto a un numero entero.
            numero = Integer.parseInt(input);

            // Si es 0 o positivo, lo agregamos a la suma y al contador
            if (numero >= 0) {
                suma += numero;
                contador++;
            } else {
                // Si es negativo, se detiene el ciclo
                continuar = false;
            }

        } while (continuar);

        // Calculamos la media
        if (contador > 0) {
            media = (float) suma / contador;
            JOptionPane.showMessageDialog(null, "La media de los numeros digitados es: " + media);
        } else {
            // Sino se digita ningun numero valido
            JOptionPane.showMessageDialog(null, "No se digitaron numeros validos para calcular la media");
        }

        // Se cierra el scanner
        entrada.close();
        //Mostramos salida por consola
        System.out.println("Programa finalizado.");
    }
}
