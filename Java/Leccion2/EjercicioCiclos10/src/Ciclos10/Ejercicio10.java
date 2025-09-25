/*CLASE 6:A. Programacion Orientada a objetos parte 4-Tarea
Punto: 6.8 Ejercicio Ciclos 10: Con Clase Scanner y JOption*/
/*Ejercicio 10: Pedir 10 numeros y escribir la suma total
Hacerlo con la clase JOptionPane*/
package ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int suma = 0;

        // Pedir 10 números usando JOptionPane
        for (int i = 1; i <= 10; i++) {
            String input = JOptionPane.showInputDialog(
                null,
                "Digite el número " + i + ":",
                "Entrada de datos",
                JOptionPane.QUESTION_MESSAGE
            );
            int numero = Integer.parseInt(input);
            suma += numero;
        }

        // Mostrar resultado
        JOptionPane.showMessageDialog(
            null,
            "La suma total es: " + suma,
            "Resultado",
            JOptionPane.INFORMATION_MESSAGE
        );
    }
}
