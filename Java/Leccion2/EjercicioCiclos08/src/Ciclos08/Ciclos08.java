/*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.7Ejercicio Ciclos 08 con Scanner y JOptionPane*/
//Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N.
//Clase Scanner
package Ciclos08;

import java.util.Scanner;

public class Ciclos08 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese un numero N mayor a 0: ");
        int N = scanner.nextInt();

        if (N <= 0) {
            System.out.println("Numero incorrecto. Debe ser mayor que 0");
        } else {
            System.out.println("Ingrese un numero:");
            for (int i = 1; i <= N; i++) {
                System.out.println(i);
            }

            scanner.close();
        }

    }
}
