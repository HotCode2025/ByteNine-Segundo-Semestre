/*CLASE 6:A. Programacion Orientada a objetos parte 4-Tarea
Punto: 6.8 Ejercicio Ciclos 10: Con Clase Scanner y JOption*/
/*Ejercicio 10: Pedir 10 numeros y escribir la suma total
Hacerlo con la clase Scanner*/
package ciclos10;

import java.util.Scanner;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0;

        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite el número " + i + ": ");
            int numero = entrada.nextInt();
            suma += numero;
        }

        System.out.println("\nLa suma total es: " + suma);

        entrada.close();
    }
}
