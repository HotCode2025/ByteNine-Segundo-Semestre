package Java.Clase3;
//Ejercicio 4: Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido.
//Lo hacemos primero con la clase Scanner
//Luego lo hacemos con la clase JOptionPane
import java.util.Scanner;

import javax.swing.JOptionPane;

class EjercicioN5_Ciclos {
    public static void main(String[] args){
        /*//Con la clase Scanner
        Scanner entrada = new Scanner(System.in);
        int contador1 = 0;
        System.out.print("Ingrese un número (negativo para salir): ");
        int numero = entrada.nextInt();
        while (numero>=0){
            contador1++;
            System.out.print("Ingrese un número (negativo para salir): ");
            numero = entrada.nextInt();
        } 

        System.out.println("Cantidad de números introducidos: " + contador1 + " Con la clase Scanner");
        entrada.close();*/

        //Con la clase JOptionPane
        String input = JOptionPane.showInputDialog("Ingrese un número (negativo para salir): ");
        int numero = Integer.parseInt(input);
        int contador2 = 0;

        while (numero>=0){
            contador2++;
            input = JOptionPane.showInputDialog("Ingrese un número (negativo para salir): ");
            numero = Integer.parseInt(input);
        }

        JOptionPane.showMessageDialog(null, "Cantidad de números introducidos: " + contador2 + " Con la clase JOptionPane");
    }
}
