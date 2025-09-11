/*CLASE 4:tema:Clases y Objetos Poo parte 2 Tarea
Punto: 4.7 Ejercicio con ciclos 7 con la Clase Scanner y JoptionPane
Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo, 
y calcular la media*/
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digito un numero: "));
        while(numero >=0){//Mientras el nuro sea negativo
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        if (conteo==0){
            JOptionPane.showMessageDialog(null,"Error, la division entre cero no existe");
        }
        else{
            promedio = (float) suma/conteo;
            JOptionPane.showMessageDialog(null, "El promedio es: "+promedio);
        }
    }
    
}
