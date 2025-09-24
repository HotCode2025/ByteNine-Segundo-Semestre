/*CLASE 6:B. Programacion Orientada a objetos parte 5-Tarea
Punto: 7.2 Ejercicio Ciclos 11: Con Clase Scanner y JOption*/
/*Ejercicio 11: Diseñar un programa  que muestre el producto
de los 10 primeros numeros impares
Clase JOptionPane*/
package Ciclos11;

import javax.swing.JOptionPane;
public class Ejercicio11 {
    public static void main(String[] args) {
        // Mostrar título del programa
        JOptionPane.showMessageDialog(null, 
            "CÁLCULO DEL PRODUCTO DE LOS 10 PRIMEROS NÚMEROS IMPARES", 
            "Ejercicio 11 - Ciclos", 
            JOptionPane.INFORMATION_MESSAGE);
        
        // Inicializar variables
        long producto = 1; // Usamos long para evitar desbordamiento
        int contador = 0;
        int numero = 1;
        StringBuilder numerosImpares = new StringBuilder();
        
        // Ciclo while para encontrar los 10 primeros números impares
        while (contador < 10) {
            // Agregar número impar a la lista (excepto el último)
            if (contador < 9) {
                numerosImpares.append(numero).append(" × ");
            } else {
                numerosImpares.append(numero);
            }
            
            producto *= numero; // Multiplicar el producto
            contador++; // Incrementar contador
            numero += 2; // Siguiente número impar
        }
        
        // Mostrar el resultado
        String mensaje = "LOS 10 PRIMEROS NÚMEROS IMPARES SON:\n";
        mensaje += numerosImpares.toString() + "\n\n";
        mensaje += "EL PRODUCTO DE TODOS ELLOS ES:\n";
        mensaje += producto;
        
        JOptionPane.showMessageDialog(null, 
            mensaje, 
            "Resultado Final", 
            JOptionPane.INFORMATION_MESSAGE);
    }
    
}
