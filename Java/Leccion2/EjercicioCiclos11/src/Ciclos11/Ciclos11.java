/*CLASE 6:B. Programacion Orientada a objetos parte 5-Tarea
Punto: 7.2 Ejercicio Ciclos 11: Con Clase Scanner y JOption*/
/*Ejercicio 11: Diseñar un programa  que muestre el producto
de los 10 primeros numeros impares
Clase Scanner*/
package Ciclos11;
import java.util.Scanner;
public class Ciclos11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Mostrar título del programa
        System.out.println("================================================");
        System.out.println("CÁLCULO DEL PRODUCTO DE LOS 10 PRIMEROS NÚMEROS IMPARES");
        System.out.println("================================================");
        
        // Inicializar variables
        long producto = 1;
        int contador = 0;
        int numero = 1;
        
        System.out.println("\nProceso de cálculo:");
        System.out.println("-------------------");
        
        // Ciclo while para los 10 primeros números impares
        while (contador < 10) {
            long productoAnterior = producto;
            producto *= numero;
            
            System.out.println("Paso " + (contador + 1) + ": " + 
                             productoAnterior + " × " + numero + " = " + producto);
            
            contador++;
            numero += 2;
        }
        
        // Mostrar resultado final
        System.out.println("\n================================================");
        System.out.println("RESULTADO FINAL: " + producto);
        System.out.println("================================================");
        
        scanner.close();
    }
    
}
