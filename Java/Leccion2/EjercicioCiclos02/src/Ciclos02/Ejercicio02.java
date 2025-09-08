/*Clase 2:Ejercicios con ciclos y Crear Clases POO parte 0 (20-08)
Punto:-2.2 Ejercicio 2 de ciclos en Java con la clase JOption*/
//Entrada y salida datos: Clase JOption
/*Ejercicio2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un  cero 0. */
package Ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02 {

    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null, "El numero" + numero + " es POSITIVO");
            } else {
                JOptionPane.showMessageDialog(null, "El numero" + numero + " es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero " + numero + " finaliza el programa");
    }
}
