/*Clase 3: Tema: Clases y Objetos POO parte 1 Solución(27-08)
 Punto:3.3 Ejercicio con Ciclos 5 y clase Scanner y JOptionPane*/
 /*Ejercicio 5: Realiza un juego para adivinar un numero.
Para elllo generar un numero aleaatorio entre 0 y 100 y
luego ir pidiendo numeros indicando "es mayor" o "es menor" 
segun sea mayor o menor respecto a N.
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos */
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {

    public static void main(String[] args) {
        int numeroAleatorio = (int) (Math.random() * 101);
        int numeroDigitado;
        int intentos = 0;

        JOptionPane.showMessageDialog(null, "Adivina el numero entre 0 y 100");

        do {

            String input = JOptionPane.showInputDialog("Digite un numero: ");

            numeroDigitado = Integer.parseInt(input);
            intentos++;

            if (numeroDigitado > numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "El numero oculto es MENOR.");
            } else if (numeroDigitado < numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "El numero oculto es MAYOR.");
            }

        } while (numeroDigitado != numeroAleatorio);

        JOptionPane.showMessageDialog(null, "Adivinaste el numero!");
        JOptionPane.showMessageDialog(null, "El numero era: " + numeroAleatorio + "\n"
                + "Lo adivinaste en " + intentos + " intentos.");
    }

}
