/*CLASE 6:B. Programacion Orientada a objetos parte 5-Tarea
Punto: 7.3 Ejercicio Ciclos 12: Con Clase Scanner y JOption*/
/*Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con la clase JOptionPane*/
package Ciclos12;

import javax.swing.JOptionPane;
public class Ejercicio12 {
    public static void main(String[] args) {
        // Mostrar título del programa
        JOptionPane.showMessageDialog(null, 
            "CALCULADORA DE FACTORIAL", 
            "Ejercicio 12 - Ciclos", 
            JOptionPane.INFORMATION_MESSAGE);
        
        // Pedir número al usuario usando JOptionPane
        String input = JOptionPane.showInputDialog("Ingrese un número para calcular su factorial:");
        int numero = Integer.parseInt(input);
        
        // Validar que el número no sea negativo
        if (numero < 0) {
            JOptionPane.showMessageDialog(null, 
                "ERROR: No existe factorial para números negativos.", 
                "Error", 
                JOptionPane.ERROR_MESSAGE);
        } else {
            long factorial = 1;
            StringBuilder proceso = new StringBuilder();
            StringBuilder detalles = new StringBuilder();
            
            // CICLO FOR para calcular el factorial
            detalles.append("PROCESO DE CÁLCULO:\n");
            detalles.append("-------------------\n");
            
            for (int i = 1; i <= numero; i++) {
                factorial *= i;
                proceso.append(i);
                if (i < numero) {
                    proceso.append(" × ");
                }
                detalles.append(i + "! = " + factorial + "\n");
            }
            
            // Mostrar resultado final
            String mensaje = "NÚMERO INGRESADO: " + numero + "\n\n";
            mensaje += detalles.toString() + "\n";
            mensaje += "RESULTADO FINAL:\n";
            mensaje += numero + "! = " + proceso.toString() + " = " + factorial;
            
            JOptionPane.showMessageDialog(null, 
                mensaje, 
                "Resultado del Factorial", 
                JOptionPane.INFORMATION_MESSAGE);
        }
    }
}
