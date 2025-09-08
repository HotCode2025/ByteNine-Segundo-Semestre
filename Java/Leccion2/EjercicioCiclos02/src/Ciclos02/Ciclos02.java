/*Clase 2:Tema: Ejercicios con ciclos y Crear Clases POO parte 0 (20-08)
Punto:-2.2 Ejercicio 2 de ciclos en Java con la clase Scanner*/
/*Ejercicio2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un  cero 0. */
package Ciclos02;

import java.util.Scanner;

public class Ciclos02 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El numero " + numero + " es positivo");
            } else {
                System.out.println("El numero " + numero + " es negativo");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero " + numero + " finaliza el programa");
    }

}

