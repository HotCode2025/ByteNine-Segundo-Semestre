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

public class Ciclos05 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numeroAleatorio = (int) (Math.random() * 101);
        int numeroDigitado;
        int intentos = 0;

        System.out.println("Adivina el numero entre 0 y 100.");

        do {
            System.out.println("Digite un numero: ");
            numeroDigitado = entrada.nextInt();
            intentos++;

            if (numeroDigitado > numeroAleatorio) {
                System.out.println("El numero oculto es MENOR.");
            } else if (numeroDigitado < numeroAleatorio) {
                System.out.println("El numero oculto es MAYOR.");
            }
        } while (numeroDigitado != numeroAleatorio);

        System.out.println("Felicitaciones!!Adivinaste el numero");
        System.out.println("El numero era: " + numeroAleatorio);
        System.out.println("Lo lograste en " + intentos + " intentos.");
    }
}
