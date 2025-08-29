package Clase2;
/*Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un número negativo*/

import java.util.Scanner;

public class Ejercicio1Ciclo {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese un número (negativo para salir): ");
        int numero = entrada.nextInt();
        
        while (numero >= 0) {
            int cuadrado = numero*numero;
            System.out.println("El cuadrado de " + numero + " es: " + cuadrado);
            System.out.print("Ingrese otro número (negativo para salir): ");
            numero = entrada.nextInt();
        }
    entrada.close();
    System.out.println("El programa finalizo");
    }

}
