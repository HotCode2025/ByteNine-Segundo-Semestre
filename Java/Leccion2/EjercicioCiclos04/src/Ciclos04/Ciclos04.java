/*Clase 3:Clases y Objetos POO parte 1 Solución(27-08)
 Punto:3.2 Ejercicio con Ciclos 4 y clase Scanner y JOptionPane*/
 /*Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
  *mostrar Cuantos numeros se han introducido.
  Lo hacemos primero con la clase Scanner y luego con la clase
  JOption Pane
 */
package Ciclos04;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos04 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int numero, contador = 0; // Se inicializa el contador en 0

        // El primer mensaje lo mostramos con JOption
        JOptionPane.showMessageDialog(null, "Digite numeros en la consola,finaliza si ingresa negativo");

        //El ingreso lo hacemos desde consola
        System.out.println("Digite un numero: ");
        numero = entrada.nextInt();

        // Con  while pedimos los numeros, hasta que digite 0
        while (numero >= 0) {
            contador++; // incrementamos el contador

            // Mostramos los resultados con JOption
            JOptionPane.showMessageDialog(null, "El numero " + numero + " es Positivo");

            System.out.println("Digite otro numero: ");
            numero = entrada.nextInt(); // Pide otro número en la consola dentro del ciclo
        }
        //Mensaje para finalizar el programa por consola(scanner)
        System.out.println("Programa  finalizado se digito un numero negativo");

        // El mensaje para contar los numerod digitado8 JOptionPane)
        JOptionPane.showMessageDialog(null, "Se introdujeron " + contador + " numeros en total (sin contar el negativo).");

    }

}
