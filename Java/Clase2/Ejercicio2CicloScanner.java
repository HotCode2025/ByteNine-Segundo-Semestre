/* Ejercicio 02: Leer un número e indicar si es positivo o 
negativo. El proceso se repitira hasta que se introduzca 
un cero 0 
 */

import java.util.Scanner;

public class Ejercicio2CicloScanner {
   public static void main(String[] args) { 
        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite un número: "); 

        var numero = Integer.parseInt(entrada.nextLine());

        while(numero !=0){

            if(numero > 0){
                System.out.println("El número " + numero + " es Positivo");   
            }
            else {
                System.out.println("El número " + numero + " es Negativo");
            }
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        entrada.close();
        System.out.println("El número " +numero+ " Finaliza el Programa");
   }                 
}
