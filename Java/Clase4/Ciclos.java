package Clase4;

import javax.swing.JOptionPane;

public class Ciclos {

    public static void main(String[] args) {
        int numero;
        int suma = 0;

        do {
            // Pedimos el número con un cuadro de diálogo
            numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese un número (0 para salir):")
                );
            
            suma += numero; // acumulamos el número
        } while (numero != 0);

        // Mostramos el resultado final
        JOptionPane.showMessageDialog(null,
                "La suma de todos los números es: " + suma);
    }
}