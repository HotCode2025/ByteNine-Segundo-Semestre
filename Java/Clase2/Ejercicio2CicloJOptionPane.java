/* Ejercicio 02: Leer un número e indicar si es positivo o 
negativo. El proceso se repitira hasta que se introduzca 
un cero 0 
 */

//Use clase JptionPane

import javax.swing.JOptionPane;

public class Ejercicio2CicloJOptionPane {
    public static void main(String[] args) {
        String input;
        int numero;
        
        // Leer el primer número
        input = JOptionPane.showInputDialog("Digite un número:");
        numero = Integer.parseInt(input);
        
        while(numero != 0) {
            if(numero > 0) {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            } else {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es NEGATIVO");
            }
            
            // Leer el siguiente número
            input = JOptionPane.showInputDialog("Digite otro número:");
            numero = Integer.parseInt(input);
        }
        
        JOptionPane.showMessageDialog(null, "El número " + numero + " finaliza el programa");
    }
}
