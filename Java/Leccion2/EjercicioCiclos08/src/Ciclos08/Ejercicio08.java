/*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.7Ejercicio Ciclos 08 con Scanner y JOptionPane*/
//Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N.
//Clase JOptionPane

package Ciclos08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog(null, "Ingrese un numero N mayor a 0):");
        if (entrada == null) {
            JOptionPane.showMessageDialog(null, "Mal ingresado.");
            return;
        }

        int N = Integer.parseInt(entrada); // <-- sin try/catch
        if (N <= 0) {
            JOptionPane.showMessageDialog(null, "El numero debe ser mayor que 0");
            return;
        }

        int contador = 1;
        StringBuilder resultado = new StringBuilder();
        while (contador <= N) {
            resultado.append(contador).append("\n");
            contador++;
        }
        JOptionPane.showMessageDialog(null, resultado.toString());
    }
}
