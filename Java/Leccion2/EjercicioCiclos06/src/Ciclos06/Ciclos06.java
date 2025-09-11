/*CLASE 4:Clases y Objetos Poo parte 2 Tarea
4.5 Ejercicio con ciclos 6 Clase Scanner y JoptionPane
Ejercicio 6: Pedir numeros hasta que se tecle un 0, 
mostrar la suma de todos los numeros introducidos*/
package Ciclos06;

import java.util.Scanner;
public class Ciclos06 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

       int numero, suma = 0;
       do{
           System.out.println("Digite un numero: ");
           numero = Integer.parseInt(entrada.nextLine());
           suma+= numero;
       }while(numero !=0);
        System.out.println("\nLa suma de todos los numeros ingresados es: "+suma);
        
       
        
    }

}
