/*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.8 Ejercicio Ciclos 09 con Scanner y JOptionPane*/
/*Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar 
si la fecha es correcta. suponiendo que todos los meses
son de 30 dias*/
//Clase JOptionPane
package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicio09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día:"));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes:"));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año:"));

        String mensaje;
        if ((dia >= 1 && dia <= 30) && (mes >= 1 && mes <= 12) && (anio > 0)) {
            mensaje = "La fecha " + dia + "/" + mes + "/" + anio + " es correcta.";
        } else {
            mensaje = "La fecha " + dia + "/" + mes + "/" + anio + " es incorrecta.";
        }

        JOptionPane.showMessageDialog(null, mensaje);
    }
    
}
