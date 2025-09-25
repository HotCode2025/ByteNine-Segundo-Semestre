/*CLASE 6:A. Programacion Orientada a objetos parte 4-Tarea
Punto: 6.8 Ejercicio Ciclos 10: Con Clase Scanner y JOption*/
/*Ejercicio 10: Pedir 10 numeros y escribir la suma total
Hacerlo con la clase Scanner*/
package ciclos10;

import javax.swing.JOptionPane;

public class Ciclos10 {
    public static void main(String[] args) {
        // Creamos un objeto de la clase Ejercicio10
        Ejercicio10 ejercicio = new Ejercicio10();

	// Se llama al método pedirNumeros que hace la suma
        int suma = ejercicio.pedirNumeros();
        
        // Mostramos el resultado con JOptionPane
        JOptionPane.showMessageDialog(null, "La suma total es: " + suma);
    }
}