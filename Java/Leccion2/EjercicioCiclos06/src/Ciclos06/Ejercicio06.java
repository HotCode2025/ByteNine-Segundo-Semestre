/*CLASE 4:Clases y Objetos Poo parte 2 Tarea
4.5 Ejercicio con ciclos 6 Clase Scanner y JoptionPane
Ejercicio 6: Pedir numeros hasta que se tecle un 0, 
mostrar la suma de todos los numeros introducidos*/
package Ciclos06;

import javax.swing.JOptionPane;

public class Ejercicio06 {
    public static void main(String[] args) {
        int numero,suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma+= numero;
        }while(numero !=0);
        System.out.println("\nLa suma de todos los numeros ingresados es: "+suma);
    }
    
}
