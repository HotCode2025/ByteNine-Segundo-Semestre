/*Clase 3: Tema:Clases y Objetos POO parte 1 Solución(27-08)
 Punto: Ejercicio con Ciclos 3 y clase Scanner y JOptionPane*/
 /*Ejercicio 3: Leer numeros hasta que se introduzca 0
 Para cada uno indicar si es par o impar
 Primero lo haremos con la clase Scanner y luego con la clase JOptionPane*/
 /*
Al unificar las dos clases: Scanner y JOtionPane, la primera ventana emergente, 
muestra fuera del IDE (Escritorio) luego apartir del segundo ingreso funciona perfecto, 

 */
package Ciclos03;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos03 {
    public static void main(String[] args) {
     
        Scanner entrada = new Scanner(System.in);
        int numero;

        do {
            System.out.println("Digite  un número: ");
            numero = entrada.nextInt();

            if (numero != 0) {
                if (numero % 2 == 0) {
                    JOptionPane.showMessageDialog(null, "El número " + numero + " es PAR.");
                } else {
                    JOptionPane.showMessageDialog(null, "El número " + numero + " es IMPAR.");
                }
            }
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "El Programa ha finalizado porque se digito CERO(0)");
        entrada.close();
    }
}
