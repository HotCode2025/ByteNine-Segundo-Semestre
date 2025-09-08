/*Clase 3: Tema:Clases y Objetos POO parte 1 Solución(27-08)
 Punto: Ejercicio con Ciclos 3 y clase Scanner y JOptionPane*/
 /*Ejercicio 3: Leer numeros hasta que se introduzca 0
 Para cada uno indicar si es par o impar
 Primero lo haremos con la clase Scanner y luego con la clase JOptionPane*/
 /*
Al unificar las dos clases: Scanner y JOtionPane, la primera ventana emergente, 
muestra fuera del IDE (Escritorio), 
por lo cual consideramos no mezclar las dos clases y hacerlas por separadas
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class Ciclos03 {

    public static void main(String[] args) {
        /* 

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
        entrada.close();*/

        /*Ejercicio con Scanner
        Scanner entrada = new Scanner(System.in);
        int numero;

        do {
            System.out.print("Digite  un número: ");
            numero = entrada.nextInt();

            if (numero != 0) {
                if (numero % 2 == 0) {
                     
                    System.out.println("El número " + numero + " es PAR.");
                } else {
                    System.out.println("El número " + numero + " es IMPAR.");
                }
            }
        } while (numero != 0);

        System.out.println("El Programa ha finalizado porque se digito Cero (0)");*/
        
        //Ejercicio JOption
               int numero;

        do {
            // Se usa showInputDialog para pedir un número.
            // La entrada es un String y se convierte a int.
            String input = JOptionPane.showInputDialog("Digite un número: ");
            numero = Integer.parseInt(input);

            if (numero != 0) {
                if (numero % 2 == 0) {
                    JOptionPane.showMessageDialog(null, "El número " + numero + " es PAR.");
                } else {
                    JOptionPane.showMessageDialog(null, "El número " + numero + " es IMPAR.");
                }
            }
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "El Programa ha finalizado porque se digito CERO(0)");

    }

}
