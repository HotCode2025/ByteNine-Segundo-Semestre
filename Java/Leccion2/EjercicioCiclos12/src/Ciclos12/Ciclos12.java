/*CLASE 6:B. Programacion Orientada a objetos parte 5-Tarea
Punto: 7.3 Ejercicio Ciclos 12: Con Clase Scanner y JOption*/
/*Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con la clase Scanner*/
package Ciclos12;

import java.util.Scanner;
public class Ciclos12 {
  public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("====================================");
        System.out.println("      CALCULADORA DE FACTORIAL");
        System.out.println("====================================");
        
        System.out.print("Ingrese un número: ");
        int numero = scanner.nextInt();
        
        if (numero < 0) {
            System.out.println("ERROR: No existe factorial para números negativos.");
        } else {
            long factorial = 1;
            int i = 1;
            
            // CICLO WHILE para calcular factorial
            System.out.println("\nCalculando con ciclo WHILE:");
            System.out.println("---------------------------");
            while (i <= numero) {
                factorial *= i;
                System.out.println(i + "! = " + factorial);
                i++;
            }
            
            System.out.println("\nResultado: " + numero + "! = " + factorial);
        }
        
        scanner.close();
    }
}
