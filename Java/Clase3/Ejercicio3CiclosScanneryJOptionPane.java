//Ejercicios 03 Ciclos, Usamos Clase Scanner y Clase OKptionPane Primer Ejercicio Clase Scanner

package Clase3;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio3CiclosScanneryJOptionPane {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        /* 
        System.out.println("PROGRAMA PARA DETERMINAR SI UN NÚMERO ES PAR O IMPAR");
        System.out.println("Introduce números (0 para salir):");
        
        do {
            System.out.print("Introduce un número: ");
            numero = entrada.nextInt();
            
            if (numero != 0) {
                if (numero % 2 == 0) {
                    System.out.println("El número " + numero + " es PAR");
                } else {
                    System.out.println("El número " + numero + " es IMPAR");
                }
            }
            
        } while (numero != 0);
        
        System.out.println("Programa finalizado.");
        entrada.close();
    }
*/

//Ejercicio3 Usando Clase JOptionPane

        
// Scanner entrada = new Scanner(System.in);
        int numero = -1;

        // Ejercicio3 Usando Clase JOptionPane
        JOptionPane.showMessageDialog(null, 
            "PROGRAMA PARA DETERMINAR SI UN NÚMERO ES PAR O IMPAR\n" +
            "Introduce números (0 para salir)", 
            "Par o Impar", 
            JOptionPane.INFORMATION_MESSAGE);
        
        do {
            String input = JOptionPane.showInputDialog(null,
                "Introduce un número:", 
                "Entrada de datos", 
                JOptionPane.QUESTION_MESSAGE);
            
            // Verificar si el usuario hizo clic en Cancelar
            if (input == null) {
                JOptionPane.showMessageDialog(null, 
                    "Programa cancelado por el usuario", 
                    "Cancelado", 
                    JOptionPane.WARNING_MESSAGE);
                break;
            }
            
            try {
                numero = Integer.parseInt(input);
                
                if (numero != 0) {
                    String mensaje;
                    if (numero % 2 == 0) {
                        mensaje = "El número " + numero + " es PAR";
                    } else {
                        mensaje = "El número " + numero + " es IMPAR";
                    }
                    
                    JOptionPane.showMessageDialog(null, 
                        mensaje, 
                        "Resultado", 
                        JOptionPane.INFORMATION_MESSAGE);
                }
                
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, 
                    "Error: Debes introducir un número válido", 
                    "Error", 
                    JOptionPane.ERROR_MESSAGE);
                numero = -1; // Continuar el bucle
            }
            
        } while (numero != 0);
        
        JOptionPane.showMessageDialog(null, "Programa finalizado.", "Fin", JOptionPane.INFORMATION_MESSAGE);
    }    
}