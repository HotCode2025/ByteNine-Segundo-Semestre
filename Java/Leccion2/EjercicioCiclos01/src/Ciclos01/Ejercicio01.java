/*CLASE 1:Tema:Tema: Ejercicios con ciclos y Crear Clases POO parte 0(20-08)
Punto: 2.2 Ejercicio 1 de ciclos en Java sin la clase Scanner: PRESENTANDO LA CLASE JOptionPane
/*Ejercicio 1: Leer un numero y mostrar su cuadrado.
Repetir el proceso hasta que se introduzca un numero negativo.
 */
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
                 int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){ // Mientras el número sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }

}
