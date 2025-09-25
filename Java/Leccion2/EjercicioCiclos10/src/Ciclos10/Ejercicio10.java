/*CLASE 6:A. Programacion Orientada a objetos parte 4-Tarea
Punto: 6.8 Ejercicio Ciclos 10: Con Clase Scanner y JOption*/
/*Ejercicio 10: Pedir 10 numeros y escribir la suma total
Hacerlo con la clase JOptionPane*/
package ciclos10;

import java.util.Scanner;

public class Ejercicio10 {
    
    // Método que pide 10 números con Scanner y devuelve la suma	
    public int pedirNumeros() {
        Scanner entrada = new Scanner(System.in);
        int suma = 0;
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite el número " + i + ": ");
            int numero = entrada.nextInt(); // lee el número del usuario
            suma += numero; // acumula la suma
        }
        return suma; // devuelve la suma total
    }
}
