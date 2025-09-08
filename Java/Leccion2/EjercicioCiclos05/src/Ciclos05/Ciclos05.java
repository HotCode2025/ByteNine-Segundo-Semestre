/*Clase 3: Tema: Clases y Objetos POO parte 1 Solución(27-08)
 Punto:3.3 Ejercicio con Ciclos 5 y clase Scanner y JOptionPane*/
 /*Ejercicio 5: Realiza un juego para adivinar un numero.
Para elllo generar un numero aleaatorio entre 0 y 100 y
luego ir pidiendo numeros indicando "es mayor" o "es menor" 
segun sea mayor o menor respecto a N.
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos */
package Ciclos05;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos05 {

    public static void main(String[] args) {
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        int numeroAleatorio;
        int numeroDigitado;
        int intentos = 0;

        // Generar un número aleatorio entre 0 y 100 
        numeroAleatorio = (int) (Math.random() * 101);

        System.out.println("JUEGO: Adivina el numero oculto entre 0 y 100");

        do {
            if (intentos == 0) {
                System.out.print("Digite un número: ");
            } else {
                System.out.print("Digite otro número: ");
            }

            numeroDigitado = entrada.nextInt();
            intentos++;

            if (numeroDigitado > numeroAleatorio) {
                System.out.println("Pista: El número es MENOR al ingresado");
            } else if (numeroDigitado < numeroAleatorio) {
                System.out.println("Pista: El número es MAYOR al ingresado");
            } else {
                System.out.println("¡Felicidades!, el numero correcto era: " + numeroAleatorio + "");
            }
        } while (numeroDigitado != numeroAleatorio);

        System.out.println("Haz digitado:" + intentos + " numeros ,hasta adivinar el correcto.");*/

        //Clase JoPtion
          int numeroAleatorio;
        int numeroDigitado;
        int intentos = 0;
        
        // Generar un número aleatorio entre 0 y 100
        numeroAleatorio = (int) (Math.random() * 101);
        
        JOptionPane.showMessageDialog(null, "¡Adivina el número entre 0 y 100!");
        
        do {
            // Se usa JOptionPane.showInputDialog para pedir el número.
            // Este método devuelve un String.
            String input = JOptionPane.showInputDialog("Digite un número: ");
            
            // 
            numeroDigitado = Integer.parseInt(input);
            intentos++;
            
            if (numeroDigitado > numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "Pista: El número es MENOR al ingresado.");
            } else if (numeroDigitado < numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "Pista: El número es MAYOR al ingresado.");
            }
        } while (numeroDigitado != numeroAleatorio);
        
        JOptionPane.showMessageDialog(null, "¡Felicidades!, el numero correcto era: " + numeroAleatorio + ".\n"
                + "Haz digitado: " + intentos + " numeros hasta adivinar.");

    }

}
