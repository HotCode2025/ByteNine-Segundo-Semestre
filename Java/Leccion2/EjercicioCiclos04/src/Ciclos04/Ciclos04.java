/*Clase 3:Clases y Objetos POO parte 1 Solución(27-08)
 Punto:3.2 Ejercicio con Ciclos 4 y clase Scanner y JOptionPane*/
 /*Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
  *mostrar uantos numeros se han introducido.
  Lo hacemos primero con la clase Scanner y luego con la clase
  JOption Pane
  */
package Ciclos04;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos04 {

    public static void main(String[] args) {
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        int numero, contador = 0; // Se inicializa el contador en 0

        System.out.println("Digite un numero(Finaliza si introduce 0): ");
        numero = entrada.nextInt();

        // Se usa  while hasta que sea >= a 0
        while (numero >= 0) {
            contador++; // incrementa el contador por cada numero introducido
            System.out.println("El numero " + numero + " es Positivo");
            System.out.println("Digite otro numero: ");
            numero = entrada.nextInt(); //pide otro número dentro del ciclo
        }

        System.out.println("El Programa ha finalizado porque se introdujo un numero negativo");
        System.out.println("Se introdujeron " + contador + " numeros en total (sin contar el negativo).");*/

        //Clase JoptionPane
        int numero, contador = 0; // Se inicializa el contador en 0
        String input = JOptionPane.showInputDialog("Digite un numero: ");// Usar una ventana de diálogo para obtener el primer número
        numero = Integer.parseInt(input);

        // El ciclo while se ejecuta mientras el numero no sea negativo
        while (numero >= 0) {
            contador++; // Se incrementa el contador por cada número válido
            JOptionPane.showMessageDialog(null, "El numero " + numero + " es Positivo.");
            
            // Pedir otro número dentro del ciclo
            input = JOptionPane.showInputDialog("Digite otro numero: ");
            numero = Integer.parseInt(input);
        }

        JOptionPane.showMessageDialog(null, "El Programa ha finalizado porque se introdujo un numero negativo.");
        JOptionPane.showMessageDialog(null, "Se introdujeron " + contador + " numeros en total (sin contar el negativo).");

    }

}
